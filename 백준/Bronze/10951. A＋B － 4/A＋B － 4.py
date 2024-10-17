import sys

def main():
    while True:
        try:
            A, B = map(int, sys.stdin.readline().rstrip().split())
        
            if A < 0 or B > 10:
                return
            
            print(A + B)
            
        except:
            break
    
if __name__ == '__main__':
    main()