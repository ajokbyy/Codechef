

import sys
sys.setrecursionlimit(300000)
MOD = 10**9 + 7
input = sys.stdin.readline


def build_lca(n, graph, root=1):
    LOG = (n).bit_length()
    parent = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)

    def dfs(u, p):
        for v in graph[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            parent[0][v] = u
            dfs(v, u)

    dfs(root, 0)

    # Binary lifting table
    for i in range(1, LOG):
        for v in range(1, n + 1):
            parent[i][v] = parent[i - 1][parent[i - 1][v]]


    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if diff >> i & 1:
                u = parent[i][u]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if parent[i][u] != parent[i][v]:
                u = parent[i][u]
                v = parent[i][v]
        return parent[0][u]

    return lca, depth

def solve():

    first_line = input().strip()
    if not first_line:
        return
    n, q = map(int, first_line.split())


    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


    lca, depth = build_lca(n, graph)


    for _ in range(q):
        k_line = input().strip()
        if not k_line:
            break
        k = int(k_line)

        nodes_line = input().strip()
        if not nodes_line:
            break
        nodes = list(map(int, nodes_line.split()))

        if k < 2:
            print(0)
            continue


        nodes.sort(key=lambda x: depth[x])

        total = 0

        for i in range(k):
            for j in range(i + 1, k):
                u, v = nodes[i], nodes[j]
                ancestor = lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[ancestor]
                total = (total + u * v * dist) % MOD

        print(total % MOD)

if __name__ == "__main__":
    try:
        solve()
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
