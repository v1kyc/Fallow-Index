import random

def pseudo_sample(population, k):
    return random.sample(population, k)

def true_sample(population, k):
    return 0