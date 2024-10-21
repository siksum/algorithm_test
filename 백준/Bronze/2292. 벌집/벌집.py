def main():
    N = int(input())
    
    if N < 1 or N > 1000000000:
        return
    
    tmp = 1
    for i in range(0, N):
        tmp += 6 * i
        
        if tmp >= N:
            print(i+1)
            return
    
if __name__ == '__main__':
    main()