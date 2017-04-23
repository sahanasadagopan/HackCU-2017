import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings




def get_move():
    moveCommand = ""
    #dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIAJMHJ2TULWSOIOMVQ', aws_secret_access_key='yYUv1YPFZbCF7Wej8ZcC')
    #dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id='AKIAJMHJ2TULWSOIOMVQ', aws_secret_access_key='yYUv1YPFZbCF7Wej8ZcC')
    
    session = boto3.Session(
            aws_access_key_id='XXXXXX',
            aws_secret_access_key='XXXXXX',
            region_name='us-east-1',
        )
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('RobotCommands')
    
    #print(list(dynamodb.tables.all()))
#     newMove = "Move";
#     response = table.update_item(
#         Key={
#             'ID':1
#             },
#         UpdateExpression="set Command = :c",
#         ExpressionAttributeValues={
#             ':c': newMove
#         },
#         ReturnValues="UPDATED_NEW"
#     )
    
    #print(json.dumps(response, indent=4, cls=DecimalEncoder))    
    last_move = "";
    while(1):        
        response = table.scan()
        moveCommand = response['Items'][0]['Command']    
        if last_move != moveCommand:
            print moveCommand;
            last_move = moveCommand; 
        if moveCommand == "stop":
            break;
        
    #print response;
    
    
    #return moveCommand

get_move();
print "Stopped. Exiting."