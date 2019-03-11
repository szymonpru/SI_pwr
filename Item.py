class Item():
    def __init__(self,index, reward, weight):
        self.index=index
        self.reward=reward
        self.weight=weight
        self.profitability=reward/weight
