import os
from datetime import datetime

from web3 import Web3

from WSN.settings import CONTRACT_ADDRESS, SERVER_ADDRESS

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
				"name": "_cluster_header",
				"type": "address"
			},
			{
				"name": "_data",
				"type": "string"
			},
			{
				"name": "_date",
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
				"name": "local_data",
				"type": "string[]"
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
			},
			{
				"name": "_date",
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
		"constant": false,
		"inputs": [
			{
				"name": "_date",
				"type": "string"
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
				"type": "string"
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

full_byte_code = "60806040523480156200001157600080fd5b5060405162002025380380620020258339810180604052620000379190810190620002ce565b8060008190555081600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008090505b84518110156200017957600160408051908101604052808784815181101515620000ab57fe5b9060200190602002015173ffffffffffffffffffffffffffffffffffffffff1681526020018684815181101515620000df57fe5b906020019060200201518152509080600181540180825580915050906001820390600052602060002090600202016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010155505050808060010191505062000085565b50505050506200042a565b60006200019282516200040c565b905092915050565b600082601f8301121515620001ae57600080fd5b8151620001c5620001bf826200039a565b6200036c565b91508181835260208401935060208101905083856020840282011115620001eb57600080fd5b60005b838110156200021f578162000204888262000184565b845260208401935060208301925050600181019050620001ee565b5050505092915050565b600082601f83011215156200023d57600080fd5b8151620002546200024e82620003c3565b6200036c565b915081818352602084019350602081019050838560208402820111156200027a57600080fd5b60005b83811015620002ae5781620002938882620002b8565b8452602084019350602083019250506001810190506200027d565b5050505092915050565b6000620002c6825162000420565b905092915050565b60008060008060808587031215620002e557600080fd5b600085015167ffffffffffffffff8111156200030057600080fd5b6200030e878288016200019a565b945050602085015167ffffffffffffffff8111156200032c57600080fd5b6200033a8782880162000229565b93505060406200034d8782880162000184565b92505060606200036087828801620002b8565b91505092959194509250565b6000604051905081810181811067ffffffffffffffff821117156200039057600080fd5b8060405250919050565b600067ffffffffffffffff821115620003b257600080fd5b602082029050602081019050919050565b600067ffffffffffffffff821115620003db57600080fd5b602082029050602081019050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006200041982620003ec565b9050919050565b6000819050919050565b611beb806200043a6000396000f3fe6080604052600436106100d5576000357c010000000000000000000000000000000000000000000000000000000090048063026bfd93146100da5780630bdd71b3146101055780631c53c2801461012e5780631f2cb6e11461016c5780632fea6afb146101975780633a96fdd7146101c257806346bdca9a146101ff57806349cb3ec51461023c57806364a0aec8146102795780638d22fa10146102b6578063bafb3581146102df578063bca5f8f51461031d578063d6345e6f14610348578063e4daff8f14610385578063ff0b073d146103c5575b600080fd5b3480156100e657600080fd5b506100ef6103f0565b6040516100fc9190611a01565b60405180910390f35b34801561011157600080fd5b5061012c60048036036101279190810190611645565b610554565b005b34801561013a57600080fd5b5061015560048036036101509190810190611771565b6106c1565b604051610163929190611979565b60405180910390f35b34801561017857600080fd5b50610181610714565b60405161018e919061190b565b60405180910390f35b3480156101a357600080fd5b506101ac61073e565b6040516101b99190611a1c565b60405180910390f35b3480156101ce57600080fd5b506101e960048036036101e49190810190611705565b610747565b6040516101f69190611a01565b60405180910390f35b34801561020b57600080fd5b5061022660048036036102219190810190611705565b610a0d565b60405161023391906119e6565b60405180910390f35b34801561024857600080fd5b50610263600480360361025e9190810190611589565b610a23565b60405161027091906119c4565b60405180910390f35b34801561028557600080fd5b506102a0600480360361029b9190810190611771565b610c57565b6040516102ad91906119a2565b60405180910390f35b3480156102c257600080fd5b506102dd60048036036102d891908101906115b2565b610d79565b005b3480156102eb57600080fd5b5061030660048036036103019190810190611589565b610ec5565b604051610314929190611979565b60405180910390f35b34801561032957600080fd5b5061033261100b565b60405161033f9190611a01565b60405180910390f35b34801561035457600080fd5b5061036f600480360361036a9190810190611589565b611040565b60405161037c9190611a01565b60405180910390f35b34801561039157600080fd5b506103ac60048036036103a791908101906116c4565b611162565b6040516103bc9493929190611926565b60405180910390f35b3480156103d157600080fd5b506103da611460565b6040516103e79190611a1c565b60405180910390f35b6000806000905060008090505b60028054905081101561054c57600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1660028281548110151561045257fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614806105335750600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166002828154811015156104e957fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b1561053f576001820191505b80806001019150506103fd565b508091505090565b60026080604051908101604052808573ffffffffffffffffffffffffffffffffffffffff168152602001600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001838152602001848152509080600181540180825580915050906001820390600052602060002090600402016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550604082015181600201908051906020019061069b929190611466565b5060608201518160030190805190602001906106b8929190611466565b50505050505050565b6001818154811015156106d057fe5b90600052602060002090600202016000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010154905082565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054905090565b600060608390506060839050600082519050808251101561076757815190505b60008090505b818110156109b357828181518110151561078357fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191684828151811015156107fe57fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916101561089d577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff945050505050610a07565b82818151811015156108ab57fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916848281518110151561092657fe5b9060200101517f010000000000000000000000000000000000000000000000000000000000000090047f0100000000000000000000000000000000000000000000000000000000000000027effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191611156109a6576001945050505050610a07565b808060010191505061076d565b508151835110156109e9577fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9350505050610a07565b8151835111156109ff5760019350505050610a07565b600093505050505b92915050565b600080610a1a8484610747565b14905092915050565b6060600280549050604051908082528060200260200182016040528015610a5e57816020015b6060815260200190600190039081610a495790505b509050600080905060008090505b600280549050811015610c4d578373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610a9f57fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161480610b5e57508373ffffffffffffffffffffffffffffffffffffffff16600282815481101515610b1457fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610c4057600281815481101515610b7257fe5b90600052602060002090600402016002018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610c175780601f10610bec57610100808354040283529160200191610c17565b820191906000526020600020905b815481529060010190602001808311610bfa57829003601f168201915b50505050508383815181101515610c2a57fe5b9060200190602002018190525081806001019250505b8080600101915050610a6c565b5081915050919050565b6060806028604051908082528060200260200182016040528015610c8a5781602001602082028038833980820191505090505b509050600080905060008090505b600180549050811015610d6e5784600182815481101515610cb557fe5b9060005260206000209060020201600101541415610d6157600181815481101515610cdc57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168383815181101515610d1c57fe5b9060200190602002019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505081806001019250505b8080600101915050610c98565b508192505050919050565b60026080604051908101604052808673ffffffffffffffffffffffffffffffffffffffff1681526020018573ffffffffffffffffffffffffffffffffffffffff168152602001838152602001848152509080600181540180825580915050906001820390600052602060002090600402016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002019080519060200190610e9e929190611466565b506060820151816003019080519060200190610ebb929190611466565b5050505050505050565b60008060606002604051908082528060200260200182016040528015610eff57816020015b6060815260200190600190039081610eea5790505b50905060008090505b600180549050811015611003578473ffffffffffffffffffffffffffffffffffffffff16600182815481101515610f3b57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610ff657600181815481101515610f9857fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600182815481101515610fd957fe5b906000526020600020906002020160010154935093505050611006565b8080600101915050610f08565b50505b915091565b6000806000905060008090505b600280549050811015611038576001820191508080600101915050611018565b508091505090565b6000806000905060008090505b600280549050811015611158578373ffffffffffffffffffffffffffffffffffffffff1660028281548110151561108057fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16148061113f57508373ffffffffffffffffffffffffffffffffffffffff166002828154811015156110f557fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b1561114b576001820191505b808060010191505061104d565b5080915050919050565b60008060608060008090505b6002805490508110156114575761123d60028281548110151561118d57fe5b90600052602060002090600402016002018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156112325780601f1061120757610100808354040283529160200191611232565b820191906000526020600020905b81548152906001019060200180831161121557829003601f168201915b505050505087610a0d565b1561144a5760028181548110151561125157fe5b906000526020600020906004020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1660028281548110151561129257fe5b906000526020600020906004020160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166002838154811015156112d357fe5b90600052602060002090600402016002016002848154811015156112f357fe5b9060005260206000209060040201600301818054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156113995780601f1061136e57610100808354040283529160200191611399565b820191906000526020600020905b81548152906001019060200180831161137c57829003601f168201915b50505050509150808054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156114355780601f1061140a57610100808354040283529160200191611435565b820191906000526020600020905b81548152906001019060200180831161141857829003601f168201915b50505050509050945094509450945050611459565b808060010191505061116e565b505b9193509193565b60005481565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106114a757805160ff19168380011785556114d5565b828001600101855582156114d5579182015b828111156114d45782518255916020019190600101906114b9565b5b5090506114e291906114e6565b5090565b61150891905b808211156115045760008160009055506001016114ec565b5090565b90565b60006115178235611b42565b905092915050565b600082601f830112151561153257600080fd5b813561154561154082611a64565b611a37565b9150808252602083016020830185838301111561156157600080fd5b61156c838284611b5e565b50505092915050565b60006115818235611b54565b905092915050565b60006020828403121561159b57600080fd5b60006115a98482850161150b565b91505092915050565b600080600080608085870312156115c857600080fd5b60006115d68782880161150b565b94505060206115e78782880161150b565b935050604085013567ffffffffffffffff81111561160457600080fd5b6116108782880161151f565b925050606085013567ffffffffffffffff81111561162d57600080fd5b6116398782880161151f565b91505092959194509250565b60008060006060848603121561165a57600080fd5b60006116688682870161150b565b935050602084013567ffffffffffffffff81111561168557600080fd5b6116918682870161151f565b925050604084013567ffffffffffffffff8111156116ae57600080fd5b6116ba8682870161151f565b9150509250925092565b6000602082840312156116d657600080fd5b600082013567ffffffffffffffff8111156116f057600080fd5b6116fc8482850161151f565b91505092915050565b6000806040838503121561171857600080fd5b600083013567ffffffffffffffff81111561173257600080fd5b61173e8582860161151f565b925050602083013567ffffffffffffffff81111561175b57600080fd5b6117678582860161151f565b9150509250929050565b60006020828403121561178357600080fd5b600061179184828501611575565b91505092915050565b6117a381611af0565b82525050565b60006117b482611aaa565b8084526020840193506117c683611a90565b60005b828110156117f8576117dc86835161179a565b6117e582611ad6565b91506020860195506001810190506117c9565b50849250505092915050565b600061180f82611ab5565b8084526020840193508360208202850161182885611a9d565b60005b848110156118615783830388526118438383516118c6565b925061184e82611ae3565b915060208801975060018101905061182b565b508196508694505050505092915050565b61187b81611b02565b82525050565b61188a81611b0e565b82525050565b600061189b82611acb565b8084526118af816020860160208601611b6d565b6118b881611ba0565b602085010191505092915050565b60006118d182611ac0565b8084526118e5816020860160208601611b6d565b6118ee81611ba0565b602085010191505092915050565b61190581611b38565b82525050565b6000602082019050611920600083018461179a565b92915050565b600060808201905061193b600083018761179a565b611948602083018661179a565b818103604083015261195a8185611890565b9050818103606083015261196e8184611890565b905095945050505050565b600060408201905061198e600083018561179a565b61199b60208301846118fc565b9392505050565b600060208201905081810360008301526119bc81846117a9565b905092915050565b600060208201905081810360008301526119de8184611804565b905092915050565b60006020820190506119fb6000830184611872565b92915050565b6000602082019050611a166000830184611881565b92915050565b6000602082019050611a3160008301846118fc565b92915050565b6000604051905081810181811067ffffffffffffffff82111715611a5a57600080fd5b8060405250919050565b600067ffffffffffffffff821115611a7b57600080fd5b601f19601f8301169050602081019050919050565b6000602082019050919050565b6000602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b6000602082019050919050565b6000611afb82611b18565b9050919050565b60008115159050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b6000611b4d82611b18565b9050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015611b8b578082015181840152602081019050611b70565b83811115611b9a576000848401525b50505050565b6000601f19601f830116905091905056fea265627a7a72305820ae000032a91a494841144293b9eadc877bfea36ca2791bd5714b17401dc4c02f6c6578706572696d656e74616cf50037"

SERVER_ADDRESS = 'http://127.0.0.1:7545'
CONTRACT_ADDRESS = '0xa811CA0B5580CAE728313eAa9c55B5620a6A70c8'


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
        transactions_dates = cls.contract.functions.getTransactionsDate(node).call()
        transactions = list()
        for transaction_date in transactions_dates:
            sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
            if sender != '0x0000000000000000000000000000000000000000' and receiver != '0x0000000000000000000000000000000000000000':
                transactions.append(
                    Transaction(sender, receiver, datetime.fromtimestamp(float(date)), data))
        return transactions

    # Check if a node is the sink one
    @classmethod
    def check_sink_node(cls, node):
        print(str(cls.get_sink_node().get('address')))
        print(node)
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
        # Get number of clusters
        clusters_counter = cls.contract.functions.getClustersCounters().call()
        clusters = [i for i in range(0, clusters_counter)]
        transactions = list()
        for cluster in clusters:
            local_nodes = [node for node in cls.contract.functions.getClusterNodesAddresses(cluster).call() if
                           node != '0x0000000000000000000000000000000000000000']
            for node in local_nodes:
                transactions_dates_ids = [transaction_id for transaction_id in
                                          cls.contract.functions.getTransactionsDate(node).call() if
                                          transaction_id != '']
                for transaction_date in transactions_dates_ids:
                    sender, receiver, date, data = cls.contract.functions.getTransactionDetails(transaction_date).call()
                    if sender != '0x0000000000000000000000000000000000000000' and receiver != '0x0000000000000000000000000000000000000000':
                        transactions.append(Transaction(sender, receiver, datetime.fromtimestamp(float(date)), data))
        return transactions

    # Send data to the cluster header
    @classmethod
    def send_data_to_cluster_header(cls, node_address, data):
        cls.check_instances()
        node_details = cls.contract.functions.getNodeDetails(node_address).call()
        cluster = node_details.get('address')

    # Retrieve cluster-header for a given cluster
    @classmethod
    def get_cluster_header(cls, cluster):
        cluster_nodes = [node for node in cls.contract.functions.getClusterNodesAddresses(cluster).call() if
                         node != '0x0000000000000000000000000000000000000000']
        cluster_nodes_balances = list()
        for account in cluster_nodes:
            if type(account) is not str:
                account = account[0]
            print(account)
            #cluster_nodes.append((account, cls.web3.eth.getBalance(account)))
        print(cluster_nodes_balances)
        # cluster_header = sorted(cluster_nodes_balances, key=lambda line : line[1])[0]
        # print(cluster_header)