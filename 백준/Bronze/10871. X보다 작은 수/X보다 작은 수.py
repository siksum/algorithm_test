import sys

def main():
    N, X = (map(int, sys.stdin.readline().rstrip().split()))
    
    if N < 1 or X > 10000:
        return
    
    print_list = []
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    
    for i in A:
        if i < X:
            print_list.append(i)

    print(' '.join(map(str, print_list)))
    
if __name__ == '__main__':
    main()