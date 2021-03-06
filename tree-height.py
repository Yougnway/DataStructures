# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                # self.n = int(sys.stdin.readline())
                # self.parent = list(map(int, sys.stdin.readline().split()))
                self.n = int(5)
                self.parent = [4,-1, 4 ,1, 1]
                self.heights = [0] * self.n

        def old_compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;
        def compute_height(self):
                # Replace this code with a faster implementation
                return max([self.find_height(i) for i in range(self.n)])

        def find_height(self, node):
                if self.parent[node] == -1:
                        return 1

                if self.heights[node]:
                        return self.heights[node]

                self.heights[node] = 1 + self.find_height(self.parent[node])
                return self.heights[node]


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
