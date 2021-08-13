from pos_esperanto_library import *

def check_in_lists(w):
    if w in articles_espe:
        return False
    elif w in possessive_pronouns_espe:
        return False
    elif w in possessive_pronouns_espe:
        return False
    elif w in objective_pronouns_espe:
        return False        
    elif w in suffixes_espe:
        return False
    elif w in prefixes_espe:
        return False
    elif w in prepositions_espe:
        return False
    elif w in conjuctions_espe:
        return False 
    elif w in personal_pronouns_espe:
        return False 
    elif w in compatives_superlatives_espe:
        return False
    elif w in compound_words_espe:
        return False
    elif w in numbers_espe:
        return False
    elif w in verbs_espe:
        return False 
    elif w in nouns_espe:
        return False
    elif w in adverbs_espe:
        return False 
    elif w in adjectives_espe:
        return False        
    else:
        return True  

def pos_espe_analyzer(token_text):
    pos_espe={"articles":[],"prepositions":[],"personal_pronouns":[],"possessive_pronouns":[],
    "objective_pronouns":[],"compatives_superlatives":[],"compound_words":[],"numbers":[],"conjuctions":[],
    "prefixes":[],"suffixes":[],"nouns":[],"adjectives":[],"adverbs":[],"verbs":[]} 
    
    for word in token_text:
        w=word.lower()
        # Chech the pos which are before the word
        if w in articles_espe:
            if w not in pos_espe["articles"]:
                pos_espe["articles"].append(w)        
        elif w in prepositions_espe:
            if w not in pos_espe["prepositions"]:
                pos_espe["prepositions"].append(w)
        elif w in personal_pronouns_espe:
            if w not in pos_espe["personal_pronouns"]:
                pos_espe["personal_pronouns"].append(w) 
        elif w in possessive_pronouns_espe:
            if w not in pos_espe["possessive_pronouns"]:
                pos_espe["possessive_pronouns"].append(w) 
        elif w in objective_pronouns_espe:
            if w not in pos_espe["objective_pronouns"]:
                pos_espe["objective_pronouns"].append(w)
        elif w in compatives_superlatives_espe:
            if w not in pos_espe["compatives_superlatives"]:
                pos_espe["compatives_superlatives"].append(w) 
        elif w in compound_words_espe:
            if w not in pos_espe["compound_words"]:
                pos_espe["compound_words"].append(w) 
        elif w in numbers_espe:
            if w not in pos_espe["numbers"]:
                pos_espe["numbers"].append(w) 
        elif w in conjuctions_espe:
           if w not in pos_espe["conjuctions"]:
                pos_espe["conjuctions"].append(w)            
        # Check the words which starts with a phrase like bellow        
        if len(w)>4:
            for checkword in prefixes_espe:
                if w.startswith(checkword):
                    if w not in pos_espe["prefixes"]:
                        pos_espe["prefixes"].append(w)
        # Check the words in suffixes which are in the end of the word
        if len(w)>4:
            for checkword in suffixes_espe:
                if checkword in w[-4:]:
                    if w not in pos_espe["suffixes"]:
                        pos_espe["suffixes"].append(w)        
        if len(w)>4:
            for checkword in nouns_espe:
                if w.endswith(checkword):
                    if w not in pos_espe["nouns"]:
                        pos_espe["nouns"].append(w)
        if len(w)>4:
            for checkword in verbs_espe:
                if w.endswith(checkword):
                    if w not in pos_espe["verbs"]:
                        pos_espe["verbs"].append(w)                    
        if len(w)>4:
            for checkword in adjectives_espe:
                if w.endswith(checkword):
                    if w not in pos_espe["adjectives"]:
                        pos_espe["adjectives"].append(w)
        # Check for adverbs . Words ending with -e
        if w[-1]=="e":
            if check_in_lists(w):
                if w not in pos_espe["adverbs"]:
                    pos_espe["adverbs"].append(w)                 
    return pos_espe    
