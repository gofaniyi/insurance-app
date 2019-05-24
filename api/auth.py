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
                ValueError: ('Authorization failed. Please contact support.', 500),
                TypeError: ('Authorization failed. Please contact support.', 500),
                jwt.ExpiredSignatureError: ('Token expired. Please login to get a new token',
                                            401),
                jwt.DecodeError: ('Authorization failed due to an Invalid token.', 401),
                jwt.InvalidTokenError: ('Authorization failed due to an Invalid token.', 401),
                jwt.InvalidIssuerError: ('Cannot verify the token provided as the expected issuer does not match.', 401),
                jwt.InvalidAlgorithmError: ('Cannot verify the token provided as it was signed with a different algorithm.',
                                            401),
                jwt.InvalidSignatureError: ('Cannot verify the signature of the token provided as it was signed by a non matching private key', 500)
            }
            message, status_code = exception_mapper.get(
                type(error), ('Authorization failed. Please contact support.', 500))
            raise ValidationError({'message': message}, status_code)