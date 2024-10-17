def compare_quadrant(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)
    else:
        print(0)
        
        
def main():
    x = int(input())
    y = int(input())
    
    compare_quadrant(x, y)
    
    
if __name__ == '__main__':
    main()