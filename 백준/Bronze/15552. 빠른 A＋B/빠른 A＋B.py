import sys

def main():
    testcase = int(sys.stdin.readline().rstrip())
    if testcase > 1000000:
        return
    
    for i in range(testcase):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A + B)
  

if __name__ == '__main__':
    main()