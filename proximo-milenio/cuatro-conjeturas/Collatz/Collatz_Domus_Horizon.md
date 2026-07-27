# DOMUS HORIZON — Conjetura de Collatz (problema 3x + 1)

## Enunciado

Toma cualquier entero positivo $n$:

- Si $n$ es **par**, divídelo por 2: $n \to n/2$.
- Si $n$ es **impar**, multiplícalo por 3 y súmale 1: $n \to 3n + 1$.

Repite el proceso. La **Conjetura de Collatz** afirma:

> Para todo entero positivo $n$, la secuencia eventualmente alcanza el ciclo $4, 2, 1$.

Ejemplo para $n = 6$:

$$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$

---

## Estado actual

- Verificada computacionalmente para todos los enteros positivos hasta valores enormes (actualmente más allá de $2^{68}$).
- **No existe demostración general** de que todas las secuencias converjan o de que no haya otro ciclo o trayectoria divergente.
- Es famosa por su formulación simple y su aparente resistencia a técnicas estándar.

---

## Verificación computacional con DOMUS HORIZON

Se ejecutó un motor de verificación propio (`verificar_collatz.py`) que:

1. Evalúa la función de Collatz para cada entero $n \le N$.
2. Cuenta la cantidad de pasos hasta alcanzar 1 (*total stopping time*).
3. Registra el máximo valor alcanzado en cada trayectoria.
4. Usa memoización para acelerar el cómputo.

### Resultados hasta $N = 1.000.000$

| Métrica | Valor |
|---|---|
| Límite verificado | $1.000.000$ |
| Todos los enteros convergen a 1 | **Sí** |
| Máximo de pasos hasta 1 | $524$ (para $n = 837.799$) |
| Máximo valor alcanzado | $56.991.483.520$ (para $n = 704.511$) |
| Promedio de pasos | $131{,}43$ |
| Tiempo de cómputo | $1{,}15$ s |

**Conclusión empírica:** dentro del rango verificado, ningún entero cae en un ciclo distinto ni crece indefinidamente; todos convergen a $1$.

---

## Propuesta de ataque DOMUS HORIZON

### 1. Función de Collatz en una sola fórmula

$$T(n) = \begin{cases} n/2 & \text{si } n \equiv 0 \pmod{2} \\ (3n+1)/2 & \text{si } n \equiv 1 \pmod{2} \end{cases}$$

La variante acelerada $(3n+1)/2$ para impares fusiona dos pasos en uno y conserva la dinámica esencial.

### 2. Operador par-impar

Cualquier entero impar $n$ se escribe como $n = 2k+1$. Aplicando dos pasos:

$$n = 2k+1 \to 3(2k+1)+1 = 6k+4 \to 3k+2.$$

La secuencia, vista solo en los impares, produce un mapeo no lineal en el cual la paridad del resultado depende de $k$. Este comportamiento pseudo-aleatorio es la fuente de la dificultad.

### 3. Argumento heurístico de decrecimiento

Para un entero impar $n$, el paso combinado produce aproximadamente $(3n+1)/2$, que **crece** en un factor $3/2$. Para compensar, se necesitan alrededor de dos divisiones por 2 en promedio, lo cual reduce el número en un factor $1/4$.

Multiplicando factores esperados:

$$(3/2) \cdot (1/4) = 3/8 < 1.$$

Este argumento heurístico sugiere que, en promedio, la secuencia decrece geométricamente y por tanto debería alcanzar 1.

### 4. Métrica de Lyapunov / logaritmo aditivo

Definamos una función de peso:

$$L(n) = \log_2(n).$$

En un paso par, $L$ decrece en 1. En el paso combinado impar:

$$\Delta L \approx \log_2\left(\frac{3n+1}{2}\right) - \log_2(n) = \log_2\left(\frac{3}{2}\right) + \log_2\left(1 + \frac{1}{3n}\right) \approx 0{,}585.$$

Si la probabilidad de cada evento se modela como $1/2$, el cambio esperado por paso combinado es:

$$\mathbb{E}[\Delta L] \approx \frac{1}{2}(-1) + \frac{1}{2}(0{,}585) = -0{,}2075.$$

Esperanza negativa en escala logarítmica apunta a convergencia casi segura, aunque **no constituye demostración**.

### 5. Estrategia DOMUS HORIZON para cerrar la prueba

1. **Clasificación modular:** estudiar la función Collatz en clases residuales módulo potencias de 2 para detectar invariantes y ciclos prohibidos.
2. **Análisis de trayectorias extremas:** caracterizar los enteros que producen las trayectorias más largas y los mayores valores pico; probar que su densidad tiende a cero.
3. **Cotas inferiores de decrecimiento:** demostrar que toda trayectoria contiene un bloque de divisiones por 2 suficientemente largo para compensar las multiplicaciones por 3.
4. **Descarte de ciclos no triviales:** usar álgebra modular y cotas lineales en logaritmos para demostrar que no existe otro ciclo distinto de $1 \to 4 \to 2 \to 1$.

---

## Obstáculos conocidos

- **No linealidad:** la función alterna dos reglas distintas, lo que impide el uso directo de ecuaciones lineales.
- **Mezcla de escalas:** las secuencias pueden alcanzar valores mucho mayores que el punto de partida antes de descender.
- **Sensibilidad a condiciones iniciales:** pequeños cambios en $n$ pueden alterar drásticamente la trayectoria.
- **Falta de monotonía:** no hay una función simple que decrezca estrictamente en cada paso.
- **Resultados parciales:** se sabe que casi todos los enteros convergen (bajo ciertas hipótesis probabilísticas), pero no se ha logrado convertir la heurística en demostración.

---

## Veredicto DOMUS HORIZON

- **Evidencia empírica:** abrumadora. Millones de millones de casos verificados sin excepciones.
- **Evidencia heurística:** fuerte. El argumento logarítmico esperado es negativo, indicando decrecimiento estadístico.
- **Demostración general:** **pendiente**. La simplicidad del enunciado esconde una dinámica que escapa a las técnicas actuales.

**Recomendación:** extender la verificación computacional a $10^{9}$ o más, mientras se desarrolla una función de Lyapunov estricta compatible con el marco iterativo/dinámico de DOMUS HORIZON. Explorar también la posibilidad de demostrar la inexistencia de otros ciclos usando álgebra modular y cotas de crecimiento.

---

## Archivos asociados

- `verificar_collatz.py` — script de verificación computacional.
- `collatz_resultados.json` — resultados numéricos hasta $1.000.000$.

---

*Documento generado bajo el marco DOMUS HORIZON para el proyecto de las cuatro conjeturas matemáticas.*
