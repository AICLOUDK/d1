# python3
import sys
import itertools
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    k, t, reads = int(data[0]), int(data[1]), data[2:]
    kmers = [read[i:i+k] for read in reads for i in range(len(read)-k+1)]
    g = defaultdict(lambda: [set(), 0])
    for kmer in kmers:
        p, s = kmer[:-1], kmer[1:]
        if p != s:
            if s not in g[p][0]:
                g[p][0].add(s)
                g[s][1] += 1
    print(count_bubbles(t, g))

def count_bubbles(t, g):
    b = 0
    p = defaultdict(list)
    def dfs(path, start, node, depth):
        if node != start and g[node][1] > 1:
            p[(start, node)].append(path[:])
        if depth == t:
            return
        for n in g[node][0]:
            if n not in path:
                dfs(path + [n], start, n, depth + 1)
    for n in g:
        if len(g[n][0]) > 1:
            dfs([n], n, n, 0)
    for ps in p.values():
        for a, b_ in itertools.combinations(ps, 2):
            if len(set(a) & set(b_)) == 2:
                b += 1
    return b

if __name__ == "__main__":
    main()