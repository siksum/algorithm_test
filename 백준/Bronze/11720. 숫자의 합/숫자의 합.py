def main():
    N = int(input())
    A = input()
    total = 0
    for i in range(N):
        total += int(A[i])
    print(total)        
    
if __name__ == '__main__':
    main()