def compare_num(A, B):
    if A > B:
        print(">")
        
    elif A < B:
        print("<")
        
    elif A == B:
        print("==")
        
        
def main():
    num_list = input().split()
    A, B = map(int, num_list)
    
    compare_num(A, B)
    
    
if __name__ == '__main__':
    main()