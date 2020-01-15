from app.models import Survey, Observation
import pytest


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
    with pytest.raises(Exception):
        survey.can_delete()


def test_survey_verify():
    survey = Survey(name='')
    with pytest.raises(Exception):
        survey.verify(survey)


def test_survey_repr():
    survey = repr(Survey(name='Test'))
    assert survey == '<name : Test>'



def test_obs_verify():
    obs = repr(Observation(survey_id=1, value=1.1, frequency=10))
    assert obs == '<Observation 1 1.1 10>'
