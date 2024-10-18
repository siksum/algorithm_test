def main():
    N = int(input())
    if N < 1 or N > 100:
        return
    
    max_val = 2*N-1
    
    for i in range(max_val):
        if i < N:
            print(" "*(N-i-1), end='')
            print("*"*(2*i+1))
        else:
            print(" "*(i-N+1), end='')
            print("*"*(max_val-2*(i-N+1)))
            
        
if __name__ == '__main__':
    main()