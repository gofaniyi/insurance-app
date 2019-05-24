# get auth token
def get_auth_token(request):
    auth_token = ''
    auth_header = request.headers.get('Authorization')
    
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    return auth_token