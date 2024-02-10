from fastapi import FastAPI,Form
import utilClass
app = FastAPI()

ob = utilClass.sparseMat()  

@app.post("/insertMerchant")
async def insMer(pinCode : int= Form(...), merchID : str = Form(...)):
    ob.load_data()
    ob.insert_merchant(pinCode,merchID)
    ob.save_data()
    return {"result" : "successfully inserted"}

@app.post("/getMerchants")
async def getMer(pinCode : int= Form(...)):
    ob.load_data()
    a = ob.get_merchants(pinCode)
    if(a!=0):
        return  {str(pinCode):a}
    else:
        return {"error" : "pinCode DNE"}

@app.post("/delDB")
async def delDB(): 
    ob.load_data()
    ob.delete_json()
    return {"result" : "successfully deleted the database"}

@app.post("/delMerchant")
async def insMer(pinCode : int= Form(...), merchID : str = Form(...)):
    ob.load_data()
    a = ob.delete_merchant(pinCode,merchID)
    if(a!=0):
        ob.save_data()
        return {"result" : "successfully deleted"}
    else:
        return {"error" : "wrong input data"}