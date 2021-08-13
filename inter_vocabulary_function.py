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

#punctuations = '\'+`«»’=0123456789!()--[]{;:"“”\,<>./?@#$%^&*_—~}'
punctuations = ';),'
# Remove punctuation from the string
def punctuation(my_str):    
    no_punct = ""
    for char in my_str:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct

def receivefile(file_in,rootlist): 

    file_in = file_in.read().splitlines()
         
    for line in file_in:
        # After we take thew first word, the root we want to clean it of possible 
        # useless characters. The same for the mining of the root, which is after thw first
        # word of each line in the text file
        rootword=line.split()[0] 
        rootword=punctuation(rootword) 
        mining=line.partition(' ')[2].rstrip()
        mining=punctuation(mining)

        rootlist.append([rootword,mining])  

'''
# Function which receives text file with Ido roots and minigs and create one list     
def receivefile(file_in,rootlist):    
    for line in file_in:
        # After we take thew first word, the root we want to clean it of possible 
        # useless characters. The same for the mining of the root, which is after thw first
        # word of each line in the text file
        rootword=line.split()[0] 
        rootword=punctuation(rootword) 

        mining=line.partition(' ')[2].rstrip()
        mining=punctuation(mining)

        rootlist.append([rootword,mining])     
'''  
# Function to call the file with the roots and mining in text format
def call_the_files():
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterA.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistA)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterB.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistB)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterC.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistC)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterD.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistD)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterE.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistE)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterF.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistF)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterG.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistG)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterH.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistH)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterI.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistI)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterJ.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistJ)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterK.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistK)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterL.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistL)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterM.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistM)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterN.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistN)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterO.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistO)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterP.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistP)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterQ.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistQ)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterR.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistR)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterS.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistS)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterT.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistT)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterU.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistU)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterV.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistV)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterW.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistW)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterX.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistX)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterY.txt','r',encoding="utf-8")
    receivefile(file_in,rootwordlistY)
    file_in=open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_dictionary/InterZ.txt','r',encoding="utf-8")
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
def receive_tokentext_inter(token):
    dictionary_of_roots_inter={}
    # After we receive the token text in Interlingua language 
    # We create me lists with the roots for each letter of alphabet 
    call_the_files()
    # Then for every word in text we chech the first letter to find its root in the correct list
    for wordtok in token:
        word=wordtok.lower()
        if word[0]=="a":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistA,dictionary_of_roots_inter)
        elif word[0]=="b":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistB,dictionary_of_roots_inter)
        elif word[0]=="c":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistC,dictionary_of_roots_inter)
        elif word[0]=="d":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistD,dictionary_of_roots_inter)
        elif word[0]=="e":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistE,dictionary_of_roots_inter)
        elif word[0]=="f":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistF,dictionary_of_roots_inter)
        elif word[0]=="g":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistG,dictionary_of_roots_inter)
        elif word[0]=="h":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistH,dictionary_of_roots_inter)
        elif word[0]=="i":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistI,dictionary_of_roots_inter)
        elif word[0]=="j":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistJ,dictionary_of_roots_inter)
        elif word[0]=="k":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistK,dictionary_of_roots_inter)
        elif word[0]=="l":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistL,dictionary_of_roots_inter)
        elif word[0]=="m":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistM,dictionary_of_roots_inter)
        elif word[0]=="n":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistN,dictionary_of_roots_inter)
        elif word[0]=="o":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistO,dictionary_of_roots_inter)
        elif word[0]=="p":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistP,dictionary_of_roots_inter)
        elif word[0]=="q":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistQ,dictionary_of_roots_inter)
        elif word[0]=="r":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistR,dictionary_of_roots_inter)
        elif word[0]=="s":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistS,dictionary_of_roots_inter)
        elif word[0]=="t":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistT,dictionary_of_roots_inter)
        elif word[0]=="u":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistU,dictionary_of_roots_inter)
        elif word[0]=="v":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistV,dictionary_of_roots_inter)
        elif word[0]=="w":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistW,dictionary_of_roots_inter)
        elif word[0]=="x":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistX,dictionary_of_roots_inter)
        elif word[0]=="y":
            dictionary_of_roots_inter=find_theroot(word,rootwordlistY,dictionary_of_roots_inter)
        else :
            if  word[0]=="z":
                dictionary_of_roots_inter=find_theroot(word,rootwordlistZ,dictionary_of_roots_inter)        

    return dictionary_of_roots_inter


 
        
