import math

input_data = [(0.26, 1),
              (0.20, 0),
              (0.48, 1),
              (0.30, 0)]


def cross_entropy(input_data):
    loss = 0
    n = len(input_data)
    for entry in input_data:
        w_sum = entry[0]
        y = entry[1]
        loss += -(y * math.log10(w_sum) + (1 - y) * math.log10(1 - w_sum))
        print(-(y * math.log10(w_sum) + (1 - y) * math.log10(1 - w_sum)))
    return loss / n


error_term = cross_entropy(input_data)
print(error_term)
