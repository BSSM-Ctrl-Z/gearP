from flask import Flask, render_template, request
import gear

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        search = request.form["search"]
        gear.search(search)
    return render_template("home.html", lis=gear.lis)

@app.route("/result")
def result():
    return render_template("gear_json.html", result=gear.data)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
