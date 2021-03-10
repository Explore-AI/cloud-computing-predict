"""
    Function used to match words in a supplied list with those in a AWS Comprehend
    generated dictionary containing the key phrases. 
    
    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    The contents of this file should be added to a AWS  Lambda function 
    created as part of the EDSA Cloud-Computing Predict. 
    For further guidance around this process, see the README instruction 
    file which sits at the root of this repo.
    ---------------------------------------------------------------------
    
"""

# Function dependencies
import numpy as np

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
