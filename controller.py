from flask import request
from validations import validateRequestBody

def sendChatRequest(payload):
    
    if(  (type(payload) is not dict) or ("appointment_date" not in payload) or ("appointment_time" not in payload)):
        raise Exception(str(payload))
        return {"message": "check the paylaod"},400
    print(payload)
    return {"message": "Collected appointment details","data": payload},200
     
    
