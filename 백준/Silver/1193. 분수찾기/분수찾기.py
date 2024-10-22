def main():

    # 1 = 1/1
    # 2 = 1/2
    # 3 = 2/1
    # 4 = 3/1
    # 5 = 2/2
    # 6 = 1/3
    # 7 = 1/4
    # 8 = 2/3
    # 9 = 3/2
    # 10 = 4/1

    X = int(input())
    
    if X < 1 or X > 10000000:
        return


    n = 1
    while X > n:
        X -= n
        n += 1
    
    if n % 2 == 0:
        print(f'{X}/{n - X + 1}')
    
    else:
        print(f'{n - X + 1}/{X}')

if __name__ == '__main__':
    main()