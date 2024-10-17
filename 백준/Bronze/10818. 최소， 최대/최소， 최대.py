import sys

def main():
    N = map(int, sys.stdin.readline().rstrip().split())
    
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    
    print(min(A), max(A))   
    
if __name__ == '__main__':
    main()