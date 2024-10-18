def main():
    word = input()
    
    if len(word) > 1000000:
        return
    
    word_upper =word.upper()
    word_set = set(word_upper)
    
    counter = []

    for i in word_set:
       counter.append(word_upper.count(i))
    
    if counter.count(max(counter)) > 1:
        print("?")
    else:
        print(list(word_set)[counter.index(max(counter))])

        
if __name__ == '__main__':
    main()