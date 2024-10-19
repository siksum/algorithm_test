def main():
    arr = []
    
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    
    max_val = 0
    max_line = 0
    max_index = 0
    
    for i in range(len(arr)):
        if max_val < max(arr[i]):
            max_val = max(arr[i])
            max_line = i+1
            max_index = arr[i].index(max(arr[i]))+1
        elif max_val == max(arr[i]):
            if max_index < arr[i].index(max(arr[i]))+1:
                max_val = max(arr[i])
                max_line = i+1
                max_index = arr[i].index(max(arr[i]))+1
    
    print(max_val)
    print(max_line, max_index)
    
if __name__ == '__main__':
    main()