def analyze_numbers(manamba,sum):
    manamba = [20,48,7,84,93,74]
    sum = manamba[0] + manamba[1]+ manamba[2]+ manamba[3]+ manamba[4]+ manamba[5]
    if sum/6> 50:
        print("Above avarage")
    elif sum == 50:
        print("Average")
    elif sum < 50:
        print("Below avarage")
        analyze_numbers
        
        analyze_numbers(None,None)analyze_numbers
        analyze_numbers(None,None)

