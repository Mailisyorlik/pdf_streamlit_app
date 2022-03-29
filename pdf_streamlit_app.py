#initial streamlit file
import streamlit as st
from pdfminer.high_level import extract_text
import tkinter.filedialog
from 


pdf_file = tkinter.filedialog.askopenfilename()
#precompile regex patterns here


#may need a directory specification
text = extract_text(pdf_file)
#print(type(text))
#with open('training.txt', 'w') as f:
   # f.writelines(text.join(text))

print(text)



st.write(text)
