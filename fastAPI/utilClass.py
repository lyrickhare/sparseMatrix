import numpy as np
import json
import os
import random
import string

class sparseMat():
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.merch_to_ID = {}
        self.table = {}
        self.merch_ID = -1
        self.load_data()

    def load_data(self):
        '''In this function we would load our data from JSON file, and if the
            file is not present we would create a new dict'''

        if(os.path.exists("table.json")):
            self.table = json.load(open("table.json"))
        if(os.path.exists("merch_to_ID.json")):
            self.merch_to_ID = json.load(open("merch_to_ID.json"))
    
    def insert_merchant(self, pincode, merchant_name):
        '''In this function we would first find out the merchant ID corresponding to the merchant name
            If the merchant name is not found, we would allot a new ID in the increasing order.
            Then we would add the ID to the pincode.
            If the pincode is not present we would add it to our table, and then add the merchant ID'''
        if(merchant_name in self.merch_to_ID):
            self.merch_ID = self.merch_to_ID[merchant_name]
        else:
            self.merch_ID = len(self.merch_to_ID) + 1
            self.merch_to_ID[merchant_name] = len(self.merch_to_ID) + 1
        if((pincode in self.table)):
            self.table[pincode].append(self.merch_ID)
        
        else:
            self.table[pincode] = [self.merch_ID]

    def save_data(self):
        '''In this function, we would update our JSON files'''
        with open("merch_to_ID.json","w") as f:
            json.dump(self.merch_to_ID,f)
        
        with open("table.json","w") as f:
            json.dump(self.table,f)
    
    def get_merchants(self,pincode):
        '''In this function, we would retrieve all the merchant names for the given pincode'''
        merchants = [key for key, value in self.merch_to_ID.items() if value in self.table[str(pincode)]]
        return(merchants)
    
    def delete_json(self):
        '''This function is used to delete the created json files'''
        if(os.path.exists("table.json")):
            os.remove("table.json")
        if(os.path.exists("merch_to_ID.json")):
            os.remove("merch_to_ID.json")
