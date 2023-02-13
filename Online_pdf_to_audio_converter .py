import streamlit as st
import PyPDF2
from gtts import gTTS
from googletrans import Translator
import re
import os
from io import BytesIO

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "9 °C", "1 °C")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.title("PDF to Audio Converter")

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True, type=[".pdf",])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)

    pdf_file = BytesIO(bytes_data) # just to try
    pdffile = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = pdffile.getNumPages()# hey yo

    string_words = ''
    for pages in range(no_of_pages):
        pi = pdffile.getPage(pages)
        page = pdffile.getPage(pages)
        content = page.extractText()
        textonly = re.findall(r'[a-zA-Z0-9]+', content)
        string_words =  " ".join(textonly)
        
        print(string_words)

    from googletrans import LANGUAGES
    language_names =  {
        "Afrikaans": "af",
        "Albanian": "sq",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Portuguese": "pt",
        "Mandarin": "zh-CN"
    }
    language = st.selectbox("Select a language:", language_names)
    
    
    translator = Translator()
    translator.detect(string_words)
    result = translator.translate(string_words, dest=language)

    # Map full language name to language code
    lang_code_map = {
        "Afrikaans": "af",
        "Albanian": "sq",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Portuguese": "pt",
        "Mandarin": "zh-CN"
    }

    lang_code = lang_code_map.get(language, "en")  # default to "en" if language not found
    
    audio = gTTS(text=result.text, lang=lang_code)
    audio_file = 'listen_6_pdf.mp3'
    audio.save(audio_file)
    st.audio(audio_file)



