def main():
    N, M = map(int, input().split())
    arr = [0 for _ in range(N)]
        
    if N < 1 or N > 100 or M < 1 or M > 100:
        return
    
    for line in range(M):
        i, j, k = map(int, input().split())
    
        for index in range(i-1, j):
            arr[index] = k
    
    print(' '.join(map(str, arr)))        
    
if __name__ == '__main__':
    main()