from chalice import Chalice
from chalice import ChaliceUnhandledError

from aws_lambda_powertools import Logger
from requests import Response

from chalicelib.blueprints import extra_routes
from chalicelib.controllers import UserController

app = Chalice(app_name='chalice-sample')

app.register_blueprint(extra_routes)

logger = Logger(service='sample')

# app.log.setLevel(logging.DEBUG)

# import os
#
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# log_format = (
#     '[%(levelname)s] %(asctime)s.%(msecs)dZ (%(aws_request_id)s) '
#     '%(filename)s:%(funcName)s[%(lineno)d] %(message)s'
# )
# if os.environ.get('IS_LOCAL'):
#     log_format = (
#         '[%(levelname)s] %(asctime)s.%(msecs)dZ '
#         '%(filename)s:%(funcName)s[%(lineno)d] %(message)s'
#     )
# formatter = logging.Formatter(log_format, '%Y-%m-%dT%H:%M:%S')
# for handler in logger.handlers:
#     handler.setFormatter(formatter)


@app.middleware('all')
def handle_errors(event, get_response):
    print('a')
    try:
        return get_response(event)
    except ChaliceUnhandledError as e:
        return Response(status_code=500, body=str(e),
                        headers={'Content-Type': 'text/plain'})

@app.route('/')
def index():
    # u = Util()
    # url = 'https://7rfvck7gef.execute-api.us-east-1.amazonaws.com/dev/'
    # response = requests.get(url)
    logger.info('test')
    logger.info('テスト')
    return {'hello': 'world'}


@app.route('/main')
def index_main():
    # u = Util()
    # url = 'https://7rfvck7gef.execute-api.us-east-1.amazonaws.com/dev/'
    # response = requests.get(url)
    logger.info('test')
    logger.info('テスト')
    return {'hello': 'world'}


@app.route('/test')
def index_test():
    # u = Util()
    # url = 'https://7rfvck7gef.execute-api.us-east-1.amazonaws.com/dev/'
    # response = requests.get(url)
    logger.info('test')
    logger.info('テスト')
    return {'hello': 'world'}


@app.lambda_function()
@app.route('/sample')
def index_2():
    return {'msg': 'function'}


@app.lambda_function()
@app.route('/sp')
def index_sample():
    return {'msg': 'function'}


@app.lambda_function(name='YnFunc01')
@app.route('/user')
def user_list():
    user = UserController()
    return user.list()


@app.lambda_function(name='YnFunc02')
@app.route('/detail')
def user_detail():
    user = UserController()
    args = 'a'
    return user.detail(args)


@app.route('/aws')
def aws_sample():
    import boto3
    conf = {
        'aws_access_key_id': 'aws_access_key_id',
        'aws_secret_access_key': 'aws_secret_access_key',
        'region_name': 'ap-northeast-1',
        'endpoint_url': 'http://dynamodb-local:8000'
    }
    client = boto3.client('dynamodb', **conf)
    return client.list_tables()


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
