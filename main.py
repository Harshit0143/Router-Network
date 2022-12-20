# we need only path or walks or trails?
# using trail is used. bnotice that if A is a subset of B then min(A)>= min(B)
# we can always breakdown a trail into shorter subset paths


# Since the list can contain multiple networks between same pair of self.vertex_list[adj] s, it makes sense
# to use the maximum capacity one from them every time
# also it is possible that (0,1,30) and (1,0, 60) may be presen in this case the most useful edge is (0,1,30)
# so we need to convert the list into a simple list first


def simple_undirected_graph(L):

    for i in range(0, len(L)):

        if L[i][0] > L[i][1]:
            L[i] = (L[i][1], L[i][0], L[i][2])

    L.sort()
    M = []
    M.append(L[-1])

    for i in range(len(L)-2, -1, -1):
        if L[i][0] == M[-1][0] and L[i][1] == M[-1][1]:
            continue
        M.append(L[i])
    return M

    # L has no more than 1 edge between 2 vertices we want to use the max capacity of them all
    # (0,1,10) and (1,0,30) will appear exactly once as (0,1,30)


class graph:
    class node:  # vertices are self.vertex_list[adj] s
        def __init__(self):
            self.adj_list = []

    def compare(self, l, r):

        if self._caplis[self.priority_q[l]] > self._caplis[self.priority_q[r]]:
            return True
        elif self._caplis[self.priority_q[l]] == -1:  # these is eactly one such
            return True
        return False

    def heap_down(self, id):
        l_id = len(self.priority_q)-1
        while (2*id + 1 <= l_id):
            l_ch = 2*id + 1
            r_ch = 2*id + 2
            max_ch = l_ch
            if r_ch <= l_id:
                if self.compare(r_ch, l_ch):
                    max_ch = r_ch
            if not self.compare(max_ch, id):
                break
            self.q_loc[self.priority_q[id]] = max_ch
            self.q_loc[self.priority_q[max_ch]] = id
            self.priority_q[id], self.priority_q[max_ch] = self.priority_q[max_ch], self.priority_q[id]
            id = max_ch

    def heap_up(self, id):  # takes list index to heap up
        while (id-1)//2 >= 0:
            par = (id-1)//2
            # if child is not strictly greater than prent then stop
            if not self.compare(id, par):
                break
            self.q_loc[self.priority_q[id]] = par
            self.q_loc[self.priority_q[par]] = id
            self.priority_q[id], self.priority_q[par] = self.priority_q[par], self.priority_q[id]
            id = par

    def top(self):
        return self.priority_q[0]

    def pop_max(self):
        self.q_loc[self.priority_q[0]] = len(self.priority_q)-1
        self.q_loc[self.priority_q[-1]] = 0

        self.priority_q[0], self.priority_q[-1] = self.priority_q[-1], self.priority_q[0]
        a = self.priority_q.pop()
        self.heap_down(0)
        return a

    def __init__(self, n, L, s, t):  # L is the edge list #
        self._size = n
        self._caplis = [0]*n
        self._caplis[s] = -1

        self.priority_q = [0]*n
        self.q_loc = [None]*n
        for i in range(0, n):
            self.q_loc[i] = i
            self.priority_q[i] = i
        self._caplis[s] = -1
        self.heap_up(s)

        self.vertex_list = [None]*n
        for i in range(0, n):
            self.vertex_list[i] = self.node()
        for i in L:
            (u, v, c) = i
            self.vertex_list[u].adj_list.append((v, c))
            self.vertex_list[v].adj_list.append((u, c))


# i think we need to fix that each element should be present int he queue just 1 occurence

    def mini(self, a, b):
        if a == -1:
            return b
        elif b == -1:
            return a
        return min(a, b)

    def bfs(self, st, end):

        prev = [None]*self._size
        visited = [False]*self._size

        while len(self.priority_q) != 0:  # think of this

            x = self.pop_max()

            visited[x] = True
            for y in self.vertex_list[x].adj_list:

                (ind, wt) = y
                latest_cap = self.mini(wt, self._caplis[x])

                if not visited[ind] and self._caplis[ind] != -1 and latest_cap > self._caplis[ind]:
                    self._caplis[ind] = latest_cap  # x tak mini
                    self.heap_up(self.q_loc[ind])
                    prev[ind] = x
        return prev

    def find_max(self, st, end):
        prev = self.bfs(st, end)
        cap = self._caplis[end]

        path = []
        while end != st:
            path.append(end)
            end = prev[end]
        path.append(st)
        for i in range(0, len(path)//2):
            path[i], path[len(path)-1-i] = path[len(path)-1-i], path[i]

        return (cap, path)


def findMaxCapacity(n, L, u, v):

    X = simple_undirected_graph(L)

    g = graph(n, X, u, v)

    return g.find_max(u, v)
