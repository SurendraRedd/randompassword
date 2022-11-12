'''
Random Password Generator using streamlit
Author: Surendra Reddy
'''

#import the necessary modules!
import streamlit as st
import random
import string

from PIL import Image

# Page Config details
st.set_page_config(
        page_title = 'Password',
        page_icon = "🔑",
        layout = "centered",
        initial_sidebar_state = "expanded")
    

st.title("🔑 Random Password Generator")
image = Image.open('password-generator.jpg')
st.image(image, caption='Random Password Generator')

with st.expander("👉 what is this tool❓"):
    st.markdown('**Random Password Generator** to generate secure passwords from characters, \
                letters, numbers, symbols, and special characters. Random password generator to create \
                alphanumeric passwords for any kind of login or other uses')
    st.markdown('- 👉Select the **length** of the password')
    st.markdown('- 👉**Random password** will be generated based on the length')
    st.write('\n')

st.write('\n')

# Tooltips also support markdown
input_markdown = '''
By default max length will be 34 and min length is 6!
'''.strip()
lengthst = int(st.number_input('Enter the length of password',6,34,help=input_markdown))
                  

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
st.text_area('Random Password',password1,help="Password output")


st.write('\n')
URL = 'https://surendraredd-randompassword-pw-j36ex4.streamlit.app/'
with st.expander('Share This Tool'):
    st.write(URL)