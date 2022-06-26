class Customer:
    def __init__(self, id, salutation, name, address, points):
        self.id = id
        self.salutation = salutation
        self.name = name
        self.address = address
        self.points = points

    def __str__(self) -> str:
        return
        "{},{},{},{},{}".format(self.id,self.salutation,self.name,self.address,self.points)