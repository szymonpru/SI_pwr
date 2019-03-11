class City():
    def __init__(self,index, cord_x, cord_y):
        self.index=index
        self.cord_x=cord_x
        self.cord_y=cord_y
        self.items=[]

    def add_item(self, item):
        self.items.append(item)