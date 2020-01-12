from flask import render_template
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


# @app.route('/stat/<int:observation_id>', methods=['GET', 'PUT'])
# def stat(observation_id=None):
#     return Observation.get_delete_put_post(observation_id)


@app.route('/stat/<int:survey_id>', methods=['GET', 'PUT'])
def stat(survey_id=None):
    # observation = Observation.query.get_or_404(survey_id)
    # return Observation.json_filter_by(survey_id=survey_id)
    return Observation.get_delete_put_post(survey_id=survey_id,user=Observation,prop_filters=survey_id)
    # return Observation.get_delete_put_post(survey_id)
