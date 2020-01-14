from app.models import Survey, Observation


def test_new_survey():
    survey = Survey(name='hiren raj')
    assert survey.name == 'hiren raj'


def test_new_observation():
    observation = Observation(survey_id=1, value=3.3, frequency=10)
    assert observation.value == 3.3
    assert observation.survey_id == 1
    assert observation.frequency == 10


def test_survey_can_delete():
    survey = Survey(name='Hiren Raj')
    assert survey.can_delete() == 'Exception: Deletion not allowed. Magic value!'
