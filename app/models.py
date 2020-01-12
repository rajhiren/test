from app import db
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db


class Survey(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    observations = db.relationship('Observation', backref='author', lazy='dynamic')

    # serializer fields
    create_fields = update_fields = ['name']

    # check if flask-serialize can delete
    def can_delete(self):
        if self.name == 'Hiren Raj':
            raise Exception('Deletion not allowed. Magic value!')

    # checks if Flask-Serialize can create/update
    def verify(self, create=False):
        if not self.name or len(self.name) < 1:
            raise Exception('Missing Name')

    def __repr__(self):
        return '<name : {}, id : {}>'.format(self.name, self.id)
        # return dict(name=self.name, id=self.id)


class Observation(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    value = db.Column(db.Float)
    frequency = db.Column(db.Integer)

    # serializer fields
    create_fields = update_fields = ['survey_id', 'value', 'frequency']

    # checks if Flask-Serialize can create/update
    def verify(self, create=False):
        if not self.value or len(self.value) < 1:
            raise Exception('Invalid value')
        elif not self.frequency or len(self.frequency) < 1:
            raise Exception('Invalid Frequency')
        elif not self.survey_id or len(self.survey_id) < 1:
            raise Exception('Invalid Survey_id')
        # elif self.survey_id not in Survey.query.filter_by(id=self.survey_id).all():
        #     raise Exception(Survey.dict_list(Survey.query.filter_by(id=self.survey_id).all()))
        # elif isinstance(self.survey_id, int):
        #     raise Exception('Survey ID not integer')

    def __repr__(self):
        return '<Setting %r %r %r>' % (self.survey_id, self.value, self.frequency)
