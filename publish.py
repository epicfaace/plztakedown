from solcx import install_solc
install_solc(version='latest')

from web3 import Web3

from solcx import compile_source

contents = open("Storage.sol").read()
# Solidity source code
compiled_sol = compile_source(
    contents,
    output_values=['abi', 'bin']
)

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

Storage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Storage.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

storage = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

result = storage.functions.retrieve().call()
print(result)