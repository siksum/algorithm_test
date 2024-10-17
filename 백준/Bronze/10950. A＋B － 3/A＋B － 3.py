def main():
    test_case =int(input())    
    sum_list = []
    for i in range(test_case):
        A, B = map(int, input().split())
        if A < 0 or B > 11:
            return

        sum_list.append(A + B) 
    
    for i in range(test_case):
        print(sum_list[i])    
    
if __name__ == '__main__':
    main()