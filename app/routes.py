from flask import render_template, request
from app import app
from app.models import Survey, Observation, db


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


# @app.route('/stat/<int:observation_id>', methods=['GET', 'PUT'])
# def obs(observation_id=None):
#     return Observation.get_delete_put_post(observation_id)


@app.route('/stat/<int:survey_id>', methods=['GET', 'PUT', 'POST'])
def stat(survey_id=None):
    if request.form:
        # raise Exception(survey_id)
        observation = Observation(survey_id=survey_id, value=request.form.get('value'), frequency=request.form.get('frequency') )
        db.session.add(observation)
        db.session.commit()
    return 'Observation Added', 200
    # return Observation.get_delete_put_post(survey_id)
