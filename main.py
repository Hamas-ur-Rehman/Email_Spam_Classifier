import time
import streamlit as st
#importing necessary libraries
import numpy as np 
import pandas as pd 
import re
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from joblib import load
loadmodel = load('spam_classifier_with_NLTK.joblib')

st.title("Email Spam Classifier 📨")
st.text("This project was created by Hamas ur Rehman")

def check_email_variable(data):
    '''This function is used to predict whether an email is spam or not using the email_spam classifier model.
        It only takes in one parameter by passing it into it :
        Body.
        Just simply pass in the body of the email and you will get a prediciton of whether email classifies as spam or not
    '''
    email_input = pd.DataFrame([data], columns=['Body'])
    no_link = [re.sub(r'http\S+', '', i) for i in email_input["Body"]]
    clean = [re.sub('[^a-zA-Z0-9 ]', '', i) for i in no_link]
    lower = [i.lower() for i in clean]
    tokens = [nltk.word_tokenize(w) for w in lower]
    lemma = WordNetLemmatizer()
    lemmatized = [[lemma.lemmatize(w) for w in text] for text in tokens]
    without_stopwords = [[w for w in text if w not in stopwords.words('english')] for text in lemmatized]
    vectorizer = CountVectorizer(max_features=20000)
    X = vectorizer.fit_transform([' '.join(text) for text in without_stopwords]).toarray()
    X = np.pad(X, ((0, 0), (0,  20000 - X.shape[1])))   
    if(loadmodel.predict(X) == 0):
        st.write("Email is not Spam") 
    else:
        st.write("Email is Spam !!!") 



with st.form(key='my_form'):
    with st.spinner(text='In progress'):
        time.sleep(3)
    email = st.text_input('Enter the email body: ')
    submit = st.form_submit_button('predict')


if submit:
    if email == "":
        st.write("Please enter the email body")
    else:
        check_email_variable(email)
    
else:
    st.write("Please enter an email body to predict")