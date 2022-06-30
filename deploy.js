async function main() {
    const StorageContract = await ethers.getContractFactory('Storage');
  
    // Start deployment, returning a promise that resolves to a contract object
    const storageContract = await StorageContract.deploy()
    console.log("deploying the contract")
    await storageContract.deployed()
    console.log("Contract deployed to address:", storageContract.address)
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error)
      process.exit(1)
    })
  