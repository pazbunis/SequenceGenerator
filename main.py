import generator as gen
dna = gen.generate_random_dna([0.25, 0.25, 0.25, 0.25], 30)
print(dna)
#print(gen.dna_to_one_hot(dna))
rep_dna = gen.random_expression_replacement(dna, 'AAAAAA')
print(rep_dna)
