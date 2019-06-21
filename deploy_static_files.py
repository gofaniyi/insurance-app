import flask_s3

from collections import namedtuple

MyStruct = namedtuple('MyStruct', 'config static_folder static_url_path')

def deploy():
    """
    upload static files to s3

    Return:
        func: call the function if successful or the click help option if unsuccesful
    """
    print('Uploading static files to S3....')
    params = { 
        'config' : {
            'FLASKS3_BUCKET_NAME': 'zappa-ok587zsna',
        },
        'static_folder' : './dist/static',
        'static_url_path' : '/static'
    }
    app = MyStruct(**params)
    flask_s3.create_all(app)

    print('Uploaded static files to S3.....')


deploy()