from flask import Flask, render_template, request, redirect, url_for, flash
from sqlitedb import dbconnection

app = Flask(__name__)

@app.route("/helloworld")
def helloworld():
    try:
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select * from customer")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)
    finally:
        print("data returned")

def test():
    print("test")
   

@app.route("/newrental")
def newrental():
    return render_template("newrental.html")

@app.route("/transactions")
def transactions():
    return render_template("transactions.html")

@app.route("/viewtransaction")
def viewtran():
    return render_template("viewtransaction.html")

@app.route("/edittransaction")
def edittran():
    return render_template("edittransaction.html")

@app.route("/newbook")
def newbook():
    return render_template("newbook.html")

@app.route("/viewbooks")
def viewbooks():
    return render_template("viewbooks.html")

@app.route("/editbook")
def editbook():
    return render_template("editbook.html")

@app.route("/newcustomer")
def newcustomer():
    return render_template("newcustomer.html")

@app.route("/viewcustomers")
def viewcustomers():
    try:
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select * from customer")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)
    finally:
        print("data returned")
        return render_template("viewcustomers.html")

@app.route("/editcustomer")
def editcustomer():
    return render_template("editcustomer.html")

@app.route("/")
def home():
    hello = "Hello "
    user = {"name":"Ryan"}
    return render_template("home.html", greeting = hello + user["name"])

if __name__ == "__main__":
    helloworld()