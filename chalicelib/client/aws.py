import boto3
import botocore


class Dynamodb:
    def __init__(self) -> None:
        config = {
            'aws_access_key_id': 'aws_access_key_id',
            'aws_secret_access_key': 'aws_secret_access_key',
            'region_name': 'ap-northeast-1',
            'endpoint_url': 'http://dynamodb-local:8000'
        }
        self.__client = boto3.client('dynamodb', **config)
        self.__table = 'UserInfoTable'

    def get(self) -> botocore.client:
        return self.__client
