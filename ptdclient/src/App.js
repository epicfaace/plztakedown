import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from "react";
import Contract from 'web3-eth-contract';

function App() {
  const [data, setData] = useState(null);
  useEffect(() => {
    // https://ropsten.etherscan.io/address/0xEf80B7e50e74a48Dbb76d1dec3ae1eDFcdd75E1B#code
    Contract.setProvider('wss://ropsten.infura.io/ws/v3/7709bfd6a1d141f8ac2bd969c5688fbe');
    let jsonInterface = [{ "inputs": [], "name": "owner", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "retrieve", "outputs": [{ "internalType": "string", "name": "", "type": "string" }], "stateMutability": "view", "type": "function" }];
    let address = '0xEf80B7e50e74a48Dbb76d1dec3ae1eDFcdd75E1B';
    let contract = new Contract(jsonInterface, address);
    contract.methods.retrieve().call({}, function (error, result) {
      setData(result);
      if (error) {
        console.error(error);
      } else {
        console.log(result);
      }
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {!data && <p>Loading...</p>}
        {data && <div dangerouslySetInnerHTML={{__html: data}} />}
      </header>
    </div>
  );
}

export default App;
