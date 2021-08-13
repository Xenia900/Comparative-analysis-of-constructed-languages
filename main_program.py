#!/usr/bin/env python
# coding: utf-8

from ido_vocabulary_function import receive_tokentext_ido
# Calculate time to excecute the programe 
import time
# NLTK tool 
import nltk
from nltk.tokenize import word_tokenize
# Frequency  of words
from nltk.probability import FreqDist 
# Visualize the results
import matplotlib
matplotlib.use('TkAgg')
# Visualize list data
import matplotlib.pyplot as plt
# For entropy calculation
import math
# Visualise the dictionaries
import uuid
import tkinter as tk
from tkinter import ttk
# Visualize the pie chart of Pos (Parts of Speech)
import numpy as np
# For lemmetization matching strings
from fuzzy_match import match
from fuzzy_match import algorithims
# File with the most common roots of esperanto
from esperanto_roots import *

# Dictionary for letter frequency in Esperanto language
alphabet_espreranto = {'A': 0,'B': 0,'C': 0,'Ĉ': 0,'D': 0,'E': 0,'F': 0,
    'G': 0,'Ĝ': 0,'H': 0,'Ĥ': 0,'I': 0,'J': 0,'Ĵ': 0,'K': 0,'L': 0,
    'M': 0,'N': 0,'O': 0,'P': 0,'R': 0,'S': 0,'Ŝ': 0,'T': 0,'U': 0,'Ŭ': 0,'V': 0,'Z':0,'a':0,'b':0,'c':0,'ĉ':0,'d':0,'e':0,'f':0,'g':0,'ĝ':0,'h':0,'ĥ':0,'i':0,'j':0,'ĵ':0,
           'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'r':0,'s':0,'ŝ':0,'t':0,'u':0,'ŭ':0,'v':0,'z':0}
# Dictionary for letter frequency in Ido language           
alphabet_Ido={'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,
    'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,
    'Y':0,'Z':0,'a':0,'b':0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,
    'm': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y':0,'z':0} 
# Dictionary for letter frequency in Interlingua language           
alphabet_Inter={'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,
    'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,
    'Y':0,'Z':0,'a':0,'b':0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,
    'm': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y':0,'z':0}            
# Help list for lemmetization in Esperanto 
pro_list=[]
# Define punctuation
punctuations = '''+`«»’=0123456789!()--[]{};:'"“”\,<>./?@#$%^&*_—~'''

# Remove punctuation from the string
def punctuation(my_str):    
    no_punct = ""
    for char in my_str:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct

# Takes the file in string format and we tokenize it (word split)
def tokenization(string_file): 
    string_tokens=[]
    token_text=word_tokenize(string_file)
    print("\nThe are %d letters in the text:"%(len(string_file)))
    print('\nThere are %d words in the text'%(len(token_text)))
    return token_text

# Frequency of each letter in the alphabet_Ido
def alphabet_frequency(file,alphabet_dic):   
    # For each letter in the text ,check if is key in the esprenato alphabet 
    # dictionary, if so add 1 in this letter 
    for letter in file:            	
        if letter in alphabet_dic.keys():    
            alphabet_dic[letter] += 1    	
    # Divide each letter with the total number of letters         
    #for letter in alphabet_dic.keys():
    #    alphabet_dic[letter] = alphabet_dic[letter] / count                 

# Frequency of each word in the text   
def count_appearance_of_words(token_text):    
    fdist=FreqDist()    
    for word in token_text:
        fdist[word.lower()]+=1   
              
    di_count = nltk.FreqDist(token_text)
    del di_count['']
    # li_sorted its a sorted list of each word and its count appearance in the text    
    li_sorted = sorted(di_count.items(), key=lambda x: x[1], reverse=True)
    return li_sorted 

def lists_visual(dataX,dataY,namex,namey,title,number,comment):     
    name = dataY
    price = dataX
    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9)) 
    # Horizontal Bar Plot
    ax.barh(name, price) 
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False) 
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none') 
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10) 
    # Add x, y gridlines
    ax.grid(b = True, color ='grey',
    linestyle ='-.', linewidth = 0.5,
    alpha = 0.2) 
    # Show top values
    ax.invert_yaxis() 
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10, fontweight ='bold',color ='grey') 
    # Add Plot Title
    ax.set_title(title,loc ='left', ) 
    # Add Text watermark
    fig.text(0.9, 0.15,comment, fontsize = 12,color ='grey', ha ='right', va ='bottom',alpha = 0.7) 
    # Show Plot
    plt.show() 

# Visualise in pie chart            
def pie_visual(pos_part,data_slices):
    x=np.char.array(pos_part)
    y=np.array(data_slices)
    porcent=y
    patches, texts = plt.pie(y, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f}'.format(i,j) for i,j in zip(x, porcent)]
    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],reverse=True))
    plt.legend(patches, labels, loc='center', bbox_to_anchor=(-0.1, 1.),fontsize=8)
    plt.savefig('piechart.png', bbox_inches='tight')
    plt.show()  

# Calculate the frequency of each word in the text 
def computefreq(list_freq,token_text,nameoftext):
    freqlist=[]
    sublist=[]
    textcount=len(token_text)
    # We create three list with the data we need to visualize
    Y_Count=[]
    X_words=[]
    Y_freq=[]
    for tupleword in list_freq:
        word=tupleword[0]
        countword=tupleword[1]
        Y_Count.append(countword)
        freqword=countword/float(textcount)
        # We want to store the value calculation
        freqlist.append([word,freqword])
        Y_freq.append(freqword)
        X_words.append(word)
    # Visualize the results top n=30 most common words
    n=30
    lists_visual(Y_Count[:n],X_words[:n],"Count the appearance of words","Words","Count-calculation",n,nameoftext)
    lists_visual(Y_freq[:n],X_words[:n],"Frequencies","Words","Frequency-calculation",n,nameoftext)       
    return freqlist 


# Calculates the Shannon entropy for the given string.
# Returns: Shannon entropy (min bits per byte-character).
def calculate_shannon_entropy(string):    
    ent = 0.0
    if len(string) < 2:
        return ent
    size = float(len(string))
    # Calculate the frequency of every symbol in ascii total 128
    for b in range(128):
        freq = string.count(chr(b))
        if freq > 0:
            # After we count the number of each ascii character in the text,
            # we devide with the total amount, size of charactes in the whole text
            # so we can find the frequency of each ascii character 
            freq = float(freq) / size
            # We calculate the entropy by character 
            ent = ent + freq * math.log(freq, 2)                   
    return -ent     

# Functions for lemmetization
def commonfirstletter_list(word):
    for sublist in roots:
        # take the first argument roots=["word","mining of word"]
        root_word=sublist[0]   
        if root_word[0].lower()==word[0].lower():
            pro_list.append(sublist)
    return pro_list  

def lemmetize_Esperanto(token_text):
    dictionary_of_roots={}

    for word in token_text:
        word_in_text=word.lower()     
        pro_list=commonfirstletter_list(word_in_text)
        max_ratio=0
        for sublist in pro_list:
            wordroot=sublist[0].lower()
            mining=sublist[1].lower()
            Ratio =algorithims.trigram(word_in_text,wordroot)       
            if Ratio > max_ratio:
                max_ratio=Ratio
                toproot=wordroot
                Themining=mining
        if Ratio>0.4:
            # Dictionary with words and roots
            add_or_append(dictionary_of_roots,word_in_text,toproot)
            add_or_append(dictionary_of_roots,word_in_text,Themining)        
            add_or_append(dictionary_of_roots,word_in_text,max_ratio)                      
        pro_list.clear() 
    return dictionary_of_roots

# Function to create dictionaries for the words which have something 
# in common   
def add_or_append(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
        dictionary[key].append(value) 
    else:
        if value not in dictionary[key]:
            dictionary[key].append(value)            

# Function which create a dictionary key : Part of speech
# value : words of text which are this parts of speech
def procces_pos(pos):
    dic_pos={}
    poskeys=[]
    pos_sum=[]
    for sublist in pos:
        add_or_append(dic_pos,sublist[1],sublist[0])         
    for key, value in dic_pos.items():  
        poskeys.append(key)
        pos_sum.append(len([item for item in value if item])) 
    pie_visual(poskeys,pos_sum)      
    for key, value in dic_pos.items():
        final_new= list(set(value))
        dic_pos[key]=final_new      
    return dic_pos   

# Function for visualise the dictionary of POS   
def j_tree(tree, parent, dic):
    for key in sorted(dic.keys()):
        uid = uuid.uuid4()
        if isinstance(dic[key], dict):
            tree.insert(parent, 'end', uid, text=key)
            j_tree(tree, uid, dic[key])
        elif isinstance(dic[key], tuple):
            tree.insert(parent, 'end', uid, text=str(key) + '()')
            j_tree(tree, uid,
                   dict([(i, x) for i, x in enumerate(dic[key])]))
        elif isinstance(dic[key], list):
            tree.insert(parent, 'end', uid, text=str(key) + '[]')
            j_tree(tree, uid,
                   dict([(i, x) for i, x in enumerate(dic[key])]))
        else:
            value = dic[key]
            if isinstance(value, str):
                value = value.replace(' ', '_')
            tree.insert(parent, 'end', uid, text=key, value=value)
            
def tk_tree_view(data):
    # Setup the root UI
    root = tk.Tk()
    root.title("tk_tree_view")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    # Setup the Frames
    tree_frame = ttk.Frame(root, padding="3")
    tree_frame.grid(row=0, column=0, sticky=tk.NSEW)
    # Setup the Tree
    tree = ttk.Treeview(tree_frame, columns=('Values'))
    tree.column('Values', width=100, anchor='center')
    tree.heading('Values', text='Values')
    j_tree(tree, '', data)
    tree.pack(fill=tk.BOTH, expand=1)
    # Limit windows minimum dimensions
    root.update_idletasks()
    root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())
    root.mainloop()  

# Function for remove stop word word such as articles,prepositions,pronoun
# and words with small length 
def remove_stopword(string_text):    
    new_string = ' '.join([w for w in string_text.split() if len(w)>4])
    return new_string               

# Function to call all the other functions 
def main_procces_Esperanto(my_st,name_document):

    # Frequency of each letter in the esperanto alphabet
    alphabet_frequency(my_st,alphabet_espreranto)    
    plt.bar(list(alphabet_espreranto.keys()), alphabet_espreranto.values(), color='g')
    plt.show()
    print(alphabet_espreranto)   

    # Remove punctuation from the string
    st=punctuation(my_st)

    # Takes the file in string format 
    # and we tokenize it (word split)
    token_file=tokenization(st)    

    # Count each word in the text
    list_freq=[]
    list_freq=count_appearance_of_words(token_file)
    
    # compute the frequency of each word in the text 
    # so we can understand how important the word is
    computefreq(list_freq,token_file,name_document)      

    # Function for calculate the Shannon entropy by character in the text  
    entropy=calculate_shannon_entropy(st) 
    print("entropy\n",entropy)

    # Find which part of speech is each word
    # File for this job
    from pos_esperanto_function import pos_espe_analyzer
    dic_pos_espe=pos_espe_analyzer(token_file) 
    tk_tree_view(dic_pos_espe)
    # Visualize the amount of POS in Ido 
    poskeys=[]
    pos_sum=[]
    for key, value in dic_pos_espe.items():
        poskeys.append(key)
        pos_sum.append(len([item for item in value if item])) 
    pie_visual(poskeys,pos_sum)
    
     # Function for lemmetization
    dictionaryroots=lemmetize_Esperanto(token_file)
    tk_tree_view(dictionaryroots)

    # Function for stopwords remove
    new_string_text=remove_stopword(st)
    # Takes the file in string format 
    # and we tokenize it (word split)
    new_token_file=tokenization(new_string_text) 
    # Count of each word in the text
    list_freq_new=[]
    list_freq_new=count_appearance_of_words(new_token_file)
    # compute the new values of frequencies
    computefreq(list_freq_new,new_token_file,name_document) 

def main_procces_Ido(my_st,name_document):
    
    # Frequency of each letter in the Ido alphabet
    alphabet_frequency(my_st,alphabet_Ido)
    plt.bar(list(alphabet_Ido.keys()), alphabet_Ido.values(), color='g')    
    plt.show()
    print(alphabet_Ido) 

    # Remove punctuation from the string
    st=punctuation(my_st)

    # Takes the file in string format 
    # and we tokenize it (word split)
    token_file=tokenization(st)
    #print(token_file)
    
    # Count appearance of each word in the text
    list_freq=[]
    list_freq=count_appearance_of_words(token_file)
    # Frequency of each word
    computefreq(list_freq,token_file,name_document) 
    
    # Function for stopwords remove
    new_string_text=remove_stopword(st)
    # Takes the file in string format 
    # and we tokenize it (word split)
    new_token_file=tokenization(new_string_text) 
    # Count appearance  of each word in the text
    list_freq_new=[]
    list_freq_new=count_appearance_of_words(new_token_file)
    # compute the new word frequencies 
    computefreq(list_freq_new,new_token_file,name_document)    
    
    # Function for calculate the Shannon entropy of the text  
    entropy=calculate_shannon_entropy(st) 
    print("entropy\n",entropy)
    
    # Find which part of speech is each word
    # File for this job
    from pos_ido_function import pos_ido_analyzer
    dic_pos_ido=pos_ido_analyzer(token_file) 
    tk_tree_view(dic_pos_ido)
    # Visualize the amount of POS in Ido 
    poskeys=[]
    pos_sum=[]
    for key, value in dic_pos_ido.items():
        poskeys.append(key)
        pos_sum.append(len([item for item in value if item])) 
    pie_visual(poskeys,pos_sum) 
    
    # Function for lemmetization
    dic_roots_ido={}
    from ido_vocabulary_function import receive_tokentext_ido
    dic_roots_ido=receive_tokentext_ido(token_file)  
    tk_tree_view(dic_roots_ido) 

def main_procces_Inter(my_st,name_document):
    
    # Frequency of each letter in the Ido alphabet
    alphabet_frequency(my_st,alphabet_Inter)
    plt.bar(list(alphabet_Inter.keys()), alphabet_Inter.values(), color='g')    
    plt.show()
    print(alphabet_Inter) 
    
    # Remove punctuation from the string
    st=punctuation(my_st)

    # Takes the file in string format 
    # and we tokenize it (word split)
    token_file=tokenization(st)
    #print(token_file)
    
    # Count word appearance
    list_freq=[]
    list_freq=count_appearance_of_words(token_file)
    # print(list_freq)
    
    # compute the  frequency of words
    computefreq(list_freq,token_file,name_document)  

    # Function for stopwords remove
    new_string_text=remove_stopword(st)
    # Takes the file in string format 
    # and we tokenize it (word split)
    new_token_file=tokenization(new_string_text) 
    # Count each word in the text
    list_freq_new=[]
    list_freq_new=count_appearance_of_words(new_token_file)
    # Compute word frequency
    computefreq(list_freq_new,new_token_file,name_document) 
    
    # Function for calculate the Shannon entropy of the text  
    entropy=calculate_shannon_entropy(st) 
    print("entropy\n",entropy)

    # Find which part of speech is each word
    # File for this job
    from pos_inter_function import pos_inter_analyzer
    dic_pos_inter=pos_inter_analyzer(token_file) 
    tk_tree_view(dic_pos_inter)
    # Visualize the amount of POS in Ido 
    poskeys=[]
    pos_sum=[]
    for key, value in dic_pos_inter.items():
        poskeys.append(key)
        pos_sum.append(len([item for item in value if item])) 
    pie_visual(poskeys,pos_sum) 
    
    # Function for lemmetization
    from visual_dic_inter import show_data
    dic_roots_inter={}
    from inter_vocabulary_function import receive_tokentext_inter   
    dic_roots_inter=receive_tokentext_inter(token_file) 
    for key,value in dic_roots_inter.items():
        print(key,value,"\n")
    show_data(dic_roots_inter) 
  
# Main programme for all languages

start_esp=time.time()
file_esperanto = open('C:/Users/XENIA/Desktop/DIPLO/Esperanto_Text/esperantobig1.txt','r',encoding="utf-8")
string_file_esperanto = file_esperanto.read().replace("\n", " ")
file_esperanto.close()
name_document="Second Esperanto document"
main_procces_Esperanto(string_file_esperanto,name_document)
end_esp=time.time()
print("Time to excecute the esperanto text",(end_esp-start_esp)/60.0)
'''
# Main programme for Ido language
start_Ido=time.time()
file_Ido = open('C:/Users/XENIA/Desktop/DIPLO/Ido_Text/idosmall.txt','r',encoding="utf-8")
string_file_Ido = file_Ido.read().replace("\n", " ")
file_Ido.close()
name_document="First Ido document"
main_procces_Ido(string_file_Ido,name_document)
end_Ido=time.time()
print("Time to excecute the Ido text",(end_Ido-start_Ido)/60.0)

# Main programme for Interligua language
start_Inter=time.time()
file_Inter = open('C:/Users/XENIA/Desktop/DIPLO/Interlingua_Text/interlinguatext5.txt','r',encoding="utf-8")
string_file_Inter = file_Inter.read().replace("\n", " ")
file_Inter.close()
name_document="First Interlingua document"
main_procces_Inter(string_file_Inter,name_document)
end_Inter=time.time()
print("Time to excecute the Intelingua text",(end_Inter-start_Inter)/60.0)
'''