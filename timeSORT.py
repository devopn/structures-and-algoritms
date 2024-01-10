from datetime import datetime
from sys import setrecursionlimit
setrecursionlimit(1200000000)
def timeit(func):
    def wrapper(array):
        a = datetime.now()
        func(array)
        b = datetime.now()
        print(b - a)

    return wrapper

@timeit
def buble_sort(array):  
    N = len(array)  
    for i in range(N-1):  
        for j in range(N-i-1):  
            if array[j] > array[j+1]: 
                array[j],array[j+1] = array[j+1], array[j] 

@timeit
def shake_sort(array):  
    left = 0  
    right = len(array) - 1  
    while left <= right:  
        for i in range(left, right, 1):  
            if array[i] > array[i + 1]:  
                array[i], array[i + 1] = array[i + 1], array[i]  
        right -= 1 
        for i in range(right, left, -1):  
            if array[i - 1] > array[i]:  
                array[i], array[i - 1] = array[i - 1], array[i]  
        left += 1 

@timeit
def insert_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1 
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1 
        arr[j+1] = key 

@timeit
def choose_sort(A): 
    for i in range(len(A) - 1): 
        min_index = i 
        for k in range(i + 1, len(A)): 
            if A[k] < A[min_index]: 
                min_index = k 
        A[i], A[min_index] = A[min_index], A[i] 

@timeit
def count_sort(array): 
    scope = max(array) + 1 
    C = [0] * scope 
    for x in array: 
        C[x] += 1 
    array[:] = [] 
    for number in range(scope): 
        array += [number] * C[number]

def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin+1, end+1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part
@timeit
def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part-1)
        quick(sort_nums, part+1, end)
    return quick(sort_nums, begin, end)

@timeit
def merge_sort(data):
    def merge_sorts(array): 
        if len(array) > 1: 
            r = len(array)//2 
            L = array[:r] 
            M = array[r:] 
            merge_sorts(L) 
            merge_sorts(M) 
            i = j = k = 0 
            while i < len(L) and j < len(M): 
                if L[i] < M[j]: 
                    array[k] = L[i] 
                    i += 1 
                else: 
                    array[k] = M[j] 
                    j += 1 
                k += 1 
            while i < len(L): 
                array[k] = L[i] 
                i += 1 
                k += 1 
            while j < len(M): 
                array[k] = M[j] 
                j += 1 
                k += 1
    merge_sorts(data)
@timeit
def tim_sort(array):
    array.sort()



@timeit
def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def build_max_heap(alist):
    length = len(alist)
    start = (length - 2)//2
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = index*2+1
    r = index*2+2
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

with open("random_10k_+-100000.txt", "r") as f:
    print("----- random_10k +-100000 -----")
    lines = list(map(int, f.readlines()))
    print("Heap sort:", end = " ")
    heapsort(lines)
    print("Bubble sort:", end = " ")
    buble_sort(lines)
    print("Shake sort:", end = " ")
    shake_sort(lines)
    print("Choose sort:", end = " ")
    choose_sort(lines)
    print("Insert sort:", end = " ")
    insert_sort(lines)
    print("Count sort:", end = " ")
    count_sort(lines)
    print("Quick sort:", end = " ")
    quick_sort(lines)
    print("Merge sort:", end = " ")
    merge_sort(lines)
    print("Tim sort:", end = " ")
    tim_sort(lines)

with open("random_100k_+-100000.txt", "r") as f:
    print("----- random_100k +-100000 -----")
    lines = list(map(int, f.readlines()))
    print("Heap sort:", end = " ")
    heapsort(lines)
    print("Bubble sort:", end = " ")
    buble_sort(lines)
    print("Shake sort:", end = " ")
    shake_sort(lines)
    print("Choose sort:", end = " ")
    choose_sort(lines)
    print("Insert sort:", end = " ")
    insert_sort(lines)
    print("Count sort:", end = " ")
    count_sort(lines)
    print("Quick sort: ---")
    quick_sort(lines)
    print("Merge sort:", end = " ")
    merge_sort(lines)
    print("Tim sort:", end = " ")
    tim_sort(lines)
with open("random_1kk_+-100000.txt", "r") as f:
    print("----- random_1kk +-100000 -----")
    lines = list(map(int, f.readlines()))
    print("Heap sort:", end = " ")
    heapsort(lines)
    print("Bubble sort: ---")
    buble_sort(lines)
    print("Shake sort: ---")
    shake_sort(lines)
    print("Choose sort: ---")
    choose_sort(lines)
    print("Insert sort: ---")
    insert_sort(lines)
    print("Count sort:", end = " ")
    count_sort(lines)
    print("Quick sort: ---")
    quick_sort(lines)
    print("Merge sort:", end = " ")
    merge_sort(lines)
    print("Tim sort:", end = " ")
    tim_sort(lines)
with open("random_10kk_+-100000.txt", "r") as f:
    print("----- random_10kk +-100000 -----")
    lines = list(map(int, f.readlines()))
    print("Heap sort:", end = " ")
    heapsort(lines)
    print("Bubble sort: ---")
    buble_sort(lines)
    print("Shake sort: ---")
    shake_sort(lines)
    print("Choose sort: ---")
    choose_sort(lines)
    print("Insert sort: ---")
    insert_sort(lines)
    print("Count sort:", end = " ")
    count_sort(lines)
    print("Quick sort: ---")
    quick_sort(lines)
    print("Merge sort:", end = " ")
    merge_sort(lines)
    print("Tim sort:", end = " ")
    tim_sort(lines)
with open("random_1kk_250.txt", "r") as f:
    print("----- random_1kk 250 -----")
    lines = list(map(int, f.readlines()))
    print("Heap sort:", end = " ")
    heapsort(lines)
    print("Bubble sort: ---")
    buble_sort(lines)
    print("Shake sort: ---")
    shake_sort(lines)
    print("Choose sort: ---")
    choose_sort(lines)
    print("Insert sort: ---")
    insert_sort(lines)
    print("Count sort:", end = " ")
    count_sort(lines)
    print("Quick sort: ---")
    quick_sort(lines)
    print("Merge sort:", end = " ")
    merge_sort(lines)
    print("Tim sort:", end = " ")
    tim_sort(lines)
