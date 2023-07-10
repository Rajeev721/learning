import random as r
def guess():
    try:
        input_number = input(f"please guess the number between 1 amd 10\n")
        guess_number = r.randint(1,10)
        cnt = 1
        while True:
            if input_number.isnumeric() and int(input_number) <20 and int(input_number) > 0:
                break
            else:
                input_number = input("please provide the number between 1 and 10 only \n")
        while cnt <=3:
            if int(input_number) == guess_number:
                print("great guess")
                break
            elif cnt == 3:
                print("sorry, your chances are over, better luck next time!")
                break
            else:
                input_number = input(f"the number is wrong, please guess the number between 1 amd 10\n")
                cnt += 1
    except Exception as e:
        print("the prgram has failed with error", e)

guess()