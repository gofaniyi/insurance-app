"""Module for generic model operations mixin."""

import re

from flask import request

from datetime import datetime as dt

from api.database import db

# validators
from exception.validation import ValidationError

class BaseModel(db.Model):
    """Mixin class with generic model operations."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=dt.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=dt.utcnow)

    def save(self):
        """
        Save a model instance
        """

        db.session.add(self)
        db.session.commit()
        return self

    


    def update(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)

        db.session.commit()
        return self


    @classmethod
    def get(cls, id):
        """
        return entries by id
        """
        return cls.query.filter_by(id=id).first()


    @classmethod
    def filter(cls, **kwargs):
        """
        return entries 
        """
        return cls.query.filter_by(**kwargs)


    @classmethod
    def get_or_404(cls, id):
        """
        return entries by id
        """

        record = cls.get(id)

        if not record:
            raise ValidationError(
                {
                    'message':
                    f'{re.sub(r"(?<=[a-z])[A-Z]+",lambda x: f" {x.group(0).lower()}" , (cls.__name__))} not found'
                },
                404)

        return record

    def get_child_relationships(self):
        """
        Method to get all child relationships a model has.
        This is used to ascertain if a model has relationship(s) or
        not when validating delete operation.
        It must be overridden in subclasses and takes no argument.
        :return None if there are no child relationships.
        A tuple of all child relationships eg (self.relationship_field1,
        self.relationship_field2)
        """
        raise NotImplementedError(
            "The get_relationships method must be overridden in all child model classes"
        )  #noqa


    def delete(self):
        """
        Delete a model instance.
        """
        db.session.delete(self)
        db.session.commit()
        return True