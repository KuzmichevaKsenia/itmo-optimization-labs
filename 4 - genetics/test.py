from itertools import permutations

from .specimen import Specimen

population = []
perm = list(permutations([i for i in range(1, len(Specimen.paths))]))
for i in perm:
    population.append(Specimen([0] + list(i) + [0]))
best_specimen = min(population)
print('Оптимальный путь:', best_specimen.genome, 'длиной', best_specimen.weight)