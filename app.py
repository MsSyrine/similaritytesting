# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

# load the algo 
from cosine_similarity import cosine_similarity as cos

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # For debugging
#     print(f"welcome !")

#     return jsonify(data)

@app.route('/post/', methods=['POST'])
def post_something():

  
   a = []
   b = [] 
    # Retrieve users data from json post request
   data = request.get_json(force=True)

   user_a = data['usera']
   coord_xa = float(data['xa'])
   coord_ya = float(data['ya'])
   a = [ coord_xa,  coord_ya]
   #print(a)
   
   user_b = data['userb']
   coord_xb = float(data['xb'])
   coord_yb = float(data['yb'])
   b = [ coord_xb,  coord_yb]
   #print(b)
   #print(f"user 2 name {user_b}")

   sim = cos(a, b)
   print(sim)

   if sim:
        return jsonify({
            "Input request data": f"  User {user_a} of coordinates {a} and User {user_b} of coordinates {b} ",
            "Output": f" The Similarity is {sim}"

        })
   else:
        return jsonify({
            "ERROR"
        })



# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome!!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)