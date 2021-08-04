from flask import Flask,jsonify,request
app = Flask(__name__)
contacts = [
    {
        'id':1,
        'Contact':u'1234567890',
        'Name':u'Rithu',
        'done':False
    },
    {
        'id':2,
        'Contact':u'1234567899',
        'Name':u'abcdef',
        'done':False
    }
]
@app.route('/')
def helloWorld():
    return "HELLO"
@app.route('/add-data',methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the data'
        },400)
    contact = {
        'id':contacts[-1]['id'] + 1,
        'Contact':request.json['Contact'],
        'Name':request.json.get('Name',''),
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        'status':'success',
        'message':'Contact added successfully'
    })
@app.route('/get-data')
def getData():
    return jsonify({
        'data':contacts
    })
if (__name__ == '__main__'):
    app.run(debug=True)