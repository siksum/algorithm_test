def main():
    T = int(input())
    
    for i in range(T):
        R, S = input().split()
        
        new_s = ""
        for i in range(len(S)):
            new_s +=  S[i]*int(R)
        print(new_s)
    


if __name__ == '__main__':
    main()