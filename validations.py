# PC_CB_15 to PC_CB_20 To validate the request body send by client 
def validateRequestBody(requestBody):
    isValid = True
    # PC_CB_17 To validate weather the given payload is in list
    if(type(requestBody) is not list):
        isValid = False
        return isValid
    
    # PC_CB_18 validating the length of the list
    if(len(requestBody) ==0):
        isValid = False
    
    # PC_CB_19 to check if the role and content key present in payload
    for chat in requestBody:
        if(type(chat) is not dict):
            return False
        else:
            if(chat.get("role") == None or chat.get("content") == None):
                return False    
    return isValid