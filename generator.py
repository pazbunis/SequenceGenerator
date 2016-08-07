import numpy as np
from random import randint

num2letter = {0: 'A', 1: 'C', 2: 'T', 3: 'G'}
letter2num = dict((v, k) for k, v in num2letter.items())


def generate_random_dna(probs, n):
    """generates a sequence of n bases where probs are the probabilities of A, C,T, G"""
    seq = (num2letter[np.argmax(np.random.multinomial(1, probs))] for j in range(0,n))
    return ''.join(seq)


def dna_to_one_hot(seq):
    """converts a DNA sequence of length N to its one-hot 4xN representation"""
    num_bases = len(seq)
    letters = list(seq)
    idxs = list(map(lambda l : letter2num[l], letters))
    one_hot = np.zeros((4, num_bases))
    one_hot[idxs, np.arange(num_bases)] = 1
    return one_hot


def random_expression_replacement(seq, rep_expression):
    """places rep_expression at a random location inside seq (without trimming it)"""
    num_bases = len(seq)
    exp_length = len(rep_expression)
    idx = randint(0,num_bases - exp_length)
    output = seq[:idx] + rep_expression + seq[idx + exp_length:]
    return output
