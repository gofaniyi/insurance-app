ERROR_MESSAGES = {
    'SERVER' : 'Authorization failed. Please contact support',
    'JWT_EXPIRED_TOKEN' : 'Token expired. Please login to get a new token',
    'JWT_INVALID_TOKEN' : 'Authorization failed due to an Invalid token',
    'JWT_ISSUER' : 'Cannot verify the token provided as the expected issuer does not match',
    'JWT_ALGORITHM' : 'Cannot verify the token provided as it was signed with a different algorithm',
    'JWT_SIGNATURE' : 'Cannot verify the signature of the token provided as it was signed by a non matching private key',
    'USER_LOGIN' : 'User login attempt failed',
    'INVALID_LOGIN_CREDENTIALS' : 'Email or password is incorrect',
    'PASSWORDS_MISMATCH' : 'Passwords do not match',
    'INVALID_EMAIL' : 'This is an invalid email address',
    'DEFAULT' : 'An error occurred',
    'NOT_STRONG_PASSWORD' : 'Password should be at least 8 characters',
    'EMAIL_EXISTS' : 'Email already exist',
    'EMPTY_PAYLOAD' : 'No valid field(s) in request body',
    'REQUIRED_FIELD' : 'This field is required'
}


SUCCESS_MESSAGES = {
    'USER_LOGOUT' : 'User logged out successfully',
    'USER_LOGIN' : 'User logged in successfully',
    'USER_SIGNUP' : 'User signup successfully',
}
