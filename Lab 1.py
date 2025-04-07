# Variant 3
## using 1 def
def hamming_distance_triplets(s, t):
    distance = 0
    for i in range(0, len(s), 3):
        triplet_s = s[i:i+3]
        triplet_t = t[i:i+3]
        for j in range(len(triplet_s)):
            if triplet_s[j] != triplet_t[j]:
                distance += 1
    return distance

s = str(input("Введите первую последовательность: "))
t = str(input("Введите вторую последовательность: "))

distance = hamming_distance_triplets(s, t)

print(distance)
## using class + 3 methods
class HammingTripletCalculator:
    def __init__(self):
        self.s=""
        self.t=""

    def input_sequence(self):
        self.s = input("Введите первую последовательность:")
        self.t = input("Введите вторую последовательность:")

    def calculate_distance(self):
        distance = 0
        for i in range (0, len(self.s), 3):
            triplet_s = self.s[i:i+3]
            triplet_t = self.t[i:i+3]
            for s_char, t_char in zip(triplet_s,triplet_t):
                if s_char != t_char:
                    distance += 1
        return distance

calculator = HammingTripletCalculator()

## GAGCCTACTAACGGGAT
## CATCGTAATGACGGCCT
