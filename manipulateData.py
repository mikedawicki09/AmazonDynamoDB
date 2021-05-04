import boto3


resource = boto3.resource('dynamodb')
#holds the movies table 
table = resource.Table('MikeDawickiMovies')


#displays the table name and the date and time it was created 
print('Table:', table.table_name, 'was created:', table.creation_date_time)

#displays the number of records in the database
print('Table',table.table_name,'has', table.item_count, 'items')

#displays the table's metadata
print('Table', table.table_name, 'metadata:',table.attribute_definitions)

#inserts an item into the database
table.put_item(
    Item={
        'title': 'Justice League',
        'year': 2021,
        'OtherStuff': 'Determined to ensure Superman’s ultimate sacrifice was not in vain, Bruce Wayne aligns forces with Diana Prince with plans to recruit a team of metahumans to protect the world from an approaching threat of catastrophic proportions. Cited from https://www.imdb.com/title/tt12361974/?ref_=nv_sr_srsg_0'
        }
    )
#getting an item from the database
response = table.get_item(
    Key= {
        'title': 'Justice League',
        'year': 2021
        }
    )

#displays the title, year and description of the movie
print(response['Item']['OtherStuff'])

#updates an item in the table
table.update_item(
    Key={
        'title':'Justice League',
        'year':2021
        },
    UpdateExpression='set OtherStuff = :val',
    ExpressionAttributeValues={':val': 'Updated'},
)

#delete item from a table
table.delete_item(
    Key={
        'title': 'Justice League',
        'year':2021
        },
    )

#delete table from the database
table1 = resource.Table('MikeDawickiMovies2')
table1.delete()
