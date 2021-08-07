# For lemmetization matching strings
from fuzzy_match import match
from fuzzy_match import algorithims

# Global list for roots in Ido 
rootwordlistA=[]
rootwordlistB,rootwordlistC,rootwordlistD,rootwordlistE,rootwordlistF=[],[],[],[],[]
rootwordlistG,rootwordlistH,rootwordlistI,rootwordlistJ,rootwordlistK,rootwordlistL=[],[],[],[],[],[]
rootwordlistM,rootwordlistN,rootwordlistO,rootwordlistP,rootwordlistQ,rootwordlistR=[],[],[],[],[],[]
rootwordlistS,rootwordlistT,rootwordlistU,rootwordlistV,rootwordlistW,rootwordlistX=[],[],[],[],[],[]
rootwordlistY,rootwordlistZ=[],[]

# Function which receives text file with Ido roots and minigs and create one list     
def receivefile(file_in,rootlist):    
    for line in file_in:
        rootword=line.split()[0]                
        mining=line.partition(' ')[2].rstrip()
        rootlist.append([rootword,mining]) 

# Function to call the file with the roots and mining in text format
def call_the_files():
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_A.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistA)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_B.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistB)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_C.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistC)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_D.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistD)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_E.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistE)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_F.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistF)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_G.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistG)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_H.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistH)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_I.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistI)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_J.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistJ)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_K.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistK)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_L.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistL)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_M.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistM)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_N.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistN)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_O.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistO)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_P.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistP)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_Q.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistQ)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_R.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistR)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_S.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistS)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_T.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistT)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_U.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistU)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_V.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistV)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_W.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistW)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_X.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistX)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_Y.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistY)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Ido_dictionary/voc_Z.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistZ) 

# Function to create dictionaries for the words which have something 
# in common   
def add_or_append(dictionary,key,value):
    if key not in dictionary:
        dictionary[key] = []
        dictionary[key].append(value) 
    else:
        if value not in dictionary[key]:
            dictionary[key].append(value) 

# Find the most apropriate root from the particular word in the text
def find_theroot(word_in_text,rootlist,dictionary_of_roots):
    max_ratio=0
    for sublist in rootlist:
        # take the arguments roots=["word","mining of word"]
        wordroot=sublist[0]
        mining=sublist[1]
        Ratio =algorithims.trigram(word_in_text,wordroot)       
        if Ratio > max_ratio:            
            max_ratio=Ratio
            toproot=wordroot
            Themining=mining
    # Every time we find the root and the mining we append it to 
    # the Dictionary with words and roots 
    add_or_append(dictionary_of_roots,word_in_text,toproot)
    add_or_append(dictionary_of_roots,word_in_text,Themining)        
    add_or_append(dictionary_of_roots,word_in_text,max_ratio)

    return dictionary_of_roots  

# For every word in the text we check the first letter of the word
# then in the find_theroot function we search in the appropiate list of roots
# to find the right root for the word. We are  stemming the words in the text 
def receive_tokentext_ido(token):
    dictionary_of_roots_ido={}
    # After we receive the token text in Ido language 
    # We create the lists with the roots for each letter of alphabet 
    call_the_files() 
    # Then for every word in text we chech the first letter to find its root in the correct list
    for wordtok in token:
        word=wordtok.lower()
        if word[0]=="a":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistA,dictionary_of_roots_ido)
        elif word[0]=="b":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistB,dictionary_of_roots_ido)
        elif word[0]=="c":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistC,dictionary_of_roots_ido)
        elif word[0]=="d":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistD,dictionary_of_roots_ido)
        elif word[0]=="e":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistE,dictionary_of_roots_ido)
        elif word[0]=="f":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistF,dictionary_of_roots_ido)
        elif word[0]=="g":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistG,dictionary_of_roots_ido)
        elif word[0]=="h":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistH,dictionary_of_roots_ido)
        elif word[0]=="i":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistI,dictionary_of_roots_ido)
        elif word[0]=="j":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistJ,dictionary_of_roots_ido)
        elif word[0]=="k":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistK,dictionary_of_roots_ido)
        elif word[0]=="l":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistL,dictionary_of_roots_ido)
        elif word[0]=="m":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistM,dictionary_of_roots_ido)
        elif word[0]=="n":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistN,dictionary_of_roots_ido)
        elif word[0]=="o":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistO,dictionary_of_roots_ido)
        elif word[0]=="p":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistP,dictionary_of_roots_ido)
        elif word[0]=="q":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistQ,dictionary_of_roots_ido)
        elif word[0]=="r":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistR,dictionary_of_roots_ido)
        elif word[0]=="s":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistS,dictionary_of_roots_ido)
        elif word[0]=="t":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistT,dictionary_of_roots_ido)
        elif word[0]=="u":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistU,dictionary_of_roots_ido)
        elif word[0]=="v":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistV,dictionary_of_roots_ido)
        elif word[0]=="w":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistW,dictionary_of_roots_ido)
        elif word[0]=="x":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistX,dictionary_of_roots_ido)
        elif word[0]=="y":
            dictionary_of_roots_ido=find_theroot(word,rootwordlistY,dictionary_of_roots_ido)
        else :
            if  word[0]=="z":
                dictionary_of_roots_ido=find_theroot(word,rootwordlistZ,dictionary_of_roots_ido)        

    return dictionary_of_roots_ido


 
        
