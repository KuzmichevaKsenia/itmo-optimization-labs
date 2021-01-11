import random


class Specimen:
    paths = [[0, 4, 5, 3, 8],
             [4, 0, 7, 6, 8],
             [5, 7, 0, 7, 9],
             [3, 6, 7, 0, 9],
             [8, 8, 9, 9, 0]]

    genome = []
    weight = 0

    def __init__(self, genome):
        self.genome = genome
        self.update_weight()

    def __str__(self):
        return str({'genome': self.genome, 'weight': self.weight})

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def update_weight(self):
        self.weight = 0
        for i in range(len(self.genome) - 1):
            self.weight += Specimen.paths[self.genome[i]][self.genome[i + 1]]

    def crossing(self, partner):
        parent1 = self.genome[1:len(self.genome)-1]
        parent2 = partner.genome[1:len(self.genome)-1]

        def remove_same_elms(elms_to_remove, list_to_clean):
            for elem in elms_to_remove:
                while elem in list_to_clean:
                    list_to_clean.remove(elem)
            return list_to_clean

        length = len(parent1)
        point1 = length // 3
        point2 = length - point1
        elms_to_offspring1 = remove_same_elms(parent1[point1:point2], parent2[point2:] + parent2[:point2])
        elms_to_offspring2 = remove_same_elms(parent2[point1:point2], parent1[point2:] + parent1[:point2])
        offspring1 = Specimen([self.genome[0]] + elms_to_offspring1[:point1] + parent1[point1:point2] + elms_to_offspring1[point1:] + [self.genome[0]])
        offspring2 = Specimen([self.genome[0]] + elms_to_offspring2[:point1] + parent2[point1:point2] + elms_to_offspring2[point1:] + [self.genome[0]])
        return offspring1, offspring2

    def mutation(self, probability):
        for i in range(1, len(self.genome) - 2):
            for j in range(2, len(self.genome) - 1):
                if probability > random.random():
                    self.genome[i], self.genome[j] = self.genome[j], self.genome[i]
