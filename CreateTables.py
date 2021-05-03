import boto3

resource = boto3.resource('dynamodb')

#creates the movie table 
table = resource.create_table(
    TableName='MikeDawickiMovies2',
    KeySchema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH' # Partition Key
            },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE' #Sort Key
            }
       ],
       AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
            },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
            },
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
        }
    )
            

#creates the production table
table = resource.create_table(
    TableName='MikeDawickiAWProductionBOM',
    KeySchema=[
        {
            'AttributeName': 'ProductID',
            'KeyType': 'HASH'  # Partition key
            },
        {
            'AttributeName': 'ProductName',
            'KeyType': 'RANGE'  # Sort key
            }
        ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ProductID',
            'AttributeType': 'S'
            },
        {
            'AttributeName': 'ProductName',
            'AttributeType': 'S'
            },
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
        }
    )
