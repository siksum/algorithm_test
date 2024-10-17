import sys

def main():
    testcase = int(sys.stdin.readline().rstrip())
    
    for i in range(1, testcase+1):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        if A < 0 or B > 10:
            return
        print(f"Case #{i}:", A + B)
  

if __name__ == '__main__':
    main()