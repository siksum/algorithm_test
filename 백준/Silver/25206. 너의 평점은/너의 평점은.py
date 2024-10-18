def main():
    gpa_dict = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F': 0.0
    }
    total_score = 0
    total_credit = 0
    
    for i in range(20):
        name, credit, gpa = input().split()
        
        if gpa == 'P':
            continue
        
        total_credit += float(credit)
        total_score += float(credit) * gpa_dict[gpa] 
    
    print(round(total_score/total_credit, 6))
            
if __name__ == '__main__':
    main()