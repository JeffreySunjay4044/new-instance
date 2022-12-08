import base64
import json

import boto3
from botocore.exceptions import ClientError

region_name= "us-east-1"


def get_secret(secret_name: str) -> dict:

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        exceptions = ['DecryptionFailureException', 'InternalServiceErrorException', 'InvalidParameterException', 'InvalidRequestException', 'ResourceNotFoundException']
        if e.response['Error']['Code'] in exceptions:
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    return json.loads(secret)  # returns the secret as dictionary
