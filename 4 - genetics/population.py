class Population:
    mutation_probability = 0
    population_num = 0
    specimens = []

    def __init__(self, mutation_probability, population_num):
        Population.mutation_probability = mutation_probability
        Population.population_num = population_num

    def __str__(self):
        res = ""
        for s in self.specimens:
            res += str(s) + "\n"
        return res

    def next_generation(self):
        self.specimens.sort()
        new_specimens = []

        def doubled():
            return len(new_specimens) >= Population.population_num * 2

        for i in range(len(self.specimens)):
            for j in range(1, len(self.specimens) - 1):
                s1, s2 = self.specimens[i].crossing(self.specimens[j])
                s1.mutation(Population.mutation_probability)
                s2.mutation(Population.mutation_probability)
                new_specimens.append(s1)
                new_specimens.append(s2)
                if doubled():
                    break
            if doubled():
                break

        new_specimens.sort()
        self.specimens = new_specimens[:Population.population_num]
