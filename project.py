from flask import Flask,request,jsonify
app=Flask(__name__)
#@app.route("/")
tasks=[{
    "id":1,
    "contact":"6783976386",
    "name":"hitarth",
    "done":False
    
},
{
    "id":2 ,
    "contact":"7893758357",
    "name":"nagar",
    "done":False
}]

@app.route("/add-data",methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    task={
        "id":tasks[-1]['id'],
        "contact":request.json.get("contact",""),
        "name":request.json['name'],
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task is completed successfully"
    })
@app.route("/get-data")
def get_data():
    return jsonify({
        "data":tasks
    })
if (__name__=="__main__"):
    app.run(debug=True)