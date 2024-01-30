import numpy as np
class sparseMatrix:
    def __init__(self, totalPinCodes):
        self.tpc = totalPinCodes
        self.spMatArr = np.empty(shape=[self.tpc,],dtype=object)
    def pinToIndex(self,pincode):
        return pincode
    def insMerchant(self,pinCode,merID):
        self.spMatArr[pinCode] = np.append(self.spMatArr[pinCode],[merID])        
    def getMerchants(self,pinCode):
        return self.spMatArr[pinCode]