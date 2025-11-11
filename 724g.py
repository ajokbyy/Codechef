import sys
sys.setrecursionlimit(300000)
MOD = 10**9 + 7



def add_to_basis(basis, num):
    for b in basis:
        num = min(num, num ^ b)
    if num:
        basis.append(num)



def dfs(start, graph, visited, xor_from_root, basis):
    stack = [start]
    component_nodes = [start]

    while stack:
        node = stack.pop()
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                xor_from_root[neighbor] = xor_from_root[node] ^ weight
                stack.append(neighbor)
                component_nodes.append(neighbor)
            else:

                cycle_xor = xor_from_root[node] ^ xor_from_root[neighbor] ^ weight
                add_to_basis(basis, cycle_xor)

    return component_nodes



def bit_is_set(num, i):
    return (num >> i) & 1



def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())


    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * n
    xor_from_root = [0] * n
    final_sum = 0


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            xor_basis = []
            nodes = dfs(i, graph, visited, xor_from_root, xor_basis)

            size = len(nodes)
            bit_count = [0] * 60


            for v in nodes:
                for j in range(60):
                    if bit_is_set(xor_from_root[v], j):
                        bit_count[j] += 1

            dimension = len(xor_basis)
            total_pairs = size * (size - 1) // 2 % MOD


            for j in range(60):
                power_of_two = pow(2, j, MOD)


                bit_can_change = any((b >> j) & 1 for b in xor_basis)

                if bit_can_change:

                    contribution = total_pairs * power_of_two % MOD * pow(2, dimension - 1, MOD) % MOD
                else:

                    ones = bit_count[j]
                    zeros = size - ones
                    contribution = ones * zeros % MOD * power_of_two % MOD * pow(2, dimension, MOD) % MOD

                final_sum = (final_sum + contribution) % MOD

    print(final_sum % MOD)



def main():
    solve()


if __name__ == "__main__":
    main()
