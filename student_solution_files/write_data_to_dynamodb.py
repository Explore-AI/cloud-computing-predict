
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
import base64   # Needed to decode the incoming POST data

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    
    # --- Write to dynamodb ---
    
    # ** Create a variable that can take a random value between 1 and 1 000 000 000. 
    # This variable will be used as our key value i.e the ResponsesID and should be of type integer.
    # It is important to note that the ResponseID i.e. the rid variable, should take
    # on a unique value to prevent errors when writing to DynamoDB. **
    
    # --- Insert your code here ---
    rid = None # <--- Replace this value with your code.
    # -----------------------------
    
    # ** Instantiate the DynamoDB service with the help of the boto3 library **
    
    # --- Insert your code here ---
    dynamodb = None # <--- Replace this value with your code.
    # -----------------------------
    
    # Instantiate the table. Remember pass the name of the DynamoDB table created in step 4
    table = dynamodb.Table('# Insert the name of your generated DynamoDB table here')
    
    # ** Write the responses to the table using the put_item method. **

    # Complete the below code so that the appropriate 
    # incoming data is sent to the matching column in your DynamoDB table
    # --- Insert your code here ---
    db_response = table.put_item(Item={'ResponsesID': None, # <--- Insert the correct variable
                        'Name': None, # <--- Insert the correct variable
                        'Email': None, # <--- Insert the correct variable
                        'Cell': None, # <--- Insert the correct variable
                        'Message': None # <--- Insert the correct variable
    })
    # -----------------------------

    # ** Create a response object to inform the website 
    #    that the workflow executed successfully. **
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message'],
        'DB_response': db_response
        })
    }
    
    return lambda_response



