import generator as gen
from random import shuffle


def generate_sample(half_size, x_path, y_path):
    """generates 2*half_size sample points (DNA sequences) and stores them at the given paths, line delimited"""
    labels = list(0 for i in range(0, half_size)) + list(1 for i in range(0, half_size))
    shuffle(labels)
    with open(x_path, 'w') as x_file:
        with open(y_path, 'w') as y_file:
            for i in range(0, 2 * half_size):
                dna = gen.generate_random_dna([0.25, 0.25, 0.25, 0.25], 1000)
                if labels[i] == 1:
                    #dna = gen.place_expression(dna, 'AAAAAAAA', 0)
                    dna = gen.random_expression_replacement(dna, 'AAAAAAAA')
                x_file.write(dna + '\n')
                y_file.write(str(labels[i]) + '\n')

train_x_path = '/cs/grad/pazbu/paz/dev/projects/SequenceGenerator/train_x_1000.txt'
train_y_path = '/cs/grad/pazbu/paz/dev/projects/SequenceGenerator/train_y_1000.txt'

test_x_path = '/cs/grad/pazbu/paz/dev/projects/SequenceGenerator/test_x_1000.txt'
test_y_path = '/cs/grad/pazbu/paz/dev/projects/SequenceGenerator/test_y_1000.txt'


generate_sample(1000, train_x_path, train_y_path)
generate_sample(100, test_x_path, test_y_path)
