def main():
    T = int(input())
    
    C = [25, 10, 5, 1]
    
    for _ in range(T):
        N = int(input())
        ans = []
        for i in range(len(C)):
            r, N = divmod(N, C[i])
            ans.append(str(r))

        print(' '.join(ans))   
  
if __name__ == '__main__':
    main()