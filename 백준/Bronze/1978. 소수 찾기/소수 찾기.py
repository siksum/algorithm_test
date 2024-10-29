def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(N):
        if is_prime(a[i]):
            count += 1
        
    print(count)

if __name__ == '__main__':
    main()