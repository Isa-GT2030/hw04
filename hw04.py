# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():

    #I set up a while loop that is always true
    while True:
        #I define sentence1 as a variable equal to the user input of "Give me a sentence: "
        sentence1 = input("Give me a sentence: ").lower()
        
        # I say if the word "dog" is in the sentence, print "You used the word dog" and break the loop
        if "dog" in sentence1:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        
    
        # I say if the word "food" is in the sentence, print "You used the word dog" and break the loop
        elif secret_word in sentence1:
            print("You used the secret word!")
            break
        
    
        # I say if neither "food" nor "dog" is in the sentence, print "Try again" and re-start the loop
        else:
            print("Try again.")
        
    
    



# Task 2
def check_greater():
    
    
    #I create a while loop that is always true
    while True:
        #I define num1 as a variable equal to the user input of "Give me a first integer: "
        num1 = int(input("Give me a first integer: "))
        
        #I define num2 as a variable equal to the user input of "Give me a second integer: "
        num2 = int(input("Give me a second integer: "))
        
        
        #if num1 is greater than num2, print "First is Greater" and break out the loop
        if num1 > num2:
            print("First is Greater")
            break
        
        #else if num2 is greater than num1, print "Second is Greater" and break out the loop
        elif num2 > num1:
            print("Second is Greater")
            break
        
        #if any other condition is true, print "Try again" and restart the loop
        else:
            print("Try again")
        



# Task 3
def get_special_numbers():
    
    #Skip all numbers even numbers in the range 1 to 40
    for num in range(1,40):
        if num %2 == 0:
            continue
        
        #skip all numbers not divisible by three in the range 1 to 40
        if num %3 != 0:
            continue
        
        #skip all numbers not divisible by 5 in the range 1 to 40
        if num %5 == 0:
            continue
        
        #if the number doesn't meet any of the above conditions, print it 
        else:
            print(num)

        


# Task 4.a
def my_for_loop():
    
    
    #I define string as a variable equal to the user input of "Give me a string: "
    string = input("Give me a string: ")
    
    #I define vowels as any letter A, E, I, O, U
    vowels = "AaEeIiOoUu"
    
    #if there's a space in string or string is less than 2 or greater than 5, print bad word and return
    if " " in string or len(string) <2 or len(string)>5:
        print("bad word")
        return
    
    #for all letters in string, check if every letter is a vowel or a consonant
    for letter in string:
        
        #if a letter is a vowel, print "Letter __ is a vowel"
        if letter in vowels:
            print("letter", letter, "is a vowel")
        
        #if a letter is a consonant, print "Letter __ is a consonant"
        else:
            print("letter", letter, "is a consonant")
        
        

# Task 4.b
def my_while_loop():
    
    #while loop that is always true
    while True:
        choice = input("Choose one option: a, b, or c: ")
        
        #if the user types "a", print "Try again"
        if choice == "a":
            print("Try again")
        
        #if the user types "b", print "Goodbye" and return
        elif choice == "b":
            print("Goodbye")
            return
        
        #if the user types "c", exit the whole code
        elif choice == "c":
            exit()
        
        #if the user input is not a, b, or c, print "Try again"
        else:
            print("try again")
    


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
