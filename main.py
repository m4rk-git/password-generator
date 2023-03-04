#!/usr/bin/env python
"""\
Short password generator 
"""
import random, string

import streamlit as st
import pyperclip, pyautogui

__author__ = "Mark Domgörgen"
__status__ = "finished"

st.title('Password Generator')

st.write('Password Length')

# Initialize the Dashboard
password_length = st.slider("Password Length", min_value=1, max_value=100, label_visibility='collapsed')

symbols = st.checkbox('Include Symbols ( e.g. @#$% )')

numbers = st.checkbox('Include Numbers ( e.g. 123456 )')

lower_letters = st.checkbox('Include Lowercase Characters ( e.g. abcdef )')

upper_letters = st.checkbox('Include Uppercase Characters ( e.g. ABCDEF )')

similar = st.checkbox('Exclude Similiar Characters ( e.g. i, l, 1, L, o, 0, O )')

ambitguous = st.checkbox('''Exclude Ambiguous Characters ( {} [] () /\ ' " ` ~ , ; . : < > )''')


if 'password' not in st.session_state:
    st.session_state.password = ''


password_area = st.empty() 
password_area.text_area("Password", value=st.session_state.password, label_visibility='collapsed', placeholder='Your new password will appear here', height=50)


col1, col2, col3 = st.columns([2.2,4,1.4], gap='large')
with col1:
    generate = st.button("Generate Password")
with col2:
    copy = st.button("Copy password")
with col3:
    reset = st.button("Reset")


def list_generator():
    """Generates List of allowed symbols, based on the checked features

    Returns:
        List: Allowed Characters in the password
    """
    
    characters = []
    if symbols:
        characters.extend(['!','@','#','$','%','^','&','*','(',')','-','_','=','+','`','~','[',']','{','}',';',':',"'",'"','<',',','\\','.','>','?','/'])
    if numbers:
        characters.extend(['0','1','2','3','4','5','6','7','8','9'])
    if lower_letters:
        characters.extend(string.ascii_lowercase)
    if upper_letters:
        characters.extend(string.ascii_uppercase)
    if similar:
        remove_list = ['b','6','c','C','(','g','q','9','G','6','L','l','i','1','I','O','o','0','S','s','5','V','v','u','U','z','Z','2']
        for i in remove_list:
            characters = [x for x in characters if x != i]
    if ambitguous:
        remove_list = ['{','}','[',']','(',')','/','\\',"'",'"','`','~',',', ';', '.', ':', '<', '>']
        for i in remove_list:
            characters = [x for x in characters if x != i]
    return characters
        

def password_generator():
    """Generates the password based on the created list

    Returns:
        String: Password
    """
    
    list = list_generator()
    if not list:
        st.error("You did not select any characters", icon="🚨")
        return ''
    selection = random.choices(list, k=password_length)
    return ''.join(str(i) for i in selection)

# Implementing the button functionalities
if (generate):
    password = password_generator()
    st.session_state.password = password
    password_area.text_area("Password", value=password, label_visibility='collapsed', height=50)

if (copy):
    pyperclip.copy(st.session_state.password)

if (reset):
    del st.session_state.password
    pyautogui.hotkey("ctrl","F5")
    




# Hiding Ads
hide_streamlit_style = """
            <style>
#           #MainMenu {visibility: hidden;} 
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


