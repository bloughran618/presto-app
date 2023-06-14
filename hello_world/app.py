import json


def lambda_handler(event, context):

    # do stuff

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello to all Presto engineers! :)",
        }),
    }
