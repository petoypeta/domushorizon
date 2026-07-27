import time, json, math

N = 100_000

def sieve(limit):
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0:2] = b'\x00\x00'
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i*i
            is_prime[start:limit+1:step] = b'\x00' * ((limit - start)//step + 1)
    return is_prime

print('Generando criba hasta', N)
t0 = time.time()
is_prime = sieve(N)

twins = []
brun_sum = 0.0
for p in range(3, N-1):
    if is_prime[p] and is_prime[p+2]:
        twins.append((p, p+2))
        brun_sum += 1/p + 1/(p+2)

# Hardy-Littlewood estimate for pi_2(x): 2*C2 * integral_2^x dt/(ln t)^2
def hl_estimate(x):
    C2 = 0.6601618158468695739278121100145557784326233602847338323
    # simple numerical integration by trapezoid
    total = 0.0
    a, b = 2.0, float(x)
    steps = 10000
    h = (b-a)/steps
    for k in range(steps+1):
        t = a + k*h
        if t <= 1:
            continue
        val = 1.0 / (math.log(t)**2)
        if k == 0 or k == steps:
            total += 0.5 * val
        else:
            total += val
    integral = total * h
    return 2 * C2 * integral

with open('primos_gemelos_resultados.json', 'w', encoding='utf-8') as f:
    json.dump({
        'limite': N,
        'total_pares_gemelos': len(twins),
        'primeros_10': twins[:10],
        'ultimos_10': twins[-10:],
        'brun_aproximacion': round(brun_sum, 8),
        'hardy_littlewood_estimacion': round(hl_estimate(N), 1),
        'tiempo_s': round(time.time()-t0, 2)
    }, f, ensure_ascii=False, indent=2)

print(f'Pares gemelos hasta {N}: {len(twins)}')
print(f'Brun approx: {brun_sum:.8f}')
print('Resultados guardados en primos_gemelos_resultados.json')
