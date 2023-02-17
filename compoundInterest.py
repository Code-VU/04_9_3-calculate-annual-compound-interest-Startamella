def calculateCompoundInterest():
    solution()
    print("---")
    solution()
    print("---")
    solution()
    
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
def solution(): 
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    A = client_one_principal*(1+(client_one_rate/100))**client_one_time
    intrest = A - client_one_principal
    print("Compound Interest:  "+str(round(intrest,2)))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
