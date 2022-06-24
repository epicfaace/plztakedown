from solcx import install_solc
install_solc(version='latest')

from web3 import Web3
from web3.middleware import geth_poa_middleware
from solcx import compile_source

contract_contents = open("Storage.sol").read()
private_key = open("private-key").read()

# Solidity source code
compiled_sol = compile_source(
    contract_contents,
    output_values=['abi', 'bin']
)

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
# w3 = Web3(Web3.EthereumTesterProvider())
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# set pre-funded account as sender
account = w3.eth.account.privateKeyToAccount(private_key)
w3.eth.default_account = account.address
print(account.address)

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