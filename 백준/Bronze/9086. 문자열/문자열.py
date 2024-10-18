def main():
    testcase = int(input())
    
    if testcase < 1 or testcase > 10:
        return
    
    for i in range(testcase):
        str = input()
        print(str[0] + str[-1])    
    
        
if __name__ == '__main__':
    main()