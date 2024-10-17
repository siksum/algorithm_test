def main():
    N, M = map(int, input().split())
    
    arr = [i+1 for i in range(N)]
    
    for _ in range(M):
        i, j = map(int, input().split())
        arr[i-1:j] = arr[i-1:j][::-1]
        
    print(' '.join(map(str, arr)))
    
if __name__ == '__main__':
    main()