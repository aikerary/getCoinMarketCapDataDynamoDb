import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CryptoPrecios')

def lambda_handler(event, context):
    crypto_id = event['pathParameters']['cryptoId']

    response = table.scan(
        FilterExpression=boto3.dynamodb.conditions.Key('CryptoId').eq(crypto_id)
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(items)
    }