import random
import string
S1 = list(string.ascii_uppercase + string.ascii_lowercase)
S2 = list(string.digits + string.punctuation )
random.shuffle(S1)
random.shuffle(S2)
PASS_NUMBER = input("enter Number of password characters:")
while True:
    try:
        PASS_NUMBER = int(PASS_NUMBER)
        if PASS_NUMBER < 6 or PASS_NUMBER > 50:
            PASS_NUMBER = int(input("Please enter Number of characters:"))
        else :
            break
    except:

        print("something wrong!")
        PASS_NUMBER = input("Please enter Number of characters:")
PASSWORD = []
N = PASS_NUMBER // 2
for i in range (0,N):
    PASSWORD.append(random.choice(S1))
for i in range (0,N):
    PASSWORD.append(random.choice(S2))
PASSWORD = "".join(PASSWORD)
print("Finally you generated you own password : ",PASSWORD)



