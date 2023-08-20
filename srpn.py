#This is your SRPN file. Make your changes here.
import re

#Intializes the empty stack.
stack = []
#Created a name for the limits of calculator.
maxnum = 2147483647
minnum = -2147483648
#Created the list of random numbers when 'r' is inputted in the SRPN calculator.
randomnum = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]
#Variable that stores how far along the randomnum list we are.
randomnumcounter = 0
#List of all unrecognised symbols in the SRPN calculator.
Unrecognisedinputs= ['a' , 'b' , 'c' , 'e' , 'f' , 'g' , 'h' , 'i', 'j' , 'k' , 'l', 'm' , 'n' , 'o' , 'p' , 'q' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ,'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I', 'J' , 'K' , 'L', 'M' , 'N' , 'O' , 'P' , 'Q' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' , '!' , "@" , "£" , '$' , '(' , ')' , '_' , '§' , '±' , '`' , '~' , ',' , '<' , '>' ,'.' , '?' , ';' , ':' , '"' , "'" , '|' , '{' , ' }' , ' [' , ']']

#Function that prints a stack overflow if its beyond 23, else it 'push'es the 'num'ber value to the end of the stack.
def push(num):
    if len(stack) >= 23:
        print("Stack overflow.")
    else:
        stack.append(satcheck(int(num)))

#Saturation check function that ensures inputs are within range.
def satcheck(command):
    if command >= maxnum:
        return maxnum
    elif command <= minnum:
        return minnum
    else:
        return command

#Function that does all of the calculations.
def process_command(command):
    #Seperates the letters and multiple digits number
    command =re.split(r'(^-[0-9]+|\^=|\D)', command)
    #Pushes item that has been split into a new stack called splitted.
    #Splittng process reference at @https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
    splitted = [item for item in command if item != "" and item != " "]
    #Object is now used to define what is being inputted.
    for object in splitted:
        #Checks for a stack underflow depending on the length of the stack.
        if object in "+-/*^%" and len(stack)<=1:
            print("Stack underflow.")

        elif object == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            push(num1 + num2)

        elif object == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            push(num2 - num1)

        elif object == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            if num1 == 0:
                print("Divide by 0.")
            else:
                push(num2/num1)

        elif object == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            push(num1 * num2)

        elif object == '^':
            #If last element of stack is negative then the operation doesn't work else it works.
            if stack[-1] < 0:
                print("Negative power.")
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                push(pow(num2,num1))

        elif object == '%':
            num1 = stack.pop()
            num2 = stack.pop()
            if num2 == 0:
                print("Divide by 0.")
            else:
                push(num2 % num1)

        elif object == 'd':
            #Checks for an empty else it prints the whole stack
            if len(stack)==0:
                print(minnum)
            else:
                for i in stack:
                    print(int(i))

        elif object == 'r':
            randomnumcounter = 0
            push(randomnum[randomnumcounter])
            if randomnumcounter == 21:
                #Resets counter once it reaches the end of the randomnum list.
                randomnumcounter = 0
            else:
                #Increments counter by 1 through the list.
                randomnumcounter += 1

        elif object == "#":
            #Prevents error when '#' is inputted to allow comments.
            return 0

        elif object in Unrecognisedinputs:
            print(f"Unrecognised operator or operand \"{object}\".")

        elif object == "":
            #Prevents an error when blank space is inputted in the calculator.
            print("")

        elif object == "=":
            if len(stack)==0:
                print("Stack empty.")
            else:
                #Will print last value on the stack or stack empty if the numbers have been inputted.
                print(int(stack[-1]))

        else:
            push(object)
#This is the entry point for the program.
#It is suggested that you do not edit the below,
#to ensure your code runs with the marking script
if __name__ == "__main__":
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
        except EOFError:
            exit()
