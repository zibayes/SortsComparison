class IntroSort():

    def introsort(self, alist):
        maxdepth = (len(alist).bit_length() - 1) * 2
        self.introsort_helper(alist, 0, len(alist), maxdepth)
        return alist

    def introsort_helper(self, alist, start, end, maxdepth):
        if end - start <= 1:
            return
        elif maxdepth == 0:
            self.heapsort(alist, start, end)
        else:
            p = self.partition(alist, start, end)
            self.introsort_helper(alist, start, p + 1, maxdepth - 1)
            self.introsort_helper(alist, p + 1, end, maxdepth - 1)

    def partition(self, alist, start, end):
        pivot = alist[start]
        i = start - 1
        j = end

        while True:
            i = i + 1
            while alist[i] < pivot:
                i = i + 1
            j = j - 1
            while alist[j] > pivot:
                j = j - 1

            if i >= j:
                return j

            self.swap(alist, i, j)

    def swap(self, alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]

    def heapsort(self, alist, start, end):
        self.build_max_heap(alist, start, end)
        for i in range(end - 1, start, -1):
            self.swap(alist, start, i)
            self.max_heapify(alist, index=0, start=start, end=i)

    def build_max_heap(self, alist, start, end):
        def parent(i):
            return (i - 1) // 2

        length = end - start
        index = parent(length - 1)
        while index >= 0:
            self.max_heapify(alist, index, start, end)
            index = index - 1

    def max_heapify(self, alist, index, start, end):
        def left(i):
            return 2 * i + 1

        def right(i):
            return 2 * i + 2

        size = end - start
        l = left(index)
        r = right(index)
        if (l < size and alist[start + l] > alist[start + index]):
            largest = l
        else:
            largest = index
        if (r < size and alist[start + r] > alist[start + largest]):
            largest = r
        if largest != index:
            self.swap(alist, start + largest, start + index)
            self.max_heapify(alist, largest, start, end)