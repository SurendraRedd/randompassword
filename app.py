'''
Random Password Generator using streamlit
Author: Surendra Reddy
'''

#import the necessary modules!
import streamlit as st
import random
import string
from streamlit_player import st_player

from PIL import Image

# Page Config details
st.set_page_config(
        page_title = 'Password',
        page_icon = "🔑",
        layout = "centered",
        initial_sidebar_state = "expanded")
    

st.title("🔑 Random Password Generator")
image = Image.open('password-generator.jpg')
st.image(image, caption='Random Password Generator',use_column_width='always')

col1, col2 = st.columns(2)

with col1:
    with st.expander('Demo'):
        #st.markdown('[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://surendraredd-randompassword.streamlit.app/))')
        # Embed a youtube video
        st_player("https://youtu.be/1VkPi33VQ6I")

with col2:
    with st.expander("👇What is Tool About & How it works❓"):
        st.markdown('**Random Password Generator** to generate secure passwords from characters, \
                    letters, numbers, symbols, and special characters. Random password generator to create \
                    alphanumeric passwords for any kind of login or other uses')
        st.markdown('1.Select the **length** of the password')
        st.markdown('2.Click on the **Generate** button. Else default password will be available')
        st.markdown('3.**Random password** will be generated based on the length')
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


if st.button('👉Generate'):
    #use random 
    temp1 = random.sample(all,lengthst)

    #create the password 
    password1 = "".join(temp1)

else:
    password1 = ""

#print the password
st.text_area('Random Password',password1,help="Password output")


st.write('\n')

URL = 'https://surendraredd-randompassword.streamlit.app/'
with st.expander('Share This Tool'):
    st.write(URL)