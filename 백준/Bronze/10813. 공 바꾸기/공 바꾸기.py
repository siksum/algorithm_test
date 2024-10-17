def main():
    N, M = map(int, input().split())
    arr = [i+1 for i in range(N)]
        
    if N < 1 or N > 100 or M < 1 or M > 100:
        return
    
    for line in range(M):
        i, j = map(int, input().split())

        temp = arr[j-1]
        arr[j-1] = arr[i-1]
        arr[i-1] = temp
    
    print(' '.join(map(str, arr)))        
    
if __name__ == '__main__':
    main()