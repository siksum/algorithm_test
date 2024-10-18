def main():
    count = int(input())
    
    if count > 100:
        return

    word_counter = 0
    
    for i in range(count):
        word = input()
        if len(word) > 100:
            return
        
        counter = 0
        
        word_set = list(set(word))
        for j in range(len(word_set)):
            j_list = list(filter(lambda x: word[x] == word_set[j], range(len(word))))
            
            if len(j_list) > 1:
                for k in range(len(j_list)):
                    if k == 0:
                        continue
                    if j_list[k] - j_list[k-1] > 1:
                        counter -= 1
                        break
                    else:
                        continue
                counter += 1
            else:
                counter += 1
        
        if counter == len(word_set):
            word_counter += 1
    
    print(word_counter)
            
            
if __name__ == '__main__':
    main()