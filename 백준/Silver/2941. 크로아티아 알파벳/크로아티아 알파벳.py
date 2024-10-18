def main():
    word = input()
    
    if len(word) > 100:
        return
    
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    
    for i in croatia:
        word = word.replace(i, 'a')
        
    print(len(word))        
    
if __name__ == '__main__':
    main()