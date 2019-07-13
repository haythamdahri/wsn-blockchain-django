## Usage

After all dependancies are installed, run `Ganache` software.

First go to https://remix.ethereum.org/, create and compile your contract

Run the following commands to open the node console then deploy your contract to the Blockchain

Submit the transaction that deploys the contract
We have 4 clusters
1 => node{1} -> node{5}
1 => node{6} -> node{30}
1 => node{31} -> node{70}
1 => node{71} -> node{99}

```
HAYTHAM:~/Networking contract deloyment
$ node
> Web3 = require('web3')
> web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:7545"));
> code = fs.readFileSync('Networking.sol').toString()
> abiDefinition = JSON.parse(fs.readFileSync('Networking.abi'))
> const networkingContract = new web3.eth.Contract(abiDefinition)
> byteCode = fs.readFileSync('Networking.bin').toString()
> let accounts = [], accountsClusters = [], sinkNode;
> web3.eth.getAccounts().then(e => {sinkNode = e[0]; accounts = e;});
 // Set nodes on their clusters
> for( let i=1; i<accounts.length; i++ ) {
        if( i <= 5 ) {
            accountsClusters.push(0);
        } else if( i <= 30 ) {
            accountsClusters.push(1);
        } else if( i <= 70 ){
            accountsClusters.push(2);
        } else {  
            accountsClusters.push(3);
        } 
    }   
> networkingContract.options.data = "0x" + byteCode;    
> const deployedContract;
> networkingContract.deploy({
    arguments: [accounts.slice(1, accounts.length), accountsClusters, sinkNode]
})
.send({
    from: accounts[0],
    gas: 1500000
})
.then((newContractInstance) => {
    console.log(newContractInstance.options.address) // instance with the new contract address
});

```