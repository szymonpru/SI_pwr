import pandas as py
import numpy as np
import random
from Thief import Thief
from City import City
from Item import Item


def loader(file_name):
    f = open(file_name, "r")
    contents = f.readlines()
    temp = contents[2].split("\t")
    dimentions = int(temp[temp.__len__() - 1])

    temp = contents[3].split("\t")
    number_of_items = int(temp[temp.__len__() - 1])

    temp = contents[4].split("\t")
    capacity_of_knapsack = int(temp[temp.__len__() - 1])

    temp = contents[5].split("\t")
    min_speed = float(temp[temp.__len__() - 1])

    temp = contents[6].split("\t")
    max_speed = float(temp[temp.__len__() - 1])

    cities = []

    for i in range(dimentions):
        temp = contents[10 + i].split("\t")
        city_index = int(temp[0])
        cord_x = float(temp[1])
        cord_y = float(temp[2])

        city = City(city_index, cord_x, cord_y)
        cities.append(city)

    for i in range(number_of_items):
        temp = contents[11 + dimentions + i].split("\t")
        index = int(temp[0])
        reward = int(temp[1])
        weight = int(temp[2])
        city_index = int(temp[3])

        item = Item(index, reward, weight)

        for city_object in cities:
            if city_object.index == city_index:
                city_object.add_item(item)

    return cities, capacity_of_knapsack, min_speed, max_speed


def generate_first_thieves(capacity_of_knapsack, min_speed, max_speed, quantity_of_thieves):
    thieves=[]
    for i in range(0, quantity_of_thieves):
        thief = Thief(capacity_of_knapsack, min_speed, max_speed)
        thieves.append(thief)
    return thieves


quantity_of_thieves = 50
loader = loader("data/easy_0.ttp")
cities = loader[0]
generate_first_thieves(loader[1], loader[2], loader[3], quantity_of_thieves)

for city in cities:
    # print(str(city.index) + " -> " + str(city.cord_x) + " -> " + str(city.cord_y))
    for item in city.items:
        print(str(item.index) + " -> " + str(item.reward) + " -> " + str(item.weight) + " -> " + str(city.index))

# generujemy pierwsza populacje, generujemy daną pulę
# selekcja, biezeby najlepszych kandydatow do naszej reprodukcji - operator ruletki lub turniejowa
# krzyzowanie - bierzemy polowe z peirwszego i z drugiego i tworzymy dwa nowe osobniki. Naprawiamy genotyp!! OX, CX, PMX
# miejsce krzyzowania losujemy - np. z jednego bierzemy 6, a z drugiego 44 miasta.
# mutacja potomstwa - bierzemy randomowo dwa miasta i zamieniamy je miejscami!
# Px [0,5 ; 1]
# Pm [0,01; 0,1]
