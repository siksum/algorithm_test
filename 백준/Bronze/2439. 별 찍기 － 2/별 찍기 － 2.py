import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    
    if N < 1 or N > 100:
        return
    
    for i in range(1, N+1):
        for j in range(N-i):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()

if __name__ == '__main__':
    main()