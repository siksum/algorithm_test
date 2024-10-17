def main():
    N =int(input())
    if N < 4 or N > 1000 or N % 4 != 0:
        return
    
    for i in range(4, N+1, 4):
        print("long", end=' ')
    print("int")
  

if __name__ == '__main__':
    main()