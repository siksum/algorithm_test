def calculate_cook_time(hour, miniute, cook_time):
    
    miniute += cook_time
    
    if miniute >= 60:
        hour += miniute // 60
        miniute = miniute % 60
        
    if hour >= 24:
        hour = hour % 24

    print(hour, miniute)
        
        
def main():
    hour, miniute = map(int, input().split())
    
    if hour < 0 or hour > 23 or miniute < 0 or miniute > 59:
        return
    
    cook_time = int(input())
    
    if cook_time < 0 or cook_time > 1000:
        return
    
    calculate_cook_time(hour, miniute, cook_time)
    
    
if __name__ == '__main__':
    main()