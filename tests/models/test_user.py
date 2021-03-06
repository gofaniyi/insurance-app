"""Test model user module"""

# Local Modules
from api.models import User

from tests.base import fake
from mock.user import USER_ONE_VALID_PASSWORD, INVALID_PASSWORD

class TestUserModel:

    def test_save(self, init_db, new_company):
        """Test for creating a new user
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        params = {
            'company_id' : new_company.id,
            'email': fake.email(),
            'password' : fake.password()
        }
        user = User(**params)
        assert user == user.save()

    def test_get(self, init_db, new_user):
        """Test for get method

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_user (User): Fixture to create a new user
        """
        assert User.get(new_user.id) == new_user

    def test_update(self, init_db, new_user):
        """Test for update method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_user (User): Fixture to create a new user
        """
        new_user.update(admin=True)
        assert new_user.admin == True

    def test_delete(self, init_db, new_user):
        """Test for delete method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_user (User): Fixture to create a new user
        """
        new_user.delete()
        assert User.get(new_user.id) == None

    def test_model_string_representation(self, init_db, new_user):
        """ Should compute the string representation of a user

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            new_user (User): Fixture to create a new user
        """
        assert repr(new_user) == f'<User: {new_user.email}>'


    def test_user_authenticate_with_right_credentials_succeeds(self, init_db, user_one):
        """

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """
        user, is_authenticated = User.authenticate(user_one.email, USER_ONE_VALID_PASSWORD)
        assert user is not None
        assert user.email == user_one.email
        assert is_authenticated == True

    def test_user_authenticate_with_wrong_password_fails(self, init_db, user_one):
        """

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """
        user, is_authenticated = User.authenticate(user_one.email, INVALID_PASSWORD )
        assert user is not None
        assert user.email == user_one.email
        assert is_authenticated == False

    def test_user_authenticate_with_wrong_email_fails(self, init_db, user_one):
        """

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """
        user, is_authenticated = User.authenticate('wrongemail@example.com', USER_ONE_VALID_PASSWORD)
        assert user is None
        assert is_authenticated == False

    def test_user_logout(self, init_db):
        """

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        status = User.logout(fake.alphanumeric())
        assert status == True

