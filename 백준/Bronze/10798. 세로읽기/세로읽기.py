def main():
    arr = [input() for _ in range(5)]
    
    str = ''
            
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):
                str += arr[j][i]
    
    print(str)
    
if __name__ == '__main__':
    main()