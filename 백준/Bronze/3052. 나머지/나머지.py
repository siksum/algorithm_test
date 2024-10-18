def main():
    arr = [int(input()) for _ in range(10)]
    
    remainders = [i % 42 for i in arr]
    
    print(len(set(remainders)))
    
    
if __name__ == '__main__':
    main()