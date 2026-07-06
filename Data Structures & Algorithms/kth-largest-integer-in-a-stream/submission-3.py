class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for val in nums:
            print(self.heap)
            if len(self.heap) < k:
                self.heap.append(val)
                self.heapifyUp(len(self.heap) - 1)
            elif val > self.heap[0]:
                self.heap[0] = val
                self.heapifyDown(0)


    def add(self, val: int) -> int:
        print(self.heap)
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.heapifyUp(len(self.heap) - 1)
        elif val > self.heap[0]:
            self.heap[0] = val
            self.heapifyDown(0)
        return self.heap[0]
        
    def heapifyUp(self, i):
        while(self.parent(i) >= 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.swap(self.parent(i), i)
            i = self.parent(i)
    def heapifyDown(self, i):
        while(self.leftChild(i) < self.k):
            smaller = self.leftChild(i)
            if self.rightChild(i) < self.k and self.heap[self.rightChild(i)] < self.heap[smaller]:
                smaller = self.rightChild(i)
            if self.heap[i] < self.heap[smaller]:
                break
            else:
                self.swap(i, smaller)
                i = smaller
        
    
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
    def leftChild(self, i):
        return i * 2 + 1
    def rightChild(self, i):
        return i * 2 + 2
    def parent(self, i):
        return int((i - 1) / 2)
