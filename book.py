class Book:
    def __init__(self, id, title, stock):
        self.id = id
        self.title = title
        self.stock = stock

    def __str__(self) -> str:
        return
        "{},{},{}".format(self.id,self.title,self.stock)