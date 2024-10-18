import sys

def main():
    while True:
        A, B = map(int, sys.stdin.readline().rstrip().split())
    
        if A < 0 or B > 10:
            return
        
        if A == 0 and B == 0:
            break
        
        print(A + B)
    
if __name__ == '__main__':
    main()