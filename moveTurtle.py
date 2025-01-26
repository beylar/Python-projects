import random

def angle():
    number = random.randint(-90, 90)
    return number
 
# print("in move: __name__ ==", __name__)
# print("will always execute: angle ==", angle())

if __name__ == "__main__":
    print("only if True: angle ==", angle())
    print("in move: __name__ ==", __name__)
    print("will always execute: angle ==", angle())

