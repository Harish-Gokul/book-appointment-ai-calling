# PC_CB_1 - PC_CB_3 - Importing classes and function from flask, controller, flask_cors
from flask import Flask,request
from controller import sendChatRequest
from flask_cors import CORS

# PC_CB_4 to PC_CB_5 - Create an instance for flask and invoking CORS by pass app as object 
app = Flask(__name__)
CORS(app)

# PC_CB_8 - PC_CB_11 - to handle request with /chatbot as endpoint
@app.route("/bookappointment",methods=["POST"])
def handleChatRequest():
    payload = request.get_json()
    return sendChatRequest(payload)

# PC_CB_6 to PC_CB_7 -  call app.run only if this file is executed
if(__name__ == "__main__"):
    app.run(port=10000,host="0.0.0.0")
