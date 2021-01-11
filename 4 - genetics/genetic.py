import random

from .population import Population
from .specimen import Specimen

mutation_probability = 0.01
population_num = 4

generations_num = 3

population = Population(mutation_probability, population_num)
for i in range(population_num):
    rand_genome = [j for j in range(1, len(Specimen.paths))]
    random.shuffle(rand_genome)
    rand_genome.insert(0, 0)
    rand_genome.append(0)
    population.specimens.append(Specimen(rand_genome))
population.specimens.sort()
print('Поколение 1:')
print(population)

for i in range(generations_num - 1):
    population.next_generation()
    print('Поколение {0}:'.format(i + 2))
    print(population)

best_specimen = min(population.specimens)
print('Оптимальный путь:', best_specimen.genome, 'длиной', best_specimen.weight)

