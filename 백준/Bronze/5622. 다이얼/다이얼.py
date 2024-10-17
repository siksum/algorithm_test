import sys

def main():
    total_time = 0
    num = sys.stdin.readline().strip()
    arr = [3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(num)):
        if num[i] == 'S' or num[i] == 'V' or num[i] == 'Y' or num[i] == 'Z':
            num_index = (ord(num[i])-62)//3
            total_time += arr[num_index-2]
        else:
            num_index = (ord(num[i])-59)//3
            total_time += arr[num_index-2]
    print(total_time)
            
        
if __name__ == '__main__':
    main()