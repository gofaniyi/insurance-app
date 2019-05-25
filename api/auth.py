import jwt
from datetime import datetime as dt, timedelta
from config import AppConfig
from exception.validation import ValidationError
from api.constants.messages import (ERROR_MESSAGES,)

class AuthToken:

    @staticmethod
    def encode_auth_token(user_id, days=1):
        """
        Generates the Auth Token
        """
        try:
            payload = {
                'exp': dt.utcnow() + timedelta(days=days),
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
        except (
                ValueError,
                TypeError,
                jwt.ExpiredSignatureError,
                jwt.DecodeError,
                jwt.InvalidTokenError,
                jwt.InvalidSignatureError,
                jwt.InvalidAlgorithmError,
                jwt.InvalidIssuerError,
        ) as error:
            exception_mapper = {
                ValueError: (ERROR_MESSAGES['SERVER'], 500),
                TypeError: (ERROR_MESSAGES['SERVER'], 500),
                jwt.ExpiredSignatureError: (ERROR_MESSAGES['JWT_EXPIRED_TOKEN'],
                                            401),
                jwt.DecodeError: (ERROR_MESSAGES['JWT_INVALID_TOKEN'], 401),
                jwt.InvalidTokenError: (ERROR_MESSAGES['JWT_INVALID_TOKEN'], 401),
                jwt.InvalidIssuerError: (ERROR_MESSAGES['JWT_ISSUER'], 401),
                jwt.InvalidAlgorithmError: (ERROR_MESSAGES['JWT_ALGORITHM'],
                                            401),
                jwt.InvalidSignatureError: (ERROR_MESSAGES['JWT_SIGNATURE'], 500)
            }
            message, status_code = exception_mapper.get(
                type(error), (ERROR_MESSAGES['SERVER'], 500))
            raise ValidationError({'message': message}, status_code)