import streamlit as st
import json
from web3 import Web3
from lender import *
from borrower import *
from backend import *

st.header("Welcome to CoinLender!")

#pick to be a lender or a borrower
lender_or_borrower = st.selectbox('Do you want to be a lender or borrower?', ["",'Lender', 'Borrower'])

if lender_or_borrower == "Lender":
    lender()
elif lender_or_borrower == "Borrower": 
    borrower()
else:
    print("Please select an option")