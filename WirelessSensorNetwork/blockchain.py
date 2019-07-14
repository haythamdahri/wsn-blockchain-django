import os
from datetime import datetime
from time import sleep

from web3 import Web3

from WSN.settings import CONTRACT_ADDRESS, SERVER_ADDRESS, MINIMAL_ENERGY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/contracts/'

contract_source_code = ''
with open(os.path.join(BASE_DIR, 'Networking.sol'), 'r') as file:
    contract_source_code = file.read()

contract_abi = '''[
	{
		"constant": true,
		"inputs": [],
		"name": "getSinkNodeTransactionsCount",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_date",
				"type": "uint256"
			}
		],
		"name": "getTransactionDetails",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "nodes",
		"outputs": [
			{
				"name": "nodeAddress",
				"type": "address"
			},
			{
				"name": "cluster",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getSinkNode",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_sender",
				"type": "address"
			},
			{
				"name": "_receiver",
				"type": "address"
			},
			{
				"name": "_data",
				"type": "string"
			}
		],
		"name": "sendData",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getClustersCounters",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_a",
				"type": "string"
			},
			{
				"name": "_b",
				"type": "string"
			}
		],
		"name": "compare",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_a",
				"type": "string"
			},
			{
				"name": "_b",
				"type": "string"
			}
		],
		"name": "equal",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_node",
				"type": "address"
			}
		],
		"name": "getTransactionsDate",
		"outputs": [
			{
				"name": "",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_cluster_header",
				"type": "address"
			},
			{
				"name": "_data",
				"type": "string"
			}
		],
		"name": "sendDataToSinkNode",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getAllTransactionsDate",
		"outputs": [
			{
				"name": "",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_cluster",
				"type": "uint256"
			}
		],
		"name": "getClusterNodesAddresses",
		"outputs": [
			{
				"name": "local_addresses",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_nodeAddress",
				"type": "address"
			}
		],
		"name": "getNodeDetails",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getGlobalTransactionsCount",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "node_address",
				"type": "address"
			}
		],
		"name": "getTransactionsCount",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "clustersCounter",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "nodes_addresses",
				"type": "address[]"
			},
			{
				"name": "clusters",
				"type": "uint256[]"
			},
			{
				"name": "sink_node",
				"type": "address"
			},
			{
				"name": "_clustersCounter",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]'''

byte_code = ''
with open(os.path.join(BASE_DIR, 'Networking.bin'), 'rb') as file:
    byte_code = file.read()

full_byte_code = "60806040523480156200001157600080fd5b5060405162002057380380620020578339810180604052620000379190810190620002ce565b8060008190555081600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008090505b84518110156200017957600160408051908101604052808784815181101515620000ab57fe5b9060200190602002015173ffffffffffffffffffffffffffffffffffffffff1681526020018684815181101515620000df57fe5b906020019060200201518152509080600181540180825580915050906001820390600052602060002090600202016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010155505050808060010191505062000085565b50505050506200042a565b60006200019282516200040c565b905092915050565b600082601f8301121515620001ae57600080fd5b8151620001c5620001bf826200039a565b6200036c565b91508181835260208401935060208101905083856020840282011115620001eb57600080fd5b60005b838110156200021f578162000204888262000184565b845260208401935060208301925050600181019050620001ee565b5050505092915050565b600082601f83011215156200023d57600080fd5b8151620002546200024e82620003c3565b6200036c565b915081818352602084019350602081019050838560208402820111156200027a57600080fd5b60005b83811015620002ae5781620002938882620002b8565b8452602084019350602083019250506001810190506200027d565b5050505092915050565b6000620002c6825162000420565b905092915050565b60008060008060808587031215620002e557600080fd5b600085015167ffffffffffffffff8111156200030057600080fd5b6200030e878288016200019a565b945050602085015167ffffffffffffffff8111156200032c57600080fd5b6200033a8782880162000229565b93505060406200034d8782880162000184565b92505060606200036087828801620002b8565b91505092959194509250565b6000604051905081810181811067ffffffffffffffff821117156200039057600080fd5b8060405250919050565b600067ffffffffffffffff821115620003b257600080fd5b602082029050602081019050919050565b600067ffffffffffffffff821115620003db57600080fd5b602082029050602081019050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006200041982620003ec565b9050919050565b6000819050919050565b611c1d806200043a6000396000f3fe6080604052600436106100e0576000357c010000000000000000000000000000000000000000000000000000000090048063026bfd93146100e55780630fa683d3146101105780631c53c280146101505780631f2cb6e11461018e5780632b389aee146101b95780632fea6afb146101e25780633a96fdd71461020d57806346bdca9a1461024a57806349cb3ec5146102875780635549893c146102c4578063600f0d19146102ed57806364a0aec814610318578063bafb358114610355578063bca5f8f514610393578063d6345e6f146103be578063ff0b073d146103fb575b600080fd5b3480156100f157600080fd5b506100fa610426565b6040516101079190611a3e565b60405180910390f35b34801561011c57600080fd5b50610137600480360361013291908101906117fe565b61058a565b604051610147949392919061196a565b60405180910390f35b34801561015c57600080fd5b50610177600480360361017291908101906117fe565b61074f565b6040516101859291906119b6565b60405180910390f35b34801561019a57600080fd5b506101a36107a2565b6040516101b0919061194f565b60405180910390f35b3480156101c557600080fd5b506101e060048036036101db91908101906116d7565b6107cc565b005b3480156101ee57600080fd5b506101f7610904565b6040516102049190611a59565b60405180910390f35b34801561021957600080fd5b50610234600480360361022f9190810190611792565b61090d565b6040516102419190611a3e565b60405180910390f35b34801561025657600080fd5b50610271600480360361026c9190810190611792565b610bd3565b60405161027e9190611a23565b60405180910390f35b34801561029357600080fd5b506102ae60048036036102a991908101906116ae565b610be9565b6040516102bb9190611a01565b60405180910390f35b3480156102d057600080fd5b506102eb60048036036102e6919081019061173e565b610f68565b005b3480156102f957600080fd5b506103026110c1565b60405161030f9190611a01565b60405180910390f35b34801561032457600080fd5b5061033f600480360361033a91908101906117fe565b61116e565b60405161034c91906119df565b60405180910390f35b34801561036157600080fd5b5061037c600480360361037791908101906116ae565b6112e8565b60405161038a9291906119b6565b60405180910390f35b34801561039f57600080fd5b506103a861142e565b6040516103b59190611a3e565b60405180910390f35b3480156103ca57600080fd5b506103e560048036036103e091908101906116ae565b611463565b6040516103f29190611a3e565b60405180910390f35b34801561040757600080fd5b50610410611585565b60405161041d9190611a59565b60405180910390f35b6000806000905060008090505b60028054905081101561058257600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1660028281548110151561048857fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806105695750600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1660028281548110151561051f57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610575576001820191505b8080600101915050610433565b508091505090565b6000806000606060008090505b60028054905081101561074657856002828154811015156105b457fe5b9060005260206000209060040201600201541415610739576002818154811015156105db57fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1660028281548110151561061c57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1660028381548110151561065d57fe5b90600052602060002090600402016002015460028481548110151561067e57fe5b9060005260206000209060040201600301808054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156107245780601f106106f957610100808354040283529160200191610724565b820191906000526020600020905b81548152906001019060200180831161070757829003601f168201915b50505050509050945094509450945050610748565b8080600101915050610597565b505b9193509193565b60018181548110151561075e57fe5b90600052602060002090600202016000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010154905082565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60026080604051908101604052808573ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff168152602001428152602001838152509080600181540180825580915050906001820390600052602060002090600402016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030190805190602001906108fb92919061158b565b50505050505050565b60008054905090565b600060608390506060839050600082519050808251101561092d57815190505b60008090505b81811015610b7957828181518110151561094957fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191684828151811015156109c457fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161015610a63577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff945050505050610bcd565b8281815181101515610a7157fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19168482815181101515610aec57fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161115610b6c576001945050505050610bcd565b8080600101915050610933565b50815183511015610baf577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9350505050610bcd565b815183511115610bc55760019350505050610bcd565b600093505050505b92915050565b600080610be0848461090d565b14905092915050565b6060600080905060008090505b600280549050811015610dd257600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16148015610ccb57508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610c8157fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b80610d4157508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610cf757fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b80610db757508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610d6d57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610dc55781806001019250505b8080600101915050610bf6565b50606081604051908082528060200260200182016040528015610e045781602001602082028038833980820191505090505b509050600080905060008090505b600280549050811015610f5c578573ffffffffffffffffffffffffffffffffffffffff16600282815481101515610e4557fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161480610f0457508573ffffffffffffffffffffffffffffffffffffffff16600282815481101515610eba57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610f4f57600281815481101515610f1857fe5b9060005260206000209060040201600201548383815181101515610f3857fe5b906020019060200201818152505081806001019250505b8080600101915050610e12565b50819350505050919050565b60026080604051908101604052808473ffffffffffffffffffffffffffffffffffffffff168152602001600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001428152602001838152509080600181540180825580915050906001820390600052602060002090600402016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030190805190602001906110b992919061158b565b505050505050565b6060806002805490506040519080825280602002602001820160405280156110f85781602001602082028038833980820191505090505b509050600080905060008090505b6002805490508110156111655760028181548110151561112257fe5b906000526020600020906004020160020154838381518110151561114257fe5b906020019060200201818152505081806001019250508080600101915050611106565b50819250505090565b6060600080905060008090505b6001805490508110156111c6578360018281548110151561119857fe5b90600052602060002090600202016001015414156111b95781806001019250505b808060010191505061117b565b506060816040519080825280602002602001820160405280156111f85781602001602082028038833980820191505090505b509050600080905060008090505b6001805490508110156112dc578560018281548110151561122357fe5b90600052602060002090600202016001015414156112cf5760018181548110151561124a57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16838381518110151561128a57fe5b9060200190602002019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505081806001019250505b8080600101915050611206565b50819350505050919050565b6000806060600260405190808252806020026020018201604052801561132257816020015b606081526020019060019003908161130d5790505b50905060008090505b600180549050811015611426578473ffffffffffffffffffffffffffffffffffffffff1660018281548110151561135e57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415611419576001818154811015156113bb57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166001828154811015156113fc57fe5b906000526020600020906002020160010154935093505050611429565b808060010191505061132b565b50505b915091565b6000806000905060008090505b60028054905081101561145b57600182019150808060010191505061143b565b508091505090565b6000806000905060008090505b60028054905081101561157b578373ffffffffffffffffffffffffffffffffffffffff166002828154811015156114a357fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16148061156257508373ffffffffffffffffffffffffffffffffffffffff1660028281548110151561151857fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b1561156e576001820191505b8080600101915050611470565b5080915050919050565b60005481565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106115cc57805160ff19168380011785556115fa565b828001600101855582156115fa579182015b828111156115f95782518255916020019190600101906115de565b5b509050611607919061160b565b5090565b61162d91905b80821115611629576000816000905550600101611611565b5090565b90565b600061163c8235611b74565b905092915050565b600082601f830112151561165757600080fd5b813561166a61166582611aa1565b611a74565b9150808252602083016020830185838301111561168657600080fd5b611691838284611b90565b50505092915050565b60006116a68235611b86565b905092915050565b6000602082840312156116c057600080fd5b60006116ce84828501611630565b91505092915050565b6000806000606084860312156116ec57600080fd5b60006116fa86828701611630565b935050602061170b86828701611630565b925050604084013567ffffffffffffffff81111561172857600080fd5b61173486828701611644565b9150509250925092565b6000806040838503121561175157600080fd5b600061175f85828601611630565b925050602083013567ffffffffffffffff81111561177c57600080fd5b61178885828601611644565b9150509250929050565b600080604083850312156117a557600080fd5b600083013567ffffffffffffffff8111156117bf57600080fd5b6117cb85828601611644565b925050602083013567ffffffffffffffff8111156117e857600080fd5b6117f485828601611644565b9150509250929050565b60006020828403121561181057600080fd5b600061181e8482850161169a565b91505092915050565b61183081611b22565b82525050565b600061184182611ae7565b80845260208401935061185383611acd565b60005b8281101561188557611869868351611827565b61187282611b08565b9150602086019550600181019050611856565b50849250505092915050565b600061189c82611af2565b8084526020840193506118ae83611ada565b60005b828110156118e0576118c4868351611940565b6118cd82611b15565b91506020860195506001810190506118b1565b50849250505092915050565b6118f581611b34565b82525050565b61190481611b40565b82525050565b600061191582611afd565b808452611929816020860160208601611b9f565b61193281611bd2565b602085010191505092915050565b61194981611b6a565b82525050565b60006020820190506119646000830184611827565b92915050565b600060808201905061197f6000830187611827565b61198c6020830186611827565b6119996040830185611940565b81810360608301526119ab818461190a565b905095945050505050565b60006040820190506119cb6000830185611827565b6119d86020830184611940565b9392505050565b600060208201905081810360008301526119f98184611836565b905092915050565b60006020820190508181036000830152611a1b8184611891565b905092915050565b6000602082019050611a3860008301846118ec565b92915050565b6000602082019050611a5360008301846118fb565b92915050565b6000602082019050611a6e6000830184611940565b92915050565b6000604051905081810181811067ffffffffffffffff82111715611a9757600080fd5b8060405250919050565b600067ffffffffffffffff821115611ab857600080fd5b601f19601f8301169050602081019050919050565b6000602082019050919050565b6000602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b6000602082019050919050565b6000611b2d82611b4a565b9050919050565b60008115159050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b6000611b7f82611b4a565b9050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015611bbd578082015181840152602081019050611ba2565b83811115611bcc576000848401525b50505050565b6000601f19601f830116905091905056fea265627a7a72305820404025889940730e5a222bfa8f7ab679b5005e426b8a3850205675c6a16363fd6c6578706572696d656e74616cf50037"

SERVER_ADDRESS = 'http://127.0.0.1:7545'
CONTRACT_ADDRESS = '0x1bd19716EF787833F90Ec7DD4Ff029BE34a166ac'
DEPLOYED = False


class Transaction:

    def __init__(self, sender, receiver, transaction_date, data):
        self.sender = sender
        self.receiver = receiver
        self.transaction_date = transaction_date
        self.data = data

    def __str__(self):
        return f'Sender: {self.sender} | Receiver: {self.receiver} | Date: {self.transaction_date} | Date: {self.data}'


class Blockchain:
    web3 = None
    contract = None

    # Set instance decorator
    @classmethod
    def check_instances(cls):
        if cls.web3 is None:
            cls.web3 = Web3(Web3.HTTPProvider(SERVER_ADDRESS))
        if cls.contract is None:
            cls.contract = cls.web3.eth.contract(
                address=CONTRACT_ADDRESS,
                abi=contract_abi,
            )

    # Retrieve blockchain accounts
    @classmethod
    def get_blockchain_accounts(cls):
        cls.check_instances()
        return [(account, account) for account in cls.web3.eth.accounts]

    # Retrieve a given node details
    @classmethod
    def get_node_details(cls, node):
        cls.check_instances()
        node_address = cls.web3.toChecksumAddress(node)
        node_details = cls.contract.functions.getNodeDetails(node_address).call()
        return {'address': node_details[0], 'cluster': node_details[1]}

    # Retrieve transactions of a given node
    @classmethod
    def get_node_transactions(cls, node):
        cls.check_instances()
        node_address = cls.web3.toChecksumAddress(node)
        transactions_dates = cls.contract.functions.getTransactionsDate(node_address).call()
        transactions = list()
        for transaction_date in transactions_dates:
            sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
            if sender == node or receiver == node:
                transactions.append(Transaction(sender, receiver, datetime.fromtimestamp(float(date)), data))
        return sorted(transactions, key=lambda transaction: transaction.transaction_date, reverse=True)

    # Check if a node is the sink one
    @classmethod
    def check_sink_node(cls, node):
        return cls.get_sink_node().get('address') == node

    # Retrieve sink node
    @classmethod
    def get_sink_node(cls):
        cls.check_instances()
        return {'address': cls.contract.functions.getSinkNode().call(), 'is_sink_node': True, 'cluster': None}

    # Retrieve all transactions
    @classmethod
    def get_all_transactions(cls):
        cls.check_instances()
        transactions = list()
        for transaction_date in cls.contract.functions.getAllTransactionsDate().call():
            print(cls.contract.functions.getTransactionDetails(transaction_date).call())
            sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
            transactions.append(Transaction(sender, receiver, datetime.fromtimestamp(float(date)), data))
        return sorted(transactions, key=lambda transaction: transaction.transaction_date, reverse=True)

    # Retrieve all transactions
    @classmethod
    def get_custom_transactions(cls, keyword):
        cls.check_instances()
        transactions = list()
        for transaction_date in cls.contract.functions.getAllTransactionsDate().call():
            print(cls.contract.functions.getTransactionDetails(transaction_date).call())
            sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
            if str(date) == str(keyword):
                transactions.append(Transaction(sender, receiver, datetime.fromtimestamp(float(date)), data))
        return sorted(transactions, key=lambda transaction: transaction.transaction_date, reverse=True)

    # Send data to the cluster header
    @classmethod
    def send_data_to_cluster_header(cls, node_address, data):
        try:
            cls.check_instances()
            node_details = cls.get_node_details(node_address)
            cluster = node_details.get('cluster')
            cluster_header = cls.get_cluster_header(cluster)

            # Sending data from current connected user to the cluster-header
            node_address = cls.web3.toChecksumAddress(node_details.get('address'))
            cluster_header_address = cls.web3.toChecksumAddress(cluster_header.get('address'))
            sink_node_address = cls.web3.toChecksumAddress(cls.get_sink_node().get('address'))
            transaction = {'from': node_address,
                           'gas': cls.contract.functions.sendData(node_address, cluster_header_address,
                                                                  data).estimateGas()}
            contract_data = cls.contract.functions.sendData(node_address, cluster_header_address,
                                                            data).buildTransaction(transaction)

            # Send built transaction
            cls.web3.eth.sendTransaction(contract_data)

            # Stop before sending the second transaction
            sleep(2)

            # Send received data from the cluster-header to the sink node
            new_transaction = {'from': cluster_header_address,
                               'gas': cls.contract.functions.sendDataToSinkNode(cluster_header_address,
                                                                      data).estimateGas()}
            new_contract_data = cls.contract.functions.sendDataToSinkNode(cluster_header_address,
                                                                data).buildTransaction(new_transaction)
            # Send built transaction
            cls.web3.eth.sendTransaction(new_contract_data)

            # Return true for successful transactions
            return True
        except Exception as ex:
            print(ex)
            # In case of an exception return false
            return False

    # Retrieve cluster-header for a given cluster
    @classmethod
    def get_cluster_header(cls, cluster):
        cluster_nodes_balances = list()
        for account in cls.contract.functions.getClusterNodesAddresses(cluster).call():
            if type(account) is not str:
                account = account[0]
            cluster_nodes_balances.append((account, cls.web3.eth.getBalance(account)))
        cluster_header = sorted(cluster_nodes_balances, key=lambda line: line[1], reverse=True)[0]
        for address, energy in sorted(cluster_nodes_balances, key=lambda line: line[1]):
            if cls.web3.fromWei(energy, 'ether') >= MINIMAL_ENERGY:
                cluster_header = (address, energy)
                break
        print(f'Cluste header: {cluster_header}')
        return {'address': cluster_header[0], 'balance': cluster_header[1]}
