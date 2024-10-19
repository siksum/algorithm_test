def main():
    arr = [[0]*100 for _ in range(100)]
    
    N = int(input())
    for i in range(N):
        x, y = map(int, input().split())
    
        for i in range(y, y+10):
            for j in range(x, x+10):
                arr[i][j] = 1
    
    cnt = 0
    for i in range(100):
        cnt += arr[i].count(1)
    print(cnt)
  
if __name__ == '__main__':
    main()