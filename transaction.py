class Transaction:
    def __init__(self, id, customerid, name, title, points, duedate):
        self.id = id
        self.customerid = customerid
        self.name = name
        self.title = title
        self.points = points
        self.duedate = duedate
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.id,self.customerid,self.name,self.title,self.points,self.duedate)