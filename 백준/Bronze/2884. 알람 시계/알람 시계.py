def time_setting(hour, miniute):
    if miniute < 45:
        hour -= 1
        miniute += 15
    else:
        miniute -= 45
        
    if hour < 0:
        hour = 23
        
    print(hour, miniute)
        
        
def main():
    hour, miniute = map(int, input().split())
    
    if hour < 0 or hour > 23 or miniute < 0 or miniute > 59:
        return
    
    time_setting(hour, miniute)
    
    
if __name__ == '__main__':
    main()