import os
import struct
import random

def check_unordered(arr, cmp, invert_cmp):
    sorted = True    
    counter = 0
    for i in range(len(arr) - 1):
        check = cmp(arr[i], arr[i+1])
        if invert_cmp: check = not check
        
        if check:
            counter += 1
            sorted = False
    return (sorted, counter)

def amogus_sort(arr: list, debug=False, cmp=lambda x,y: x > y):
    arr_cpy = arr.copy()
    sorted = False
    invert_cmp = False
    
    _, counter = check_unordered(arr, cmp, invert_cmp)
    arr_size = len(arr)
    if counter >= arr_size / 2:
        print("array is impossible to sort with given conditions! maybe the crewmates are the real imposters!")
        print("inverting sorting criteria...")
        invert_cmp = not invert_cmp

    while not sorted:
        for element in arr:
            sorted, counter = check_unordered(arr, cmp, invert_cmp)
            arr_size = len(arr)
            if sorted or counter >= arr_size / 2: break
            
            votes = struct.unpack('I', os.urandom(4))[0] % (arr_size+1)
            if votes >= arr_size / 2:
                if (debug): print(f'element ejected: {element}; votes: {votes}/{arr_size}')
                arr.remove(element)

        sorted, counter = check_unordered(arr, cmp, invert_cmp)
        
        if not sorted and counter >= len(arr) / 2:
            if (debug): print("the imposters have won! restarting the sorting procedure...")
            arr=arr_cpy.copy()

    if debug: print("the crewmates have won! the array is sorted!")
    return arr


if __name__ == '__main__':
    arr_size = 100
    minimum = 0
    maximum = 1
    arr = [random.randint(minimum, maximum) for i in range(arr_size)]
    print(f"unsorted array: {arr}")
    arr=amogus_sort(arr)
    print(f"sorted array: {arr}")