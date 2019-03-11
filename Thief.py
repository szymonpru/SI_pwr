class Thief():
    def __init__(self, capasity_of_knapsack, min_speed, max_speed):
        self.capasity_of_knapsack = capasity_of_knapsack
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.visited_cities = []
        self.items_in_knapsack = []
        self.fitness = 0  # zysk - koszta(czas, ktory potrzebowalismy)
