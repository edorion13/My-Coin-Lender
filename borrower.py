import streamlit as st
from backend import *
from web3 import Web3


contract, contract_abi, contract_address, ganache_url = get_info()
web3 = Web3(Web3.HTTPProvider(ganache_url))
eth_price = get_eth_price()


def loanListing():
    loan_amount = st.slider('Pick an amount', 0, 10000)
    loan_in_eth = loan_amount / eth_price
    st.write("Amount in eth", loan_in_eth)

    amount_in_wei = int(loan_amount * 50735.67)

    interest_rate = 0
    termOptions = st.selectbox('Select term options in months', (1,3,6,12,18,24,30,36))

    if termOptions == 1: 
        st.caption("Your interest rate will be 15%")
        interest_rate = 15

    elif termOptions == 3:
        st.caption("Your interest rate will be 12%" )
        interest_rate = 12

    elif  termOptions == 6:
        st.caption("Your interest rate will be 10%" )        
        interest_rate = 10
        
    elif  termOptions == 12:
        st.caption("Your interest rate will be 8%" )        
        interest_rate = 8    
    
    elif  termOptions == 18:
        st.caption("Your interest rate will be 7%" )        
        interest_rate = 7    
    
    elif  termOptions == 24:
        st.caption("Your interest rate will be 6%" )        
        interest_rate = 6    
    
    elif  termOptions == 30:
        st.caption("Your interest rate will be 5%" )        
        interest_rate = 5   

    else :
        termOptions == 36
        st.caption("Your interest rate will be 4%" )        
        interest_rate = 4               
    
    
    if st.button('Create loan'):
        transaction = contract.functions.createLoan(amount_in_wei, interest_rate, termOptions).transact({'from': '0x906c2BeBdeBD7B388472999c4a972923302C1C34'})
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        tx_id = web3.eth.get_transaction_receipt
        st.caption("Success!")

    

def makePayment():
    amount = st.number_input('Enter payment amount ($)', 0, 10000) #figure out a way to no be able to pay more than the original loan is for
    amount_in_wei = int(amount * 50735.67)
    payment_in_eth = amount / eth_price
    st.write("Amount in eth", payment_in_eth)

    if st.button('Pay Now'):
        transaction = contract.functions.repayLoan(0).transact({'from': '0x906c2BeBdeBD7B388472999c4a972923302C1C34', 'value': amount_in_wei})
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        st.caption("Success!")

def view_detials():
    if st.button("Current Loan Details"):
        loan_details = contract.functions.getLoanDetails(0).call()
        print(loan_details)
    
        


def borrower():
    st.header("Welcome to the Lender page")
    st.subheader("Your wallet address: 0x906c2BeBdeBD7B388472999c4a972923302C1C34")
    loan_or_pay = st.selectbox("Are you here to create a loan listing or make a payment?", ["","Create loan listing", "Make Paymet", "Check Current Loan Details"])


    if loan_or_pay == "Create loan listing":
        loanListing()
    elif loan_or_pay == "Make Paymet":
        makePayment()
    elif loan_or_pay== "Check Current Loan Details":
        view_detials()
    else:
        print("select an option")