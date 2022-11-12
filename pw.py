'''
Random Password Generator using Python
Author: Surendra Reddy
'''

#import the necessary modules!
import streamlit as st
import random
import string

from PIL import Image

st.title("🔑 Random Password Generator")
image = Image.open('password-generator.jpg')
st.image(image, caption='Random Password Generator')

with st.expander("👉 Explanation"):
    st.markdown('**Random Password Generator** to generate secure passwords from characters, \
                letters, numbers, symbols, and special characters. Random password generator to create \
                alphanumeric passwords for any kind of login or other uses')
    st.markdown('- 👉Select the **length** of the password')
    st.markdown('- 👉**Random password** will be generated based on the length')
    st.write('\n')

# Tooltips also support markdown
input_markdown = '''
By default max length will be 34 and min length is 0!
'''.strip()
lengthst = int(st.number_input('Enter the length of password',0,34,help=input_markdown))
                  

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp1 = random.sample(all,lengthst)

#create the password 
password1 = "".join(temp1)

#print the password
st.text_area('Random Password:',password1)

with st.expander('Share This Tool'):
    st.text_area('',password1)