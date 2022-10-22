

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Enter a year:"))
    if is_leap_year(year):
        print("Leap year")
    else:
        print("Not a Leap year")

if __name__ == "__main__":
    main()
