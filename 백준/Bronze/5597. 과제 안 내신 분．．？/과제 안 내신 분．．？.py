def main():
    arr = [0 for _ in range(30)]
    
    for i in range(28):
        student = int(input())
        arr[student-1] = 1
    
    missing = [i+1 for i, value in enumerate(arr) if value == 0]
    print(' '.join(map(str, missing)))
    
if __name__ == '__main__':
    main()