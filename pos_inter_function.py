from pos_inter_library import *

def check_in_lists(w):
    if w in articles_inter:
        return False
    elif w in possessive_pronouns_inter:
        return False
    elif w in reflexive_pronouns_inter:
        return False
    elif w in suffixes_inter:
        return False
    elif w in prefixes_inter:
        return False
    elif w in adverbs_inter:
        return False
    elif w in prepositions_inter:
        return False
    elif w in conjuctions_inter:
        return False 
    elif w in personal_pronouns_inter:
        return False 
    elif w in compatives_superlatives_inter:
        return False
    elif w in numbers_inter:
        return False
    elif w in verbs_inter:
        return False 
    else:
        return True  

def pos_inter_analyzer(token_text):
    pos_inter={"articles":[],"prepositions":[],"personal_pronouns":[],"possessive_pronouns":[],
    "reflexive_pronouns":[],"compatives_superlatives":[],"numbers":[],"conjuctions":[],"prefixes":[],"adverds_phrase":[],"suffixes":[],"nouns":[],
    "adverbs":[],"verbs":[]} 
    
    for word in token_text:
        w=word.lower()
        # Chech the pos which are before the word
        if w in articles_inter:
            if w not in pos_inter["articles"]:
                pos_inter["articles"].append(w)        
        elif w in prepositions_inter:
            if w not in pos_inter["prepositions"]:
                pos_inter["prepositions"].append(w)
        elif w in personal_pronouns_inter:
            if w not in pos_inter["personal_pronouns"]:
                pos_inter["personal_pronouns"].append(w) 
        elif w in possessive_pronouns_inter:
            if w not in pos_inter["possessive_pronouns"]:
                pos_inter["possessive_pronouns"].append(w) 
        elif w in reflexive_pronouns_inter:
            if w not in pos_inter["reflexive_pronouns"]:
                pos_inter["reflexive_pronouns"].append(w)
        elif w in compatives_superlatives_inter:
            if w not in pos_inter["compatives_superlatives"]:
                pos_inter["compatives_superlatives"].append(w) 
        elif w in numbers_inter:
            if w not in pos_inter["numbers"]:
                pos_inter["numbers"].append(w) 
        elif w in conjuctions_inter:
                if w not in pos_inter["conjuctions"]:
                    pos_inter["conjuctions"].append(w)            
        # Check the words which starts with a phrase like bellow        
        for checkword in prefixes_inter:
            if w.startswith(checkword):
                if w not in pos_inter["prefixes"]:
                    pos_inter["prefixes"].append(w)
        # Check the words whick ends with a phrase like bellow 
        for checkword in suffixes_inter:
            if w.endswith(checkword):
                if w not in pos_inter["suffixes"]:
                    pos_inter["suffixes"].append(w)        
        for checkword in nouns_inter:
            if w.endswith(checkword):
                if w not in pos_inter["nouns"]:
                    pos_inter["nouns"].append(w)
        for checkword in verbs_inter:
            if w.endswith(checkword):
                if w not in pos_inter["verbs"]:
                    pos_inter["verbs"].append(w)  
        for checkword in adverbs_inter:
            if w.endswith(checkword):
                if w not in pos_inter["adverbs"]:
                    pos_inter["adverbs"].append(w)  
        for checkword in nouns_inter:
            if w.endswith(checkword):
                if w not in pos_inter["nouns"]:
                    pos_inter["nouns"].append(w)                                      
    return pos_inter    
