import streamlit as st
import pickle
import nltk
from nltk import word_tokenize

# Step 1 : Build a tranformed_text function :

def text_preprocesing(text):
    
    # 1. Lowercase
    text = text.lower()
    
    # 2. Tokenizse
    text = nltk.word_tokenize(text)
    
    list = []   # since text is already tokenized and lowercase , below code will remove special chars and store into list
    
    # 3. Remove special words
    for i in text :
        if i.isalnum():
            list.append(i)
       
    text = list[:] # since list is filled with text with no special chars and lowez and tokz it will again clone to text
    list.clear()   # and it will be clear to append new tranformed text with no stopword and puncts
    
    
    # 4. stemming
    
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    
    for i in text:
        list.append(ps.stem(i))
    
    
    return " ".join(list)
    
            
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Tweet Intent Prediction")
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    
    # 1. preprocess
    transformed_sms = text_preprocesing(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 0:
        st.header("Appreciation")
    elif result == 1:
        st.header("Community")
    elif result == 2:
        st.header("Done")
    elif result == 3:
        st.header("Giveaway")
    elif result == 4:
        st.header("Interested ")
    elif result == 5:
        st.header("Launching Soon")
    elif result == 6:
        st.header("Presale")
    elif result == 7:
        st.header("Whitelist")
        