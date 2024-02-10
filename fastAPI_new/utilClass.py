import json
import os

class sparseMat():
    def __init__(self):
        self.merch_to_ID = {}
        self.table = {}
        self.merch_ID = -1
        self.temp = {}
        self.load_data()

    def load_data(self):
        '''In this function we would load our data from JSON file, and if the
            file is not present we would create a new dict'''
        if(os.path.exists("table.json")):
            self.table = json.load(open("table.json"))
            
        if(os.path.exists("merch_to_ID.json")):
            self.merch_to_ID = json.load(open("merch_to_ID.json"))
            self.temp = dict((v,k) for k,v in self.merch_to_ID.items())
    
    def insert_merchant(self, pincode, merchant_identification):
        '''In this function we would first find out the merchant ID corresponding to the merchant name
        If the merchant name is not found, we would allot a new ID in the increasing order.
        Then we would add the ID to the pincode.
        If the pincode is not present we would add it to our table, and then add the merchant ID'''

        try:
            self.merch_ID = self.merch_to_ID[str(merchant_identification)]
            self.temp[self.merch_ID] = merchant_identification
        except:
            if(len(self.temp) == 0):
                next_ID = 0
            else:
                next_ID = max(self.temp) + 1
            self.merch_ID = next_ID
            self.merch_to_ID[str(merchant_identification)] = self.merch_ID
            self.temp[self.merch_ID] = merchant_identification
        
        try:
            self.table[str(pincode)].append(self.merch_ID)
            self.table[str(pincode)] = list(set(self.table[str(pincode)]))
        except:
            self.table[str(pincode)] = [self.merch_ID]

    def save_data(self):
        '''In this function, we would update our JSON files'''
        with open("merch_to_ID.json","w") as f:
            json.dump(self.merch_to_ID,f)
        
        with open("table.json","w") as f:
            json.dump(self.table,f)
    
    def get_merchants(self,pincode):
        try:
            merchants = [self.temp[value] for value in self.table[str(pincode)]]
            return((merchants))
        except KeyError:
            return(0)
    
    def delete_json(self):
        '''This function is used to delete the created json files'''
        self.merch_to_ID = {}
        self.table = {}
        self.temp = {}
        if(os.path.exists("table.json")):
            os.remove("table.json")
        if(os.path.exists("merch_to_ID.json")):
            os.remove("merch_to_ID.json")

    def delete_merchant(self,pincode,merchant_identification):
        try:
            self.merch_ID = self.merch_to_ID[str(merchant_identification)]
        except:
            return(0)
        if(pincode == -1):
            del self.temp[self.merch_ID]
            del self.merch_to_ID[str(merchant_identification)]
            for i in self.table.values():
                if self.merch_ID in i:
                    i.remove(self.merch_ID)
            return(1)
        try:
            self.table[str(pincode)].remove(self.merch_ID)
        except:
            return(0)
        return(1)