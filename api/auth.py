import jwt
from datetime import datetime as dt, timedelta
from config import AppConfig
from exception.validation import ValidationError


class AuthToken:

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        """
        try:
            payload = {
                'exp': dt.utcnow() + timedelta(days=1),
                'iat': dt.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                AppConfig.JWT_SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            raise e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, AppConfig.JWT_SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise ValidationError('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise ValidationError('Invalid token. Please log in again.')