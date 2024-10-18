def main():
    while True:
        try:
            str_input = input()
            print(str_input)
        except EOFError:
            break
        
if __name__ == '__main__':
    main()