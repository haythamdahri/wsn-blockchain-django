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

full_byte_code = "60806040523480156200001157600080fd5b5060405162001e7638038062001e768339810180604052620000379190810190620002ce565b8060008190555081600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008090505b84518110156200017957600160408051908101604052808784815181101515620000ab57fe5b9060200190602002015173ffffffffffffffffffffffffffffffffffffffff1681526020018684815181101515620000df57fe5b906020019060200201518152509080600181540180825580915050906001820390600052602060002090600202016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010155505050808060010191505062000085565b50505050506200042a565b60006200019282516200040c565b905092915050565b600082601f8301121515620001ae57600080fd5b8151620001c5620001bf826200039a565b6200036c565b91508181835260208401935060208101905083856020840282011115620001eb57600080fd5b60005b838110156200021f578162000204888262000184565b845260208401935060208301925050600181019050620001ee565b5050505092915050565b600082601f83011215156200023d57600080fd5b8151620002546200024e82620003c3565b6200036c565b915081818352602084019350602081019050838560208402820111156200027a57600080fd5b60005b83811015620002ae5781620002938882620002b8565b8452602084019350602083019250506001810190506200027d565b5050505092915050565b6000620002c6825162000420565b905092915050565b60008060008060808587031215620002e557600080fd5b600085015167ffffffffffffffff8111156200030057600080fd5b6200030e878288016200019a565b945050602085015167ffffffffffffffff8111156200032c57600080fd5b6200033a8782880162000229565b93505060406200034d8782880162000184565b92505060606200036087828801620002b8565b91505092959194509250565b6000604051905081810181811067ffffffffffffffff821117156200039057600080fd5b8060405250919050565b600067ffffffffffffffff821115620003b257600080fd5b602082029050602081019050919050565b600067ffffffffffffffff821115620003db57600080fd5b602082029050602081019050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006200041982620003ec565b9050919050565b6000819050919050565b611a3c806200043a6000396000f3fe6080604052600436106100d5576000357c010000000000000000000000000000000000000000000000000000000090048063026bfd93146100da5780630fa683d3146101055780631c53c280146101455780631f2cb6e1146101835780632b389aee146101ae5780632fea6afb146101d75780633a96fdd71461020257806346bdca9a1461023f57806349cb3ec51461027c578063600f0d19146102b957806364a0aec8146102e4578063bafb358114610321578063bca5f8f51461035f578063d6345e6f1461038a578063ff0b073d146103c7575b600080fd5b3480156100e657600080fd5b506100ef6103f2565b6040516100fc919061185d565b60405180910390f35b34801561011157600080fd5b5061012c6004803603610127919081019061161d565b610556565b60405161013c9493929190611789565b60405180910390f35b34801561015157600080fd5b5061016c6004803603610167919081019061161d565b61071b565b60405161017a9291906117d5565b60405180910390f35b34801561018f57600080fd5b5061019861076e565b6040516101a5919061176e565b60405180910390f35b3480156101ba57600080fd5b506101d560048036036101d0919081019061154a565b610798565b005b3480156101e357600080fd5b506101ec6108d0565b6040516101f99190611878565b60405180910390f35b34801561020e57600080fd5b50610229600480360361022491908101906115b1565b6108d9565b604051610236919061185d565b60405180910390f35b34801561024b57600080fd5b50610266600480360361026191908101906115b1565b610b9f565b6040516102739190611842565b60405180910390f35b34801561028857600080fd5b506102a3600480360361029e9190810190611521565b610bb5565b6040516102b09190611820565b60405180910390f35b3480156102c557600080fd5b506102ce610f34565b6040516102db9190611820565b60405180910390f35b3480156102f057600080fd5b5061030b6004803603610306919081019061161d565b610fe1565b60405161031891906117fe565b60405180910390f35b34801561032d57600080fd5b5061034860048036036103439190810190611521565b61115b565b6040516103569291906117d5565b60405180910390f35b34801561036b57600080fd5b506103746112a1565b604051610381919061185d565b60405180910390f35b34801561039657600080fd5b506103b160048036036103ac9190810190611521565b6112d6565b6040516103be919061185d565b60405180910390f35b3480156103d357600080fd5b506103dc6113f8565b6040516103e99190611878565b60405180910390f35b6000806000905060008090505b60028054905081101561054e57600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1660028281548110151561045457fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806105355750600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166002828154811015156104eb57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610541576001820191505b80806001019150506103ff565b508091505090565b6000806000606060008090505b600280549050811015610712578560028281548110151561058057fe5b9060005260206000209060040201600201541415610705576002818154811015156105a757fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166002828154811015156105e857fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1660028381548110151561062957fe5b90600052602060002090600402016002015460028481548110151561064a57fe5b9060005260206000209060040201600301808054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156106f05780601f106106c5576101008083540402835291602001916106f0565b820191906000526020600020905b8154815290600101906020018083116106d357829003601f168201915b50505050509050945094509450945050610714565b8080600101915050610563565b505b9193509193565b60018181548110151561072a57fe5b90600052602060002090600202016000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010154905082565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60026080604051908101604052808573ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff168152602001428152602001838152509080600181540180825580915050906001820390600052602060002090600402016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030190805190602001906108c79291906113fe565b50505050505050565b60008054905090565b60006060839050606083905060008251905080825110156108f957815190505b60008090505b81811015610b4557828181518110151561091557fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916848281518110151561099057fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161015610a2f577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff945050505050610b99565b8281815181101515610a3d57fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19168482815181101515610ab857fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19161115610b38576001945050505050610b99565b80806001019150506108ff565b50815183511015610b7b577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9350505050610b99565b815183511115610b915760019350505050610b99565b600093505050505b92915050565b600080610bac84846108d9565b14905092915050565b6060600080905060008090505b600280549050811015610d9e57600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16148015610c9757508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610c4d57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b80610d0d57508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610cc357fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b80610d8357508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610d3957fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610d915781806001019250505b8080600101915050610bc2565b50606081604051908082528060200260200182016040528015610dd05781602001602082028038833980820191505090505b509050600080905060008090505b600280549050811015610f28578573ffffffffffffffffffffffffffffffffffffffff16600282815481101515610e1157fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161480610ed057508573ffffffffffffffffffffffffffffffffffffffff16600282815481101515610e8657fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610f1b57600281815481101515610ee457fe5b9060005260206000209060040201600201548383815181101515610f0457fe5b906020019060200201818152505081806001019250505b8080600101915050610dde565b50819350505050919050565b606080600280549050604051908082528060200260200182016040528015610f6b5781602001602082028038833980820191505090505b509050600080905060008090505b600280549050811015610fd857600281815481101515610f9557fe5b9060005260206000209060040201600201548383815181101515610fb557fe5b906020019060200201818152505081806001019250508080600101915050610f79565b50819250505090565b6060600080905060008090505b600180549050811015611039578360018281548110151561100b57fe5b906000526020600020906002020160010154141561102c5781806001019250505b8080600101915050610fee565b5060608160405190808252806020026020018201604052801561106b5781602001602082028038833980820191505090505b509050600080905060008090505b60018054905081101561114f578560018281548110151561109657fe5b9060005260206000209060020201600101541415611142576001818154811015156110bd57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1683838151811015156110fd57fe5b9060200190602002019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505081806001019250505b8080600101915050611079565b50819350505050919050565b6000806060600260405190808252806020026020018201604052801561119557816020015b60608152602001906001900390816111805790505b50905060008090505b600180549050811015611299578473ffffffffffffffffffffffffffffffffffffffff166001828154811015156111d157fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141561128c5760018181548110151561122e57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1660018281548110151561126f57fe5b90600052602060002090600202016001015493509350505061129c565b808060010191505061119e565b50505b915091565b6000806000905060008090505b6002805490508110156112ce5760018201915080806001019150506112ae565b508091505090565b6000806000905060008090505b6002805490508110156113ee578373ffffffffffffffffffffffffffffffffffffffff1660028281548110151561131657fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806113d557508373ffffffffffffffffffffffffffffffffffffffff1660028281548110151561138b57fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b156113e1576001820191505b80806001019150506112e3565b5080915050919050565b60005481565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061143f57805160ff191683800117855561146d565b8280016001018555821561146d579182015b8281111561146c578251825591602001919060010190611451565b5b50905061147a919061147e565b5090565b6114a091905b8082111561149c576000816000905550600101611484565b5090565b90565b60006114af8235611993565b905092915050565b600082601f83011215156114ca57600080fd5b81356114dd6114d8826118c0565b611893565b915080825260208301602083018583830111156114f957600080fd5b6115048382846119af565b50505092915050565b600061151982356119a5565b905092915050565b60006020828403121561153357600080fd5b6000611541848285016114a3565b91505092915050565b60008060006060848603121561155f57600080fd5b600061156d868287016114a3565b935050602061157e868287016114a3565b925050604084013567ffffffffffffffff81111561159b57600080fd5b6115a7868287016114b7565b9150509250925092565b600080604083850312156115c457600080fd5b600083013567ffffffffffffffff8111156115de57600080fd5b6115ea858286016114b7565b925050602083013567ffffffffffffffff81111561160757600080fd5b611613858286016114b7565b9150509250929050565b60006020828403121561162f57600080fd5b600061163d8482850161150d565b91505092915050565b61164f81611941565b82525050565b600061166082611906565b808452602084019350611672836118ec565b60005b828110156116a457611688868351611646565b61169182611927565b9150602086019550600181019050611675565b50849250505092915050565b60006116bb82611911565b8084526020840193506116cd836118f9565b60005b828110156116ff576116e386835161175f565b6116ec82611934565b91506020860195506001810190506116d0565b50849250505092915050565b61171481611953565b82525050565b6117238161195f565b82525050565b60006117348261191c565b8084526117488160208601602086016119be565b611751816119f1565b602085010191505092915050565b61176881611989565b82525050565b60006020820190506117836000830184611646565b92915050565b600060808201905061179e6000830187611646565b6117ab6020830186611646565b6117b8604083018561175f565b81810360608301526117ca8184611729565b905095945050505050565b60006040820190506117ea6000830185611646565b6117f7602083018461175f565b9392505050565b600060208201905081810360008301526118188184611655565b905092915050565b6000602082019050818103600083015261183a81846116b0565b905092915050565b6000602082019050611857600083018461170b565b92915050565b6000602082019050611872600083018461171a565b92915050565b600060208201905061188d600083018461175f565b92915050565b6000604051905081810181811067ffffffffffffffff821117156118b657600080fd5b8060405250919050565b600067ffffffffffffffff8211156118d757600080fd5b601f19601f8301169050602081019050919050565b6000602082019050919050565b6000602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b6000602082019050919050565b600061194c82611969565b9050919050565b60008115159050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b600061199e82611969565b9050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156119dc5780820151818401526020810190506119c1565b838111156119eb576000848401525b50505050565b6000601f19601f830116905091905056fea265627a7a7230582041260293eaac4f90d6b56d49b12b6f452f5228846406cc772f87b622478922266c6578706572696d656e74616cf50037"

SERVER_ADDRESS = 'http://127.0.0.1:7545'
CONTRACT_ADDRESS = '0x2750475ea6c86dE2d2035A0F5eE208be1a786B85'
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
    def get_all_transaction(cls):
        cls.check_instances()
        transactions = list()
        for transaction_date in cls.contract.functions.getAllTransactionsDate().call():
            print(cls.contract.functions.getTransactionDetails(transaction_date).call())
            sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
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
            transaction = {'from': node_details.get('address'),
                           'gas': cls.contract.functions.sendData(node_address, cluster_header_address,
                                                                  data).estimateGas()}
            contract_data = cls.contract.functions.sendData(node_address, cluster_header_address,
                                                            data).buildTransaction(transaction)

            # Wait before perfomring the second transaction
            sleep(0.5)

            # Send built transaction
            cls.web3.eth.sendTransaction(contract_data)

            # Send received data from the cluster-header to the sink node
            transaction = {'from': cluster_header_address,
                           'gas': cls.contract.functions.sendData(cluster_header_address,
                                                                  cls.get_sink_node().get('address'),
                                                                  data).estimateGas()}
            new_contract_data = cls.contract.functions.sendData(cluster_header_address,
                                                                cls.get_sink_node().get('address'),
                                                                data).buildTransaction(transaction)
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
