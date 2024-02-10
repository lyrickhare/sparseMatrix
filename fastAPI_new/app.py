from fastapi import FastAPI,Form
import utilClass
app = FastAPI()

ob = utilClass.sparseMat()  

@app.post("/insertMerchant")
async def insMer(pinCode : int= Form(...), merchID : int = Form(...)):
    ob.insert_merchant(pinCode,merchID)
    ob.save_data()
    return {"result" : "successfully inserted"}

@app.post("/getMerchants")
async def getMer(pinCode : int= Form(...)):
    a = ob.get_merchants(pinCode)
    if(a!=0):
        return  {str(pinCode):a}
    else:
        return {"error" : "pinCode DNE"}

@app.post("/delDB")
async def delDB(): 
    ob.delete_json()
    return {"result" : "successfully deleted the database"}

@app.post("/delMerchant")
async def insMer(pinCode : int= Form(...), merchID : int = Form(...)):
    a = ob.delete_merchant(pinCode,merchID)
    if(a!=0):
        return {"result" : "successfully deleted"}
        ob.save_data()
    else:
        return {"error" : "wrong input data"}