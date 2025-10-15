import time
import itertools
import matplotlib.pyplot as plt


def brute_force_knapsack(weights, values, W):
    # O(2^n)
    n = len(weights)
    max_value = 0
    best_combination = []

    for combination in itertools.product([0, 1], repeat=n):
        total_weight = sum(weights[i] for i in range(n) if combination[i] == 1)
        total_value = sum(values[i] for i in range(n) if combination[i] == 1)

        if total_weight <= W and total_value > max_value:
            max_value = total_value
            best_combination = combination

    selected_items = [(weights[i], values[i]) for i in range(n) if best_combination[i] == 1]
    total_selected_weight = sum(item[0] for item in selected_items)

    return max_value, selected_items, total_selected_weight


def measure_time(func, weights, values, W):
    start_time = time.time()
    max_value, selected_items, total_weight = func(weights, values, W)
    return time.time() - start_time, max_value, selected_items, total_weight


def read_input(filename):
    scenarios = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    i = 0
    while i < len(lines):
        W = int(lines[i])
        i += 1
        weights, values = [], []
        while i < len(lines) and ' ' in lines[i]:
            w, v = map(int, lines[i].split())
            weights.append(w)
            values.append(v)
            i += 1
        scenarios.append((W, weights, values))

    return scenarios


# Read input from file
input_file = "q3input.txt"
scenarios = read_input(input_file)

execution_times = []
n_values = []

for W, weights, values in scenarios:
    n = len(weights)
    exec_time, max_value, selected_items, total_weight = measure_time(brute_force_knapsack, weights, values, W)
    execution_times.append(exec_time)
    n_values.append(n)
    print(f"Scenario with {n} items:")
    print(f"  Maximum Value: {max_value}")
    print(f"  Selected Items (weight, value): {selected_items}")
    print(f"  Total Weight Used: {total_weight}")
    print(f"  Execution Time: {exec_time:.5f} sec\n")

plt.plot(n_values, execution_times, marker='o', label='Brute Force Knapsack')
plt.xlabel('Number of Artifacts')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Brute Force Knapsack')
plt.legend()
plt.grid()
plt.show()