def main():
    N = int(input())
    if N > 1000:
        return
    
    score = list(map(int, input().split()))
    if len(score) != N:
        return
    
    max_score = max(score)
    
    new_score = [s / max_score * 100 for s in score]
    print(sum(new_score) / N)
    
        
if __name__ == '__main__':
    main()