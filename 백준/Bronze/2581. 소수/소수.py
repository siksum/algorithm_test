def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input())
    M = int(input())
    
    count = 0
    min_prime = 0
    
    for i in range(N, M+1):
        if is_prime(i):
            count += i 
            if min_prime == 0:
                min_prime = i
    
    if min_prime == 0:
        print(-1)
    else:
        print(count)
        print(min_prime)
        
if __name__ == '__main__':
    main()