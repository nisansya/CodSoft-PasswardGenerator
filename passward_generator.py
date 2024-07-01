import random
import string
def generate_passward(length):
    letters=string.ascii_letters
    digits=string.digits
    punc=string.punctuation
    alphabet=letters+digits+punc
    random_passward=random.sample(alphabet,length)
    passward="".join(random_passward)
    print(passward)

print("-------------PASSWARD GENERATOR-------------")
length=int(input("Enter the length of the passward :"))
generate_passward(length)