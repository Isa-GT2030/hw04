
def divs_table(n):
    #outer loop: for i in range(1, n+1)
    for i in range(1, n+1):
        
        #print the row label
        print(f"     {i}: ", end = " ")

    #inner loop
    for j in range(1, n+1):
        
        #check if i divided by j is zero
        if i % j == 0:
            
            #if so, print j
            print(f"{j:4d}", end = "")
    print()



def main():
    num = -1
    
    while(num < 1 or num > 10):
        num = input("give me a number in [1,10]: ")
        if (not num.isdigit()):
            print("I said a NUMBER! Try again...")
            num = -1 #reset value of num
    
        num = int(num)
    divs_table(num)

if __name__ == "__main__":
    main()
    