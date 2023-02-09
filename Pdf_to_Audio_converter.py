import PyPDF2
import os
import easygui
import re
from gtts import gTTS
from googletrans import Translator

file = easygui.fileopenbox(msg="Select your PDF", title="Select a PDF File",default="*.pdf",filetypes=["*.pdf",])
file_path = file

if(os.path.exists(file_path)):
    pass
else:
    print("File does not exists")
    exit()
    
f = open(file_path, 'rb')

pdffile = PyPDF2.PdfFileReader(f)
no_of_pages = pdffile.getNumPages()

# Using regex to filter only words and numbers

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
    translator = Translator()
    translator.detect(string_words)
    #translator.translate(string_words)
    result = translator.translate(string_words, dest='en')
    print(result.text)
            
tts = gTTS(text=result.text, lang='en')
tts.save("listen_6_pdf.mp3")
    
