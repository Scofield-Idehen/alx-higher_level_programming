#!/usr/bin/python3
def weight_average(my_list=[]):
    score = sum([weight[1] * weight[0] for weight in my_list])
    weight = sum([weight[1] for weight in my_list]) or 1
    return score / weight
