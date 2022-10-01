# Python Program to Check if a Number is Odd or Even

def check_odd_even_number(number_input):
    result = ""
    if(number_input % 2 == 0):
        result = "input is even number"
    else:
        result = "input is odd number"

    return result;

def main():
    number_input = 3
    print(check_odd_even_number(number_input))
    

if __name__ == "__main__":
    main()