def main():
    word = list(str(input()))

    if list(reversed(word)) == word:
        print(1)
    else:
        print(0)
        
if __name__ == '__main__':
    main()