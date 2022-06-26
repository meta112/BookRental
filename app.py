from flask import Flask, render_template, request, redirect, url_for, flash
#from sqlitedb import dbconnection
from customer import Customer
from book import Book
from transaction import Transaction
from postgresdb import dbconnection


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


#@app.route("/addrental")
#def addrental():
    

@app.route("/transactions")
def transactions():
    return render_template("transactions.html")

@app.route("/viewtransaction")
def viewtran():
    try:
        trans = []
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select r.id, c.id, c.name, b.title, c.point, r.due from customer c, book b, rental r where c.id = r.customerid and b.id = r.bookid")
        rows = cur.fetchall()
        for row in rows:
            tran = Transaction(row[0],row[1],row[2],row[3],row[4],row[5])
            trans.append(tran)

    except Exception as e:
        print(e)
    finally:
        print("data returned")
        return render_template("viewtransaction.html", trans=trans)

@app.route("/edittransaction")
def edittran():
    return render_template("edittransaction.html")

@app.route("/newbook")
def newbook():
    return render_template("newbook.html")

@app.route("/addbook", methods = ["post"])
def addbook():
    try:
        title = request.form["title"]
        stock = request.form["stock"]

        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Book (title, stock) VALUES (%s, %s)", (title, stock))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        return redirect("/viewbooks")

@app.route("/viewbooks")
def viewbooks():
    
    try:
        books = []
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select * from book")
        rows = cur.fetchall()
        for row in rows:
            book = Book(row[0],row[1],row[2])
            books.append(book)
            
    except Exception as e:
        print(e)
    finally:
        print("data returned")
        return render_template("viewbooks.html",books=books)


@app.route("/editbook/<int:id>")
def editbook(id):
    try:
        print("starting edit book")
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select * from book where id=%s",(str(id),))
        row = cur.fetchone()
        if row:
            book = Book(row[0],row[1],row[2])
            
            return render_template("editbook.html",book=book)
        else:
            print("no data matching id")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@app.route("/updatebook", methods=["POST"])
def updatebook():
    try:
        title = request.form["title"]
        stock = request.form["stock"]
        id = request.form["id"]

        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("UPDATE Book set title=%s, stock=%s where id=%s",(title,stock,id))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        return redirect("/viewbooks")

@app.route("/newcustomer")
def newcustomer():
    return render_template("newcustomer.html")

@app.route("/addcustomer", methods = ["post"])
def addcustomer():
    try:
        salutation = request.form["salutation"]
        name = request.form["name"]
        address = request.form["address"]
        points = request.form["points"]

        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Customer (salutation, name, address, point) VALUES (%s,%s,%s,%s)", (salutation, name, address, points))
        conn.commit()
    except Exception as e:
        print(e)

    finally:
        return redirect("/viewcustomers")

@app.route("/viewcustomers")
def viewcustomers():
    try:
        customers = []
        conn = dbconnection()
        cur = conn.cursor()
        cur.execute("select * from customer")
        rows = cur.fetchall()
        for row in rows:
            customer = Customer(row[0],row[1],row[2],row[3],row[4])
            customers.append(customer)
            #print(customer)
    except Exception as e:
        print(e)
    finally:
        print("data returned")
        return render_template("viewcustomers.html",customers=customers)

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