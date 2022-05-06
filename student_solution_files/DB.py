
"""
    Lambda function that decodes and writes data from your portfolio website to your DynamoDB database.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    The contents of this file should be added to a AWS  Lambda function 
    created as part of the EDSA Cloud-Computing Predict. 
    For further guidance around this process, see the README instruction 
    file which sits at the root of this repo.
    ---------------------------------------------------------------------

"""

# Lambda dependencies
import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST
import random
import uuid
from botocore.exceptions import ClientError

#CREATE_RAW_PATH = "/contactme"

def lambda_handler(event, context):
    if event["rawPath"]== "/contactme":
        # Perform JSON data decoding 
        body_enc = json.loads(event['body'])
        body_enc = event['body']
        dec_dict = json.loads(base64.b64decode(body_enc))
    
    table.put_item(Item={'ResponsesID': rid, # <--- Insert the correct variable
                        'Name': dec_dict['name'], # <--- Insert the correct variable
                        'Email': dec_dict['email'], # <--- Insert the correct variable
                        'Cell': dec_dict['phone'], # <--- Insert the correct variable
                        'Message': dec_dict['message'] # <--- Insert the correct variable
    })
    
    # --- Write to dynamodb ---
    
    # ** Create a variable that can take a random value between 1 and 1 000 000 000. 
    # This variable will be used as our key value i.e the ResponsesID and should be of type integer.
    # It is important to note that the ResponseID i.e. the rid variable, should take
    # on a unique value to prevent errors when writing to DynamoDB. **
    
    # --- Insert your code here ---
    rid =random.randint(1,1000000)
   # rid = None # <--- Replace this value with your code.
    # -----------------------------
    
    # ** Instantiate the DynamoDB service with the help of the boto3 library **
    
    # --- Insert your code here ---
    dynamodb = boto3.resource('dynamodb')#,region_name='eu-west-1') # <--- Replace this value with your code.
    # -----------------------------
    
    # Instantiate the table. Remember pass the name of the DynamoDB table created in step 4
    table = dynamodb.Table('PredictDB')
    
    # ** Write the responses to the table using the put_item method. **

    # Complete the below code so that the appropriate 
    # incoming data is sent to the matching column in your DynamoDB table
    # --- Insert your code here ---
    """db_response = table.put_item(Item={'ResponsesID': rid, # <--- Insert the correct variable
                        'Name': dec_dict['name'], # <--- Insert the correct variable
                        'Email': dec_dict['email'], # <--- Insert the correct variable
                        'Cell': dec_dict['phone'], # <--- Insert the correct variable
                        'Message': dec_dict['message'] # <--- Insert the correct variable
    })
    # -----------------------------
    """
    #email_text = 'Hello world'

    # ** SES Functionality **

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    # --- Insert your code here ---
    """"SENDER = 'ntseleta@gmail.com'
    ses.send_mail(
        Source='ntseleta@gmail.com',
        Destination={
            'ToAddresses': [
                'ntselet@hotmail.com',
            ]
        },
        Message={
            'Subject': {
                'Data': 'Predict',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': email_text,
                    'Charset': 'UTF-8'
                },

            }
        },
    )
    # -----------------------------

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    # --- Insert your code here ---
    RECIPIENT = 'ntseleta@gmail.com'
    # -----------------------------

    # The subject line for the email.
    # --- DO NOT MODIFY THIS CODE ---
    SUBJECT = f"Data Science Portfolio Project Website - Hello {dec_dict['name']}"
    # -------------------------------

    # The email body for recipients with non-HTML email clients
    BODY_TEXT = (email_text)

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES service resource
    client = boto3.client('ses')

    # Try to send the email.
    try:
        # Provide the contents of the email.
        ses_response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                    # 'edsa.predicts@explore-ai.net', # <--- Uncomment this line once you have successfully tested your predict end-to-end
                ],
            },
            Message={
                'Body': {

                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )

    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(ses_response['MessageId'])


    # ** Create a response object to inform the website 
    #    that the workflow executed successfully. **
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
        'Name': dec_dict['Name'],
        'Email': dec_dict['Email'],
        'Cell': dec_dict['Phone_number'], 
        'Message': dec_dict['Message'],
        'DB_response': db_response
        })
    }"""
    
    return lambda_response



