from web3 import Web3
import requests

def get_info():
    contract_address = '0xB9974c8712a543F5df650F00E94B5AFAf8c92b19'
    ganache_url = 'HTTP://127.0.0.1:7545'
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    contract_abi = [
        {
            "inputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "loanId",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "borrower",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "loanAmount",
                    "type": "uint256"
                }
            ],
            "name": "LoanCreated",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "loanId",
                    "type": "uint256"
                }
            ],
            "name": "LoanFullyRepaid",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "loanId",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "lender",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "fundAmount",
                    "type": "uint256"
                }
            ],
            "name": "LoanFunded",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "loanId",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "repaymentAmount",
                    "type": "uint256"
                }
            ],
            "name": "LoanPayment",
            "type": "event"
        },
        {
            "payable": True,
            "stateMutability": "payable",
            "type": "fallback"
        },
        {
            "constant": False,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_loanAmount",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "_interestRate",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "_repaymentTerm",
                    "type": "uint256"
                }
            ],
            "name": "createLoan",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [],
            "name": "deposit",
            "outputs": [],
            "payable": True,
            "stateMutability": "payable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_loanId",
                    "type": "uint256"
                }
            ],
            "name": "fundLoan",
            "outputs": [],
            "payable": True,
            "stateMutability": "payable",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_loanId",
                    "type": "uint256"
                }
            ],
            "name": "getLoanDetails",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                },
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "loanIdCounter",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "loans",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "loanId",
                    "type": "uint256"
                },
                {
                    "internalType": "address payable",
                    "name": "borrower",
                    "type": "address"
                },
                {
                    "internalType": "address payable",
                    "name": "lender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "loanAmount",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "interestRate",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "repaymentTerm",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "fundAmount",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "amountPayed",
                    "type": "uint256"
                },
                {
                    "internalType": "bool",
                    "name": "funded",
                    "type": "bool"
                },
                {
                    "internalType": "bool",
                    "name": "repaid",
                    "type": "bool"
                },
                {
                    "internalType": "uint256",
                    "name": "balanceRemaning",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "amountOwed",
                    "type": "uint256"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_loanId",
                    "type": "uint256"
                }
            ],
            "name": "repayLoan",
            "outputs": [],
            "payable": True,
            "stateMutability": "payable",
            "type": "function"
        }
    ]
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    return contract, contract_abi, contract_address, ganache_url

import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    parameters = {
        "ids": "ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    eth_price = data["ethereum"]["usd"]

    return eth_price

# Call the function to get the ETH price
price = get_eth_price()

print(price)

