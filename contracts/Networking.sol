pragma experimental ABIEncoderV2;

contract Networking {

    struct Node {
        address nodeAddress;
        uint256 cluster;
    }

    // Date is considered as the transaction id
    struct Data {
        address sender;
        address receiver;
        uint256 date;
        string data;
    }

    uint256 public clustersCounter;
    Node[] public nodes;
    Data[] transactions;
    address sink_node_address;

    /*
        @Param clusters => Each cluster must be associated with a node
        clusters variable will have duplicated values
        mapping is not supported as parameter for constructor
        @Param nodes_addresses => Nodes addresses container
    */
    constructor(address[] memory nodes_addresses, uint256[] memory clusters, address sink_node, uint256 _clustersCounter) public {
        clustersCounter = _clustersCounter;
        sink_node_address = sink_node;
        for( uint256 i=0; i < nodes_addresses.length; i++ ) {
            nodes.push(Node({
                nodeAddress: nodes_addresses[i],
                cluster: clusters[i]
            }));
        }
    }

    /*
        Get sink node
    */
    function getSinkNode() view public returns (address) {
        return sink_node_address;
    }

    /*
        Compare two string variables
    */
     function compare(string memory _a, string memory _b) public returns (int) {
        bytes memory a = bytes(_a);
        bytes memory b = bytes(_b);
        uint minLength = a.length;
        if (b.length < minLength) minLength = b.length;
        //@todo unroll the loop into increments of 32 and do full 32 byte comparisons
        for (uint i = 0; i < minLength; i ++)
            if (a[i] < b[i])
                return -1;
            else if (a[i] > b[i])
                return 1;
        if (a.length < b.length)
            return -1;
        else if (a.length > b.length)
            return 1;
        else
            return 0;
    }

    /*
        Compare two string variables
    */
    function equal(string memory _a, string memory _b) public returns (bool) {
        return compare(_a, _b) == 0;
    }

    /*
        Send data
    */
    function sendData(address _sender, address _receiver, string memory _data) public {
        transactions.push(Data({
            sender: _sender,
            receiver: _receiver,
            date: block.timestamp,
            data: _data
        }));
    }

    /*
        Send data
    */
    function sendDataToSinkNode(address _cluster_header, string memory _data) public {
        transactions.push(Data({
            sender: _cluster_header,
            receiver: sink_node_address,
            date: block.timestamp,
            data: _data
        }));
    }

    /*
        Retrieve transactions count
    */
    function getTransactionsCount(address node_address) view public returns (int) {
        int count = 0;
        for( uint256 i = 0; i < transactions.length; i++ ) {
            if( transactions[i].sender == node_address || transactions[i].receiver == node_address ) {
                count += 1;
            }
        }
        return count;
    }

    /*
        Retrieve sink node received transactions count
    */
    function getSinkNodeTransactionsCount() view public returns (int) {
        int count = 0;
        for( uint256 i = 0; i < transactions.length; i++ ) {
            if( transactions[i].sender == sink_node_address || transactions[i].receiver == sink_node_address ) {
                count += 1;
            }
        }
        return count;
    }

    /*
        Retrieve global transactions count to check if a sink node need to receive data from any cluster-header
    */
    function getGlobalTransactionsCount() view public returns (int) {
        int count = 0;
        for( uint256 i = 0; i < transactions.length; i++ ) {
            count += 1;
        }
        return count;
    }

    /*
        Get data of a given one
    */
    function getNodeDetails(address _nodeAddress) view public returns (address, uint256) {
        string[] memory node_details = new string[](2);
        for( uint256 i = 0; i < nodes.length; i++ ) {
            if( nodes[i].nodeAddress == _nodeAddress ) {
                return( nodes[i].nodeAddress, nodes[i].cluster);
            }
        }
    }

    /*
        Retrieve nodes of a given cluster
    */
    function getClusterNodesAddresses(uint256 _cluster) view public returns (address[] memory local_addresses) {
        uint256 size = 0;
        // Get array size
        for( uint256 i = 0; i < nodes.length; i++ ) {
            if( nodes[i].cluster == _cluster ) {
                size++;
            }
        }
        address[] memory local_addresses = new address[](size);
        uint256 counter = 0;
        for( uint256 i = 0; i < nodes.length; i++ ) {
            if( nodes[i].cluster == _cluster ) {
                local_addresses[counter] = nodes[i].nodeAddress;
                counter++;
            }
        }
        return local_addresses;
    }

    /*
        Retrieve transactions date as an id of a given node
    */
    function getTransactionsDate(address _node) view public returns (uint256[] memory) {
        uint256 size = 0;
        // Get array size
        for( uint256 i = 0; i < transactions.length; i++ ) {
            if( transactions[i].sender == _node || transactions[i].receiver == _node ) {
                size++;
            }
        }
        uint256[] memory local_data = new uint256[](size);
        uint256 counter = 0;
        for( uint256 i = 0; i < transactions.length; i++ ) {
            if( transactions[i].sender == _node || transactions[i].receiver == _node ) {
                local_data[counter] = transactions[i].date;
                counter++;
            }
        }
        return local_data;
    }

     /*
        Retrieve transactions date as an id
    */
    function getAllTransactionsDate() view public returns (uint256[] memory) {
        uint256[] memory local_data = new uint256[](transactions.length);
        uint256 counter = 0;
        for( uint256 i = 0; i < transactions.length; i++ ) {
            local_data[counter] = transactions[i].date;
            counter++;
        }
        return local_data;
    }

    /*
        Retrieve transactions details of a given date considered as the id
    */
    function getTransactionDetails(uint _date) public returns (address, address, uint256, string memory) {
        for( uint256 i = 0; i < transactions.length; i++ ) {
            if( transactions[i].date == _date ) {
                return (transactions[i].sender, transactions[i].receiver, transactions[i].date, transactions[i].data);
            }
        }
    }

    /*
        Retrieve number of clusters
    */
    function getClustersCounters() view public returns (uint256) {
        return clustersCounter;
    }






















}