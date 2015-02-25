from _dionysus import PersistenceDiagram, Cocycle

# Remaps APNodes into Simplices
class APSimplexMap:
    def __init__(self, filtration):
        self.filtration = filtration

    def __getitem__(self, n):
        return self.filtration[n.i]

class APNode:
    def __init__(self, i, pairs):
        self.i = i
        self.pairs = pairs

    def sign(self):
        return self.unpaired() or self.i < self._pair()

    def unpaired(self):
        return self.i == self._pair()

    def _pair(self):
        return self.pairs[self.i][0]

    def pair(self):
        return APNode(self._pair(), self.pairs)

    @property
    def cocycle(self):
        return self.pairs[self.i][2]

def init_diagrams_from_adaptor(p, f, evaluator, data):
    if not evaluator:
        evaluator = lambda s: s.data

    if not data:
        data = lambda i: None

    dgms = []
    smap = p.make_simplex_map(f)
    for n in p:
        if not n.sign(): continue

        dim = smap[n].dimension()
        if dim + 1 > len(dgms):
            dgms.append(PersistenceDiagram(dim))

        b = evaluator(smap[n])
        d = evaluator(smap[n.pair()]) if not n.unpaired() else float('inf')
        if b == d: continue

        dgms[dim].append((b,d, data(n)))

    return dgms
