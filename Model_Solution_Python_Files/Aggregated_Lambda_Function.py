"""
    Complete AWS Lambda script for the Cloud-Computing Predict.  
    
    Contains the full logic and AWS service integration required to 
    compose an intelligent response within the project workflow.

    Author: Explore Data Science Academy.

    Description: The contents of this file should be added to a AWS 
                 Lambda function created as part of the EDSA 
                 Cloud-Computing Predict. For further guidance around 
                 this process, see the README instruction file which
                 sits at the root of this repo.
"""

# Script dependencies 
import boto3   # Python AWS SDK
import json    # Used for handling API-based data.
import base64  # Needed to decode the incoming POST data
from random import randint  # Create response id
from botocore.exceptions import ClientError # Catch errors on client side
import pandas as pd # Create Dataframe
import numpy as np # Array manipulation

# Find dominating sentiment in article
def find_max_sentiment(Comprehend_Sentiment_Output):
    
    sentiment_score = 0

    if Comprehend_Sentiment_Output['Sentiment'] == 'POSITIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Positive']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEGATIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Negative']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEUTRAL':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Neutral']

    else:
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Mixed']

    print(sentiment_score, Comprehend_Sentiment_Output['Sentiment'])
    return Comprehend_Sentiment_Output['Sentiment'], sentiment_score

# Create function to return True if certain keyphrase is in text Method 2
def key_phrase_finder(list_of_important_phrases, list_of_extracted_phrases):

    listing = []
    PhraseChecker = None

    res = str(list_of_extracted_phrases).split()

    for important_word in list_of_important_phrases:

        names = res
        names2 = [word for word in names if important_word in word]
        isnot_empty = np.array(names2).size > 0
        
        if isnot_empty == True:
            listing = np.append(listing, names2)
            
        else:
            listing = listing
            
    if np.array(listing).size > 0:
        PhraseChecker = True
        
    else:
        PhraseChecker = False
    
    return listing, PhraseChecker

    
# Function that writes emails based on key phrases
def email_response(name, email_address, critical_phrase_list, sentiment_list, sentiment_scores, list_of_extracted_phrases, AWS_Comprehend_Sentiment_Dump):
    
    # Check for sentiment of message and find dominant sentiment score
    Sentiment_finder = find_max_sentiment(AWS_Comprehend_Sentiment_Dump)
    overwhelming_sentiment = Sentiment_finder[0]
    overwhelming_sentiment_score = Sentiment_finder[1]
    
    # Check for article critical phrases
    Phrase_Matcher_Article = key_phrase_finder(critical_phrase_list,  list_of_extracted_phrases)
    Matched_Phrases_Article = Phrase_Matcher_Article[0]
    Matched_Phrases_Checker_Article = Phrase_Matcher_Article[1]
    
    # Check for project phrases
    Phrase_Matcher_Project = key_phrase_finder(['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio'],  list_of_extracted_phrases)
    Matched_Phrases_Project = Phrase_Matcher_Project[0]
    Matched_Phrases_Checker_Project = Phrase_Matcher_Project[1]
    
    # Check for C.V phrases
    Phrase_Matcher_CV = key_phrase_finder(['C.V', 'resume', 'Curriculum Vitae', 'Resume', 'CV'],  list_of_extracted_phrases)
    Matched_Phrases_CV = Phrase_Matcher_CV[0]
    Matched_Phrases_Checker_CV = Phrase_Matcher_CV[1]
    
    # Generate standard responses
    Greetings_text = f'Good day {name},'

    CV_text = 'I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. '
 
    Project_Text = 'The projects I listed on my site only include the ones not running in production. I have several other projects that might interest you.'
    
    Article_Text = 'In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you'
  
    Negative_Text = 'I see that you are unhappy in your response. Can we please set up a session to discuss why you are not happy, be it with the website, my personal projects or anything else. \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
 
    Neutral_Text = 'Thank you for your email. Let me know if you need any additional information.\n\nKind Regards, \n\nMyName'
    
    Farewell_Text = 'Thank you for your email.\n\nIf there is anyting else I can assist you with please let me know and I will set up a meeting for us to meet in person.\n\nKind Regards, \n\nMyName'
    
    # Email Logic
    # Positive Response
    if overwhelming_sentiment == 'POSITIVE':
        if  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, CV_text, Article_Text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, CV_text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, CV_text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)       
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, Project_Text ,Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, CV_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        else:
            mytuple = (Greetings_text, Project_Text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
    elif overwhelming_sentiment == 'NEGATIVE':
            mytuple = (Greetings_text, Negative_Text)
            Text = "\n \n".join(mytuple)
            
    else:
            mytuple = (Greetings_text, Neutral_Text)   
            Text = "\n \n".join(mytuple)
    
    return Text
    

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    df = {
        'statusCode': 200,
        'body': json.dumps(f"Name: {dec_dict['name']}, Email: {dec_dict['email']}, Cell: {dec_dict['phone']}, Message: {dec_dict['message']}")
    }
    
    # Write to dynamodb
    rid = randint(1, 1000000000)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Email-Responses')
    response = table.put_item(Item={'ResponsesID':rid,
                                    'Name':dec_dict['name'],
                                    'Email':dec_dict['email'] ,
                                    'Cell':dec_dict['phone'] ,
                                    'Message':dec_dict['message']
    })
    
    # Amazon Comprehend
    comprehend = boto3.client(service_name='comprehend')
    text = dec_dict['message']
    Sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    KeyPhrases = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
    
    # Get list of phrases in numpy array
    phrase = []
    for i in range(0, len(KeyPhrases['KeyPhrases'])-1):
        phrase = np.append(phrase, KeyPhrases['KeyPhrases'][i]['Text'])
        
    Text = email_response(name = dec_dict['name'], 
                          email_address = dec_dict['email'], 
                          critical_phrase_list = ['Medium', 'article', 'publish', 'Towards Data Science', 'blog'], 
                          sentiment_list =  ['Positive', 'Negative', 'Neutral', 'Mixed'], 
                          sentiment_scores = Sentiment['SentimentScore'],
                          list_of_extracted_phrases = phrase,
                          AWS_Comprehend_Sentiment_Dump = Sentiment)
        
    email_reply =   f'{Text}' 
    
    # SES Functionality
    # Replace student@explore-ai.netwith your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = 'student@explore-ai.net'
    
    # Use the form data to populate the recipient address. 
    # Note that If your account is still in the sandbox, 
    # the recipient address must be verified.
    RECIPIENT =  f"{dec_dict['email']}" 
    
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    #AWS_REGION = "us-west-1"
    
    # The subject line for the email.
    SUBJECT = "Data Science Portfolio Project Website"
    
    # The email body for recipients with non-HTML email clients
    BODY_TEXT = (email_reply)

    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Create a new SES resource and specify a region.
    # client = boto3.client('ses',region_name=AWS_REGION)
    client = boto3.client('ses')
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
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
        print(response['MessageId'])
        
        
    
    return df, email_reply
    
    
    




