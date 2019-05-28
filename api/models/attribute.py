from .base import BaseModel, db

class Attribute(BaseModel):
    """
    Model for attributes
    """

    _key = db.Column(db.String(60), nullable=False)
    label = db.Column(db.String(60), nullable=False)
    is_required = db.Column(db.Boolean, nullable=False)
    input_control = db.Column(db.String(60), nullable=False)
    choices = db.Column(db.String(250), nullable=True)
    risk_type_id = db.Column(db.Integer,
                                  db.ForeignKey('risk_types.id'),
                                  nullable=False)


    def __repr__(self):
        return '<Attribute {}>'.format(self.label)