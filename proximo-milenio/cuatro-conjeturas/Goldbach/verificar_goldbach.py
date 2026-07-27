import math, time, json

N = 100_000

def sieve(limit):
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i*i
            is_prime[start:limit+1:step] = b'\x00' * ((limit - start)//step + 1)
    primes = [i for i, val in enumerate(is_prime) if val]
    return is_prime, primes

print('Generando criba hasta', N)
t0 = time.time()
is_prime, primes = sieve(N)
print(f'Criba lista: {len(primes)} primos en {time.time()-t0:.2f}s')

# Contar representaciones por paridad
counts = [0]*(N+1)
for i, p in enumerate(primes):
    for q in primes[i:]:
        s = p + q
        if s > N:
            break
        counts[s] += 1

print('Conteo de pares terminado')

evens = list(range(4, N+1, 2))
min_count = min(counts[n] for n in evens)
max_count = max(counts[n] for n in evens)
min_n = next(n for n in evens if counts[n] == min_count)
max_n = next(n for n in evens if counts[n] == max_count)

zero_evens = [n for n in evens if counts[n] == 0]

with open('goldbach_resultados.json', 'w', encoding='utf-8') as f:
    json.dump({
        'limite': N,
        'total_primos': len(primes),
        'total_pares': len(evens),
        'representaciones_minimas': min_count,
        'n_min_representaciones': min_n,
        'representaciones_maximas': max_count,
        'n_max_representaciones': max_n,
        'contraejemplos_hasta_N': zero_evens,
        'tiempo_s': round(time.time()-t0, 2)
    }, f, ensure_ascii=False, indent=2)

print('Resultados guardados en goldbach_resultados.json')
print(f'Contraejemplos hasta {N}: {len(zero_evens)}')
print(f'Min representaciones: {min_count} (n={min_n}), Max: {max_count} (n={max_n})')
