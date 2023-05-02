from flask import Flask,render_template,request,url_for,redirect
import gear

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        search = request.form["search"]
        gear.search(search)
        return render_template('home.html',lis = gear.lis)

@app.route("/result",methods=["GET","POST"])
def result():
    if request.method == "GET":
        return render_template("gear_json.html",result=gear.data)

    
if __name__ == "__main__":
    app.run(port=8080,debug=True)