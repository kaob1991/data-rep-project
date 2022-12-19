# Temp restful api for project 

# This is working but need to change the books etc. We don't need them in here as we are going to link to a database instead. 

# API's are working however 



from flask import Flask, url_for,request,redirect,abort,jsonify

app = Flask(__name__, static_url_path = "", static_folder = "staticpages")

books = [
    {"id":1, "Title":"How to build a racecar", "Author": "Newey", "Price": 1000},
    {"id":2, "Title":"Pride and Prejudice", "Author": "Austin", "Price": 1500},
    {"id":3, "Title":"Oliver Twist", "Author": "Dickens", "Price": 3000},
    {"id":4, "Title":"Automate the boring stuff", "Author": "Sweigart", "Price": 1300},

]

nextId=5



@app.route("/")
def index():
    return "hello"

# Get all
@app.route('/books')
def getAll():
    return jsonify(books)

# Find by id
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify([]),204
    return jsonify(foundBooks[0])

#create
# curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\",\"Author\":\"Test\", \"Price\":1235}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def createBook():
    global nextId
    if not request.json:
        abort (400)


    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "price":request.json["Price"]

    }
    books.append(book)
    nextId += 1
    return jsonify(book)


# update
# curl -X PUT -H "content-type:application/json" -d "{\"Title\":\"Sense and Sensibility\", \"Price\":999}" http://127.0.0.1:5000/books/2
@app.route('/books/<int:id>', methods = ["PUT"])
def updateById(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify([]),404
    currentBook = foundBooks[0]
    if "Title" in request.json:
        currentBook["Title"] = request.json["Title"]
    if "Author" in request.json:
        currentBook["Author"] = request.json["Author"]
    if "Price" in request.json:
        currentBook["Price"] = request.json["Price"]

    return jsonify(currentBook)
# delete
# curl -X DELETE http://127.0.0.1:5000/books/5
@app.route('/books/<int:id>', methods = ['DELETE'])
def deleteById(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify([]),404
    books.remove(foundBooks[0])
    return jsonify({"done":True})






if __name__ == "__main__":
    
    app.run(debug=True)