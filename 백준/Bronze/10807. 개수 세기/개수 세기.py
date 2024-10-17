import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    if N < 1 or N > 100:
        return
    
    v_list = list(map(int, sys.stdin.readline().rstrip().split()))

    if len(v_list) != N:
        return
    
    v = int(sys.stdin.readline().rstrip())
    
    if v < -100 or v > 100:
        return   
    
    v_count = 0
    
    for i in v_list:
        if i == v:
            v_count += 1

    print(v_count)
    
if __name__ == '__main__':
    main()