ls_of_nums= [7, 9, 10, 3, 2, 1, 8, 5, 8 ]

#Find first elem in list and swap with first elem in list 
#move the sorted boundary to the right and repeat until done



def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n):
            if arr[j]< arr[min_idx]:
                min_idx= j 
        arr[i], arr[min_idx]= arr[min_idx], arr[i]
    return arr

def liner_search(ls, key):
    for i, num in enumerate(ls):
        if num == key:
            print("{} is located at position {}".format(key, i))
            return i 
    print("{} is not in the list".format(key))
    return -1

def binary_search(ls, key):
    left=0
    right= len(ls)-1
    while left <= right:
        middle =(left + right )// 2

        if ls[middle] ==key:
            return middle
        if ls[middle]> key:
            right = middle-1
        if ls[middle]< key: 
            left = middle + 1
    return -1 
sorted_nums= selection_sort(ls_of_nums)
print(sorted_nums)

liner_search(sorted_nums, 10)


bs_position= binary_search(sorted_nums, 5)
print(bs_position)