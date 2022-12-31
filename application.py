# Flask server for project 
# Taking in data from dao and posting to a mysql database correctly. 
# All these calls work- could add some more such as delete by name/driver_id, update by driver id etc 

# 

# https://stackoverflow.com/questions/48008184/method-object-is-not-json-serializable

from flask import Flask, url_for,request,redirect,abort,jsonify
from dao_f1driver import MyDAO as dao

app = Flask(__name__, static_url_path = "", static_folder = "staticpages")



@app.route("/")
def index():
    return "hello"

# Get all- working
@app.route('/drivers')
def getAll():
    returnall = dao.getAll()
    return jsonify(returnall)

# Find by id
@app.route('/drivers/<LastName>', methods = ["GET"])
def findById(LastName):
    foundDrivers =dao.findBySurname(LastName)
    #if len(foundDrivers) == 0:
     #   return jsonify([]),204
    return jsonify({LastName:foundDrivers})

#create is working
# curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\",\"Author\":\"Test\", \"Price\":1235}" http://127.0.0.1:5000/books
@app.route('/drivers', methods=['POST'])
def createdriver():
    data = ()
    newid= dao.create(data)
    return jsonify({"id":newid})


# update
# curl -X PUT -H "content-type:application/json" -d "{\"Title\":\"Sense and Sensibility\", \"Price\":999}" http://127.0.0.1:5000/books/2
@app.route('/drivers/<LastName>', methods = ["PUT"])
def updateBySurname(LastName):
   data = (("Red Bull",LastName))
   updated = dao.update(data)
   return jsonify({"id":updated})


# delete
# curl -X DELETE http://127.0.0.1:5000/books/5
@app.route('/drivers/<int:id>', methods = ['DELETE'])
def deleteById(id):
    remove = dao.delete(id)
    return jsonify({"id":remove})






if __name__ == "__main__":
    
    app.run(debug=True)