import numpy as np

def binary_search(data, target, low, high):
    mid = (low + high)//2

    if target == data[mid]:
        return mid

    elif target > data[mid]:
        binary_search(data, target, mid+1, high)

    elif target < data[mid]:
        binary_search(data, target, low, mid-1)

def main():
    arr = np.arange(0, 7)
    pos = binary_search(arr, 4, 0, len(arr))
    print(pos)


if __name__ == '__main__':
    main()