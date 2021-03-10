
"""
    Final AWS Lambda function skeleton. 
    
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
import numpy as np # Array manipulation
# <<< You will need to add additional libraries to complete this script >>> 

# ** Insert key phrases function **
# --- Insert your code here ---

# -----------------------------

# ** Insert sentiment extraction function **
# --- Insert your code here ---
 
# -----------------------------

# ** Insert email responses function **
# --- Insert your code here ---
 
# -----------------------------

# Lambda function orchestrating the entire predict logic
def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    

    # ** Insert code to write to dynamodb **
    # <<< Ensure that the DynamoDB write response object is saved 
    #    as the variable `db_response` >>> 
    # --- Insert your code here ---


    # Do not change the name of this variable
    db_response = None
    # -----------------------------
    

    # --- Amazon Comprehend ---
    comprehend = boto3.client(service_name='comprehend')
    
    # --- Insert your code here ---
    enquiry_text = None # <--- Insert code to place the website message into this variable
    # -----------------------------
    
    # --- Insert your code here ---
    sentiment = None # <---Insert code to get the sentiment with AWS comprehend
    # -----------------------------
    
    # --- Insert your code here ---
    key_phrases = None # <--- Insert code to get the key phrases with AWS comprehend
    # -----------------------------
    
    # Get list of phrases in numpy array
    phrase = []
    for i in range(0, len(key_phrases['KeyPhrases'])-1):
        phrase = np.append(phrase, key_phrases['KeyPhrases'][i]['Text'])


    # ** Use the `email_response` function to generate the text for your email response **
    # <<< Ensure that the response text is stored in the variable `email_text` >>> 
    # --- Insert your code here ---
    # Do not change the name of this variable
    email_text = None 

    
    # -----------------------------
            

    # ** SES Functionality **

    # Insert code to send an email, using AWS SES, with the above defined 
    # `email_text` variable as it's body.
    # <<< Ensure that the SES service response is stored in the variable `ses_response` >>> 
    # --- Insert your code here ---

    # Do not change the name of this variable
    ses_response = None
    
    # ...

    # Do not modify the email subject line
    SUBJECT = f"Data Science Portfolio Project Website - Hello {dec_dict['name']}"

    # -----------------------------


    # ** Create a response object to inform the website that the 
    #    workflow executed successfully. Note that this object is 
    #    used during predict marking and should not be modified.**
    # --- DO NOT MODIFY THIS CODE ---
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message'],
        'DB_response': db_response,
        'SES_response': ses_response,
        'Email_message': email_text
        })
    }
    # -----------------------------
    
    return lambda_response   
    




