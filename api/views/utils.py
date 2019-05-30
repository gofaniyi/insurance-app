
# get auth token
def get_auth_token(request):
    auth_token = ''
    auth_header = request.headers.get('Authorization')
    
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    return auth_token


def parse_attributes_data(risk_type, attributes_schema_data,
                          risk_type_id):
    """Helper method to parse and update attribute data

    Args:
        risk_type (object): risk type object
        attributes_schema_data (Attributes): Data from the attributes schema
        risk_type_id (int): The risk type Id

    """
    risk_type.attributes.delete()

    for each in attributes_schema_data:
        risk_type.attributes.append(each)