from joblib import Parallel, delayed
from os.path import exists
import json
import gc

PARALLEL = 6
DIGITS = 100
BEAM_WIDTH = 3 * 10**6
CHUNK = BEAM_WIDTH//PARALLEL
MAX = 10**DIGITS
HEURISTIC_DEPTH = 7
MOD = 6**HEURISTIC_DEPTH
heuristic_factors = [0] * MOD


def collatz(n, debug=False):
    result = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n+1
        result += 1
        if debug:
            print(result, n)
    return result


def collatz_prev(l):
    result = []
    for b in l:
        result.append(2*b)
        if b%6 == 4:
            result.append(b//3)
    return result


for m in range(MOD):
    for n in range(MOD+m, 11*MOD+m, MOD):
        lowest = n
        beam = [n]
        for d in range(HEURISTIC_DEPTH):
            beam = collatz_prev(beam)
            lowest = min(lowest, min(beam))
        heuristic_factors[m] = max(lowest/n, heuristic_factors[m])


def score(n):
    return n * heuristic_factors[n%MOD]


beam = [8]
if exists("beam.json"):
    with open("beam.json") as f:
        beam = json.loads(f.read())
chain = collatz(beam[0])
while len(beam) > 0:
    mi = min(beam)
    if chain % 200 == 0:
        with open('beam.json', 'w') as f: f.write(json.dumps(beam))
    if mi < MAX:
        print(f'{chain}: {mi}    ...{round(chain*100/len(str(mi)), 2)}')
    parts = [beam[p*CHUNK: (p+1)*CHUNK] for p in range(PARALLEL)]
    r = Parallel(n_jobs=PARALLEL)(delayed(collatz_prev)
                                  (parts[i]) for i in range(PARALLEL))
    next = []
    for l in r:
        next += l
    beam = sorted(next, key=score)
    if len(beam) > BEAM_WIDTH:
        beam = beam[:BEAM_WIDTH]

    parts = None
    next = None
    r = None
    gc.collect()
    chain += 1