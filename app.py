# Creating An Application for Vote Check
'''
Programming language used : Python
Front-end FrameWork : Streamlit
Deployement : Streamlit

'''
# Importing streamlit Library
# as - Alias Name
import streamlit as st

# Title of the Application

st.title('Vote Check Application 🚀')

# Getting Age Input From the User
age=st.number_input('Enter Your Age 😎 :')

# Checking The Age is Elibile for Voting or Not

# Creating Vote Check Button

if st.button('Check'):
    if(age>=18):
        st.write('You are Eligible For Voting 🎉')
    else:
        remaining=18-age
        st.write(f'You are not Eligible For Voting, Still You Have to Wait for {remaining} Years 🥲')    


