from flask import render_template, request
from app import app
from app.models import Survey, Observation


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    surveys = Survey.query.all()
    observations = Observation.query.all()
    return render_template('index.html', title='Surveys', surveys=surveys, observations=observations)


@app.route("/results")
def results():
    observations = Observation.query.all()
    return render_template('results.html', title='Results', observations=observations)


@app.route('/result/<survey_id>', methods=['GET'])
def result(survey_id):
    observation = Observation.query.filter_by(survey_id=survey_id).all()
    return render_template('results.html', title='Results', observations=observation)


@app.route('/survey/<int:survey_id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
@app.route('/survey', methods=['GET', 'POST'])
def survey(survey_id=None):
    return Survey.get_delete_put_post(survey_id)


@app.route('/stat/<int:id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def stat(id=None):
    # when we add observation for survey using form-post only
    if request.form:
        if Observation.request_create_form(survey_id=id, value=request.form.get('value'),
                                           frequency=request.form.get('frequency')):
            return "Observation Added for Survey : {}".format(id)
        else:
            return "Operation not permitted"
    elif request.args:
        return Observation.get_delete_put_post(id)
    else:
        return Observation.get_delete_put_post(id)
