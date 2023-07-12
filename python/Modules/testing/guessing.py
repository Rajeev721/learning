import random as r
def guess(input_number,guess_number):
    try:
        cnt = 1
        while True:
            if input_number.isnumeric() and int(input_number) <10 and int(input_number) > 0:
                break
            else:
                input_number = input("please provide the number between 1 and 10 only \n")
        while cnt <=3:
            if int(input_number) == int(guess_number):
                print("great guess")
                return True
            elif cnt == 3:
                return Exception
            else:
                input_number = input(f"the number is wrong, please guess the number between 1 amd 10\n")
                cnt += 1
    except Exception as e:
        print("the program has failed with error", e)



if __name__ == "__main__":
    guess_number = r.randint(1,10)
    print(guess_number)
    input_number = input(f"please guess the number between 1 and 10\n")
    print
    try:        
        if guess(input_number,guess_number):
            pass
        else:
            print("sorry, your chances are over, better luck next time!")
    except Exception:
        raise ValueError