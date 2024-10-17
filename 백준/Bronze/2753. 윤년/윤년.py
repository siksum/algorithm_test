def compare_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("1")
        else:
            print("0")
    else:
        print("0")
        
        
def main():
    year = int(input())
    compare_year(year)
    
    
if __name__ == '__main__':
    main()