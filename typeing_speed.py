from time import *
import random as r

def mistake(partest, usertest):
    partest_words = partest.split()
    usertest_words = usertest.split()
    error = 0
    for i in range(len(partest_words)):
        try:
            if partest_words[i] != usertest_words[i]:
                error += 1
        except IndexError:
            error += 1
    return error


def speed_time(time_s, time_e, userInput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    words = len(userInput.split())
    speed = (words / time_r) * 60
    return round(speed)

if __name__ == '__main__':
    while True:
        check = input("If you like to continue (yes/no): ")
        if check == 'yes':
            test = [
                "The quick brown fox jumps over the lazy dog while the sun sets behind the mountains.",
                "Technology evolves rapidly, shaping the world around us with innovations in communication, science, and daily life.",
                "A gentle breeze swept across the field, carrying the scent of fresh flowers and the promise of spring.",
                "Hard work and determination are the keys to achieving success and overcoming challenges in life’s journey.",
                "The stars twinkled brightly in the night sky, painting a serene and breathtaking view for all to admire."
            ]
            test1 = r.choice(test)
            print("typing speed".center(35, "*"))
            print(test1)
            print()
            print()
            time_s = time()
            userInput = input("Enter: ")
            time_e = time()

            print("Speed:", speed_time(time_s, time_e, userInput), "w/min")
            print("Error:", mistake(test1, userInput))
        else:
            print("Thank you....")
            break


