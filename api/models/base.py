"""Module for generic model operations mixin."""

import re

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
                    f'{re.sub(r"(?<=[a-z])[A-Z]+",lambda x: f" {x.group(0).lower()}" , cls.__name__)} not found'
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

    @classmethod
    def find_or_create(cls, data, **kwargs):
        """
        Finds a model instance or creates it
        """
        instance = cls.query.filter_by(**kwargs).first()
        if not instance:
            instance = cls(**data).save()
        return instance

    @classmethod
    def bulk_create(cls, raw_list):
        """
        Save raw list of records to database

        Parameters:
            raw_list(list): List of records to be saved to database
        """
        resource_list = [cls(**item) for item in raw_list]
        db.session.add_all(resource_list)
        db.session.commit()
        return resource_list

    
    @classmethod
    def exists(cls, value, column='id'):
        """Verifies whether the specified id exists in the database

        This method uses an SQL statement which returns no row data to check
        whether a record exists. It is therefore more efficient than the
        `Model.get` method when verifying existence is all that is required.

        Examples:
            User.exists(token_id, 'token_id')

        Args:
            column (str): The column to check. Defaults to 'id'
            value (str): The value to verify

        Returns:
            bool: True if the value exists, False otherwise
        """
        EXISTS = \
        """
            SELECT 1
            FROM {table}
            WHERE {table}.{column} = '{value}'
            AND {table}.deleted = false
        """

        query = EXISTS.format(
            table=cls.__table__.name, column=column, value=value)
        result = db.engine.execute(query).scalar()
        if result:
            return True
        return False
