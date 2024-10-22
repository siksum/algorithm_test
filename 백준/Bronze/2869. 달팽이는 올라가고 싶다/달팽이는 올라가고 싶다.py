def main():
    A, B, V = map(int, input().split())
    
    #올라가는 거리 = V - B
    #하루에 올라가는 거리 = A - B
    
    if (V - B) % (A - B) == 0:
        print((V - B) // (A - B))
    else:
        print((V - B) // (A - B) + 1)
    

if __name__ == '__main__':
    main()