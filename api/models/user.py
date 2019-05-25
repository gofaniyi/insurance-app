"""Module for User model."""
# System imports
from datetime import datetime as dt

#middlewares
from exception.validation import ValidationError

from config import AppConfig

from api.bcrypt import bcrypt

from api.auth import AuthToken

from .base import BaseModel, db
from .suspended_token import SuspendedToken


class User(BaseModel):
    """Class for user db table."""

    __tablename__ = 'users'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    company = db.relationship('Company', backref='users')


    def set_password(self):
        self.password = bcrypt.generate_password_hash(
            self.password, AppConfig.BCRYPT_LOG_ROUNDS
        ).decode()

    
    def save(self):
        """
        Override to save a user model instance
        """
        self.set_password()
        return super(User, self).save()

    @property
    def token(self):
        return AuthToken.encode_auth_token(self.id).decode('utf-8')

    @staticmethod
    def logout(token=''):
        param = {
            'token' : token
        }
        suspended_token = SuspendedToken(**param)
        suspended_token.save()
        return True

    
    @staticmethod
    def authenticate(email, password):
        user = User.get_by_email(email=email)

        if user and bcrypt.check_password_hash(user.password, password):
            return user, True
        return user, False


    
    @classmethod
    def get_by_email(cls, email):
        """
        return entries by email
        """
        return cls.query.filter_by(email=email).first()


    def __repr__(self):
        return f'<User: {self.email}>'