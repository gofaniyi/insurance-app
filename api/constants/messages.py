ERROR_MESSAGES = {
    'SERVER' : 'Authorization failed. Please contact support.',
    'JWT_EXPIRED_TOKEN' : 'Token expired. Please login to get a new token.',
    'JWT_INVALID_TOKEN' : 'Authorization failed due to an Invalid token.',
    'JWT_ISSUER' : 'Cannot verify the token provided as the expected issuer does not match.',
    'JWT_ALGORITHM' : 'Cannot verify the token provided as it was signed with a different algorithm.',
    'JWT_SIGNATURE' : 'Cannot verify the signature of the token provided as it was signed by a non matching private key.',
    'USER_LOGIN' : 'User login attempt failed.',
    'INVALID_LOGIN_CREDENTIALS' : 'Email or password is incorrect.'
}


SUCCESS_MESSAGES = {
    'USER_LOGOUT' : 'User logged out successfully.',
    'USER_LOGIN' : 'User logged in successfully'
}
