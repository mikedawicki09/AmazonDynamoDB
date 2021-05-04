import boto3

resource=boto3.resource('dynamodb')

table = resource.Table('MikeDawickiAWProductionBOM')
