#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    DailyEarn=[] #initializes daily earn variable
    
    for counter in range(1,6): #makes sure only 1-5 are printed for days
       Earn=float(input(f"Enter the amounter earned for day {counter}: ")) #input field for daily earnings
       DailyEarn.append(Earn) #stores each days earnings 
    
    print(DailyEarn) #prints stored values
        
        






    # YOUR CODE ENDS HERE
main()