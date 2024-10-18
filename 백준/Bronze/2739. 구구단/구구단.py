def calculate_multiplication_table(multiplication_table_num):
    for i in range(1, 10):
        print(f'{multiplication_table_num} * {i} = {multiplication_table_num * i}')
        
        
def main():
    multiplication_table_num =int(input())    
    calculate_multiplication_table(multiplication_table_num)
    
    
if __name__ == '__main__':
    main()