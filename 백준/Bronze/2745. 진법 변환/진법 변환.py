def main():
    
    N, B = input().split()
    B = int(B)
    
    if B < 2 or B > 36:
        return    

    ans = 0
    
    for i in range(len(N)):
        ans = ans * B + int(N[i], B)
    
    N = str(ans)
        
    print(N)    
  
if __name__ == '__main__':
    main()