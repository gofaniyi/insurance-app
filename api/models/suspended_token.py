from datetime import datetime as dt

from .base import BaseModel

from api.database import db

class SuspendedToken(BaseModel):
    """ Token Model for storing suspended JWT tokens"""

    __tablename__ = 'suspended_tokens'

    token = db.Column(db.String(500), unique=True, nullable=False)
    suspended_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.suspended_on = dt.utcnow()

    def __repr__(self):
        return f'<Token: {self.token}>'