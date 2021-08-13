from pos_ido_library import *

def check_in_lists(w):
    if w in articles_ido:
        return False
    elif w in possessive_pronouns_ido:
        return False
    elif w in local_pronouns_ido:
        return False
    elif w in suffixes_ido:
        return False
    elif w in prefixes_ido:
        return False
    elif w in adverbs_phrase_ido:
        return False
    elif w in prepositions_ido:
        return False
    elif w in conjuctions_ido:
        return False 
    elif w in personal_pronouns_ido:
        return False 
    elif w in compatives_superlatives_ido:
        return False
    elif w in compound_words_ido:
        return False
    elif w in numbers_ido:
        return False
    elif w in verbs_ido:
        return False 
    else:
        return True  

def pos_ido_analyzer(token_text):
    pos_ido={"articles":[],"prepositions":[],"personal_pronouns":[],"possessive_pronouns":[],
    "local_pronouns":[],"compatives_superlatives":[],"compound_words":[],"numbers":[],
    "adverbs_phrase":[],"prefixes":[],"suffixes":[],"nouns":[],
    "adjectives":[],"adverbs":[],"verbs":[],"conjuctions":[]} 
    
    for word in token_text:
        w=word.lower()
        # Chech the pos which are before the word
        if w in articles_ido:
            if w not in pos_ido["articles"]:
                pos_ido["articles"].append(w)        
        elif w in prepositions_ido:
            if w not in pos_ido["prepositions"]:
                pos_ido["prepositions"].append(w)
        elif w in personal_pronouns_ido:
            if w not in pos_ido["personal_pronouns"]:
                pos_ido["personal_pronouns"].append(w) 
        elif w in possessive_pronouns_ido:
            if w not in pos_ido["possessive_pronouns"]:
                pos_ido["possessive_pronouns"].append(w) 
        elif w in local_pronouns_ido:
            if w not in pos_ido["local_pronouns"]:
                pos_ido["local_pronouns"].append(w)
        elif w in compatives_superlatives_ido:
            if w not in pos_ido["compatives_superlatives"]:
                pos_ido["compatives_superlatives"].append(w) 
        elif w in compound_words_ido:
            if w not in pos_ido["compound_words"]:
                pos_ido["compound_words"].append(w) 
        elif w in numbers_ido:
            if w not in pos_ido["numbers"]:
                pos_ido["numbers"].append(w) 
        elif w in adverbs_phrase_ido:
                if w not in pos_ido["adverbs_phrase"]:
                    pos_ido["adverbs_phrase"].append(w)
        elif w in conjuctions_ido:
                if w not in pos_ido["conjuctions"]:
                    pos_ido["conjuctions"].append(w)            
        # Check the words which starts with a phrase like bellow        
        for checkword in prefixes_ido:
            if w.startswith(checkword):
                if w not in pos_ido["prefixes"]:
                    pos_ido["prefixes"].append(w)
        # Check the words whick ends with a phrase like bellow 
        for checkword in suffixes_ido:
            if w.endswith(checkword):
                if w not in pos_ido["suffixes"]:
                    pos_ido["suffixes"].append(w)        
        for checkword in nouns_ido:
            if w.endswith(checkword):
                if w not in pos_ido["nouns"]:
                    pos_ido["nouns"].append(w)
        for checkword in verbs_ido:
            if w.endswith(checkword):
                if w not in pos_ido["verbs"]:
                    pos_ido["verbs"].append(w)                    
        # Check for adjectives . Words ending with -a
        if w[-1]=="a":
            if check_in_lists(w):
                if w not in pos_ido["adjectives"]:
                    pos_ido["adjectives"].append(w) 
        # Check for adverbs . Words ending with -e
        if w[-1]=="e":
            if check_in_lists(w):
                if w not in pos_ido["adverbs"]:
                    pos_ido["adverbs"].append(w)                 
        # Check for nouns . Words ending with -o or -i
        if (w[-1]=="i"):        
            if check_in_lists(w):
                if w not in pos_ido["nouns"]:
                    pos_ido["nouns"].append(w)                                          
        if (w[-1]=="o"):
            if check_in_lists(w):
                if w not in pos_ido["nouns"]:
                    pos_ido["nouns"].append(w)

    return pos_ido    
