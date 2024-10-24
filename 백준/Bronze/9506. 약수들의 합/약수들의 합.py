def main():
    
    while True:
        n = int(input())
        if n == -1:
            break
    
        arr = []
        total = 0
        
        for i in range(1, n):
            if n % i == 0:
                arr.append(i)
                total += i

        if total == n:
            print(f'{n} = ', end='')
            for i in arr:
                if i == arr[-1]:
                    print(i)
                else: 
                    print(f'{i} + ', end='')
        else:
            print(n, 'is NOT perfect.')        
        

if __name__ == '__main__':
    main()