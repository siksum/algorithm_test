def main():
    N, M = map(int, input().split())
    A = []
    B = []
    
    for _ in range(N):
        A.append(list(map(int, input().split())))
        
    for _ in range(N):
        B.append(list(map(int, input().split())))
    
    total = []
    
    for i in range(N):
        M_total = []
        for j in range(M):
            M_total.append(A[i][j] + B[i][j])
        total.append(M_total)

    for i in range(N):
        print(*total[i])

if __name__ == '__main__':
    main()