from app import db
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db


class Survey(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    observations = db.relationship('Observation', backref='author', lazy='dynamic')

    # serializer fields
    create_fields = update_fields = ['name']

    # @property
    # def name(self):
    #     return self.name
    # check if flask-serialize can delete
    def can_delete(self):
        if self.name == 'Hiren Raj':
            raise Exception('Deletion not allowed. Magic value!')

    # checks if Flask-Serialize can create/update
    def verify(self, create=False):
        if not self.name or len(self.name) < 1:
            raise Exception('Missing Name')

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Observation(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    value = db.Column(db.Float)
    frequency = db.Column(db.Integer)

    # serializer fields
    create_fields = update_fields = ['survey_id', 'value', 'frequency']

    def __repr__(self):
        return '<Value {}>'.format(self.value)
