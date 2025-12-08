import math
import heapq

from collections import Counter
def distance(pt1, pt2):
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2

    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


class UnionFind:

    def __init__(self, pts):
        self.pts = pts
        n = len(pts)
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, i):
        parent = self.parents[i]

        if parent != self.parents[parent]:
            self.parents[i] = self.find(parent)
            return self.parents[i]
        
        return parent
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)

        if irep == jrep:
            return 
        
        
        if self.ranks[irep] > self.ranks[jrep]:
            self.parents[jrep] = irep
        elif self.ranks[irep] < self.ranks[jrep]:
            self.parents[irep] = jrep
        else:
            self.parents[jrep] = irep
            self.ranks[irep] += 1
 
    

def partA():
    with open("inputTxt.txt", "r") as f:
        lines = f.readlines()

        

        points = list()
        distances = []
        for line in lines:
            line = line.strip()
            x, y, z = [int(x) for x in line.split(",")]
            
            pt = (x,y,z)
            points.append(pt)
        
        for j in range(len(points)-1):
            pt = points[j]
            for i in range(j+1, len(points)):
                pt2 = points[i]
                heapq.heappush(distances, (distance(pt2, pt), (i, j)))

        
        unionFind = UnionFind(points)

        # making 10 shortest connections 
        for _ in range(1000):
            d, pair = heapq.heappop(distances)
            i1, i2 = pair 

            unionFind.unite(i1, i2)


        counter = Counter(unionFind.parents)

        

        # get all groups
        groups = {}

        for i in range(len(unionFind.parents)):
            parent = unionFind.find(i)

            if parent not in groups:
                groups[parent] = 0
            
            groups[parent] += 1
        
        vals = sorted(groups.values(), reverse=True)
        
        return vals[0] * vals[1] * vals[2]
            

        
            
print(partA())

        




        
