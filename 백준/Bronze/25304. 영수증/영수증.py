def main():
    X =int(input())
    N =int(input())
    
    if X < 1 or X > 1000000000 or N < 1 or N > 100:
        return
    
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        if a < 1 or a > 1000000 or b < 1 or b > 10:
            return
        sum += a * b
    
    if sum == X:
        print("Yes")
    else:
        print("No")
    
if __name__ == '__main__':
    main()