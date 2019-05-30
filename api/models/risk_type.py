from .base import BaseModel, db
from exception.validation import ValidationError

from api.constants.messages import ERROR_MESSAGES

class RiskType(BaseModel):
    """ Model for storing risk types"""

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

    risks = db.relationship(
        'Risk',
        backref='risk_type',
        cascade='save-update, delete',
        lazy='dynamic')

    def __repr__(self):
        return '<RiskType {}>'.format(self.name)

    def get_child_relationships(self):
        return (self.risks, )

    @property
    def risks_count(self):
        return self.risks.count()


    def delete(self):
        """ Delete a Risk Type """
        
        if self.risks.count() > 0:
            raise ValidationError(
            {
                'message': ERROR_MESSAGES['DELETING_RELATED_OBJECTS'].format('Risk type', 'Risks'),
            }, 400)
            
        #Remove attributes
        self.attributes.delete()
        return super(RiskType, self).delete()