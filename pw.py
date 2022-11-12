'''
Random Password Generator using Python
Author: Ayushi Rawat
'''

#import the necessary modules!
import streamlit as st
import random
import string

from PIL import Image



st.title("🔑 Strong Password Generator")
image = Image.open('https://www.technologyblog.org/wp-content/uploads/2022/10/complex-password-generator.jpg')
st.image(image, caption='Random Password Generator')

with st.expander("Check explanation below"):
    st.markdown('Strong **Password Generator** to generate secure passwords from characters, \
                letters, numbers, symbols, and special characters. Random password generator to create \
                alphanumeric passwords for any kind of login or other uses.')
#print('hello, Welcome to Password generator!')

#input the length of password
#length = int(input('\nEnter the length of password: '))
lengthst = int(st.number_input('Enter the length of password:',0,34))
#st.write(lengthst)                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
#temp = random.sample(all,length)
temp1 = random.sample(all,lengthst)

#create the password 
#password = "".join(temp)
password1 = "".join(temp1)

#print the password
#print(password)
st.text_area('Random Password:',password1)