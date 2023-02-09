import streamlit as st
import PyPDF2
from gtts import gTTS
from googletrans import Translator
import re
#import easygui
import os
from io import StringIO
#import pandas as pd
#import codecs

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "9 °C", "1 °C")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.title("PDF to Audio Converter")

#pdf_file = st.file_uploader("Select a PDF file:")

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True, type=[".pdf",])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    #st.write(bytes_data)
    
pdffile = PyPDF2.PdfFileReader(uploaded_file)
no_of_pages = pdffile.getNumPages()

string_words = ''
for pages in range(no_of_pages):
    pi = pdffile.getPage(pages)
    page = pdffile.getPage(pages)
    content = page.extractText()
    textonly = re.findall(r'[a-zA-Z0-9]+', content)
    #for word in textonly:
        #string_words = string_words + '' + word
        
    string_words =  " ".join(textonly)
    print(string_words)

from googletrans import LANGUAGES
 # Get the list of language names
language_names = [LANGUAGES[code] for code in LANGUAGES]
 
 # Add a dropdown menu to select the language
language = st.selectbox("Select a language:", language_names)
 
 # Get the language code for the selected language
language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(language)]

translator = Translator()
translator.detect(string_words)
result = translator.translate(string_words, dest=language)
clicked = st.button("Translate", result)
audio = gTTS(text=result.text, lang=language)
 
st.audio(audio)

