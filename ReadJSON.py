import boto3
import json
from decimal import Decimal 

resource=boto3.resource('dynamodb')
#holds the production table 
table = resource.Table('MikeDawickiAWProductionBOM')

#open the json file
with open('AW BOM.json') as json_file:
    #load the json data from the file
    data = json.load(json_file, parse_float=Decimal)
    #loop through the data
    for p in data:
            try:
                #populate dynamodb table
                table.put_item(
                    Item={'ProductID': p['ProductID'],
                          'ProductName': p['ProductName'],
                          'Category': p['Category'],
                          'Subcategory': p['Subcategory'],
                          'ListPrice': (p['ListPrice']),
                          'BOM': p['BOM']
                          }
                    )
                #print out all information for each product 
                print('Product ID: ' + p['ProductID'])
                print('Product Name: ' + p['ProductName'])
                print('Category: ' + p['Category'])
                print('Subcategory: ' + p['Subcategory'])
                print('List Price: ' + str(p['ListPrice']))
                print('BOM: ' + p['BOM'])
                print('')
            except Exception:
                print('Item has no BOM!')
