def main():
    N, B = map(int, input().split())
    
    if B < 2 or B > 36:
        return    

    ans = ""
    
    while N != 0:
        if N % B > 9:
            ans += str(chr(N % B + 55))
        else:
            ans += str(chr(N % B + 48))
        N = N // B
        
    print(ans[::-1])   
  
if __name__ == '__main__':
    main()