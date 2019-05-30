from .base import BaseModel, db
from sqlalchemy.dialects.postgresql import JSON

class Risk(BaseModel):
    """ Model for storing risks"""

    __tablename__ = 'risks'

    data = db.Column(JSON, nullable=True)
    risk_type_id = db.Column(
        db.Integer, db.ForeignKey('risk_types.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship('Company', backref='risks')


    def __repr__(self):
        return '<Risk>'