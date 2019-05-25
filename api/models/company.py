"""Module for Company model."""

# Database
from .base import BaseModel, db


class Company(BaseModel):
    """Class for companies db table."""

    __tablename__ = 'companies'

    name = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'<Company: {self.name}>'