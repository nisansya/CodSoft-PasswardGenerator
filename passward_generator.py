import random
import string
def generate_password(length):
    letters=string.ascii_letters
    digits=string.digits
    punc=string.punctuation
    alphabet=letters+digits+punc
    random_password=random.sample(alphabet,length)
    password="".join(random_password)
    print(password)

print("-------------PASSWORD GENERATOR-------------")
length=int(input("Enter the length of the password :"))
generate_password(length)
