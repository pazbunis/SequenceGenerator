import generator as gen
dna = gen.generate_random_dna([0.25, 0.25, 0.25, 0.25], 200)
replaced_dna = gen.random_expression_replacement(dna, 'AAAAAA')

print(dna)
print(replaced_dna)

print(gen.dna_to_one_hot(dna))

