

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def fast_tokens():
    for tok in sys.stdin.buffer.read().split():
        yield tok

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def _add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def range_add(self, l, r, delta):
        if l > r:
            return
        self._add(l, delta)
        self._add(r + 1, -delta)

    def point_query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class HLD:
    def __init__(self, n, graph):
        self.n = n
        self.g = graph
        self.parent = [0] * (n + 1)
        self.depth = [0] * (n + 1)
        self.heavy = [-1] * (n + 1)
        self.size = [0] * (n + 1)
        self.head = [0] * (n + 1)
        self.pos = [0] * (n + 1)
        self.cur_pos = 0

    def dfs1(self, u, p):

        self.parent[u] = p
        self.size[u] = 1
        max_size = 0
        for v in self.g[u]:
            if v == p:
                continue
            self.depth[v] = self.depth[u] + 1
            self.dfs1(v, u)
            if self.size[v] > max_size:
                max_size = self.size[v]
                self.heavy[u] = v
            self.size[u] += self.size[v]

    def dfs2(self, u, h):

        self.head[u] = h
        self.cur_pos += 1
        self.pos[u] = self.cur_pos

        if self.heavy[u] != -1:
            self.dfs2(self.heavy[u], h)
        for v in self.g[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self.dfs2(v, v)

    def build(self, root=1):
        self.depth[root] = 0
        self.dfs1(root, 0)
        self.dfs2(root, root)

    def path_apply(self, u, v, apply_func):

        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            apply_func(self.pos[self.head[u]], self.pos[u])
            u = self.parent[self.head[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        apply_func(self.pos[u], self.pos[v])


def solve():
    it = fast_tokens()
    out = []

    while True:
        try:
            n = int(next(it))
            m = int(next(it))
            p = int(next(it))
        except StopIteration:
            break  # EOF


        A = [0] + [int(next(it)) for _ in range(n)]


        g = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            g[u].append(v)
            g[v].append(u)


        hld = HLD(n, g)
        hld.build(root=1)
        bit = Fenwick(n)


        for i in range(1, n + 1):
            bit.range_add(hld.pos[i], hld.pos[i], A[i])


        def add_on_path(u, v, delta):
            hld.path_apply(u, v, lambda l, r: bit.range_add(l, r, delta))


        for _ in range(p):
            op = next(it).decode()
            if op == 'I':
                c1 = int(next(it)); c2 = int(next(it)); k = int(next(it))
                add_on_path(c1, c2, k)
            elif op == 'D':
                c1 = int(next(it)); c2 = int(next(it)); k = int(next(it))
                add_on_path(c1, c2, -k)
            elif op == 'Q':
                c = int(next(it))
                out.append(str(bit.point_query(hld.pos[c])))


    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
