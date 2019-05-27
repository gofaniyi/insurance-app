from datetime import datetime as dt

from .base import BaseModel, db

class RiskType(BaseModel):
    """ Token Model for storing risk types"""

    __tablename__ = 'risk_types'

    name = db.Column(db.String(255), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship('Company', backref='risk_types')

    attributes = db.relationship(
        'Attribute',
        backref='risk_type',
        cascade='save-update, delete',
        lazy='dynamic')

    eager_loaded_attributes = db.relationship(
        'Attribute', lazy='joined', viewonly=True)

    def __repr__(self):
        return '<RiskType {}>'.format(self.name)