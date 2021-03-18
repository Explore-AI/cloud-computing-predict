"""
    Function used to construct an intelligent response to a given input message. 
    
    
    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    The contents of this file should be added to a AWS  Lambda function 
    created as part of the EDSA Cloud-Computing Predict. 
    For further guidance around this process, see the README instruction 
    file which sits at the root of this repo.
    ---------------------------------------------------------------------
    
    Description: This function uses the `find_max_sentiment` and `key_phrase_finder` 
        functions to firstly extract the overwhelming sentiment of a message reported 
        by AWS Comprehend, and secondly see if the key phrases determined by the service 
        match with a supplied list of user phrases. Given the sentiment and the boolean
        output of the `key_phrase_finder` function, we can then use conditional logic 
        to craft an intelligent response.

"""

def email_response(name, critical_phrase_list, list_of_extracted_phrases, AWS_Comprehend_Sentiment_Dump):

    # Function Constants
    SENDER_NAME = 'Place your name here'
    
    # --- Check for the sentiment of the message and find dominant sentiment score ---
    Sentiment_finder = find_max_sentiment(AWS_Comprehend_Sentiment_Dump)
    overwhelming_sentiment = Sentiment_finder[0]
    overwhelming_sentiment_score = Sentiment_finder[1]
    
    # --- Check for article critical phrases ---
    Phrase_Matcher_Article = key_phrase_finder(critical_phrase_list,  list_of_extracted_phrases)
    Matched_Phrases_Article = Phrase_Matcher_Article[0]
    Matched_Phrases_Checker_Article = Phrase_Matcher_Article[1]
    
    # --- Check for project phrases ---
    Phrase_Matcher_Project = key_phrase_finder(['github', 'git', 'Git', 
                                                'GitHub', 'projects', 
                                                'portfolio', 'Portfolio'],  
                                                list_of_extracted_phrases)
    Matched_Phrases_Project = Phrase_Matcher_Project[0]
    Matched_Phrases_Checker_Project = Phrase_Matcher_Project[1]
    
    # --- Check for C.V phrases ---
    Phrase_Matcher_CV = key_phrase_finder(['C.V', 'resume', 'Curriculum Vitae',
                                           'Resume', 'CV'],  
                                           list_of_extracted_phrases)
    Matched_Phrases_CV = Phrase_Matcher_CV[0]
    Matched_Phrases_Checker_CV = Phrase_Matcher_CV[1]
    
    # --- Generate standard responses ---
    # === DO NOT MODIFY THIS TEXT FOR THE PURPOSE OF PREDICT ASSESSMENT ===
    Greetings_text = f'Good day {name},'

    CV_text = 'I see that you mentioned my C.V in your message. \
               I am happy to forward you my C.V in response. \
               If you have any other questions or C.V related queries please do get in touch. '

    Project_Text = 'The projects I listed on my site only include \
                    the ones not running in production. I have \
                    several other projects that might interest you.'
    
    Article_Text = 'In your message you mentioned my blog posts and data science articles. \
                   I have several other articles published in academic journals. \
                   Please do let me know if you are interested - I am happy to forward them to you'
  
    Negative_Text = f'I see that you are unhappy in your response. \
                    Can we please set up a session to discuss why you are not happy, \
                    be it with the website, my personal projects or anything else. \
                    \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
 
    Neutral_Text = f'Thank you for your email. Let me know if you need any additional information.\
                    \n\nKind Regards, \n\n{SENDER_NAME}'
    
    Farewell_Text = f'Thank you for your email.\n\nIf there is anything else I can assist \
                     you with please let me know and I will set up a meeting for us to meet\
                     in person.\n\nKind Regards, \n\n{SENDER_NAME}'
    # =====================================================================
    
    # --- Email Logic --- 
    if overwhelming_sentiment == 'POSITIVE':
        if  ((Matched_Phrases_Checker_CV == True) & \
            (Matched_Phrases_Checker_Article == True) & \
            (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Article_Text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, CV_text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == True) & \
             (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)       
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == False)):

            mytuple = (Greetings_text, Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, Project_Text ,Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif  ((Matched_Phrases_Checker_CV == True) & \
              (Matched_Phrases_Checker_Article == True) & \
              (Matched_Phrases_Checker_Project == False)):
            
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
