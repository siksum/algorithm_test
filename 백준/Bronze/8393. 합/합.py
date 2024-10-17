def main():
    n =int(input())
    if n < 1 or n > 10000:
        return
    
    sum = 0
    
    for i in range(1, n+1):
        sum += i
    print(sum)
 
if __name__ == '__main__':
    main()