(function() {

    var db = {

        loadData: function(filter) {
            return $.grep(this.records, function(record) {
                return (!filter.Name || records.Name.indexOf(filter.Name) > -1)
                    && (filter.Type === undefined || client.Type === filter.Type)
                    && (!filter.Address || client.Address.indexOf(filter.Address) > -1)
                    && (!filter.AssetID || client.AssetID === filter.AssetID)
                    && (filter.Selected === undefined || client.Selected === filter.Selected);
            });
        },

        insertItem: function(insertingClient) {
            this.records.push(insertingClient);
        },

        updateItem: function(updatingClient) { },

        deleteItem: function(deletingClient) {
            var clientIndex = $.inArray(deletingClient, this.records);
            this.records.splice(clientIndex, 1);
        }

    };

    window.db = db;


    db.type = [
        { Name: "", Id: 0 },
        { Name: "Avatar", Id: 1 },
        { Name: "Furnature", Id: 2 },
        { Name: "NFT", Id: 3 },
        { Name: "Cosmetics", Id: 4 },
        { Name: "Makeup", Id: 5 }
    ];

    db.records =[
        {"AssetID":"A1001","Type":1,"Name":"Peldi","Address":"https://ipfs.io/ipfs/bafa","Selected":false},
        {"AssetID":"A1002","Type":2,"Name":"Upland","Address":"https://ipfs.io/ipfs/badd","Selected":true},
        {"AssetID":"B1001","Type":1,"Name":"Patata","Address":"https://ipfs.io/ipfs/afde","Selected":false},
        {"AssetID":"B1002","Type":3,"Name":"Val","Address":"ethereum:0xff8d23aa","Selected":false},
        {"AssetID":"B1003","Type":1,"Name":"gogo","Address":"https://ipfs.io/ipfs/58ff","Selected":false},
        {"AssetID":"D1005","Type":3,"Name":"dota","Address":"ethereum:0x87ac15ee","Selected":false},
        {"AssetID":"D1006","Type":4,"Name":"morek","Address":"https://ipfs.io/ipfs/dea8","Selected":false},
        {"AssetID":"D1007","Type":5,"Name":"lyca","Address":"https://ipfs.io/ipfs/90fa","Selected":false},
        {"AssetID":"D1008","Type":4,"Name":"berg","Address":"https://ipfs.io/ipfs/ce76","Selected":false}
        ];

}());