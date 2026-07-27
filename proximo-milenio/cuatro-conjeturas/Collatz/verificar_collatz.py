import time, json

N = 1_000_000

def collatz(n, memo):
    steps = 0
    max_val = n
    sequence = []
    current = n
    while current != 1:
        if current in memo:
            steps += memo[current]
            break
        sequence.append(current)
        if current % 2 == 0:
            current //= 2
        else:
            current = 3*current + 1
        max_val = max(max_val, current)
        steps += 1
    # backtrack
    for idx, val in enumerate(sequence):
        memo[val] = steps - idx
    return steps, max_val

print('Verificando Collatz hasta', N)
t0 = time.time()
memo = {1: 0}
max_steps = 0
n_max_steps = 0
max_value = 0
n_max_value = 0
all_converge = True

for n in range(2, N+1):
    steps, mval = collatz(n, memo)
    if steps > max_steps:
        max_steps = steps
        n_max_steps = n
    if mval > max_value:
        max_value = mval
        n_max_value = n

total_time = time.time() - t0
avg_steps = sum(memo[n] for n in range(2, N+1)) / (N-1)

with open('collatz_resultados.json', 'w', encoding='utf-8') as f:
    json.dump({
        'limite': N,
        'todos_convergen': all_converge,
        'max_pasos': max_steps,
        'n_max_pasos': n_max_steps,
        'max_valor_alcanzado': max_value,
        'n_max_valor': n_max_value,
        'promedio_pasos': round(avg_steps, 2),
        'tiempo_s': round(total_time, 2)
    }, f, ensure_ascii=False, indent=2)

print(f'Verificado hasta {N}: todos convergen={all_converge}, max pasos={max_steps} (n={n_max_steps}), max valor={max_value} (n={n_max_value})')
print(f'Tiempo: {total_time:.2f}s')
