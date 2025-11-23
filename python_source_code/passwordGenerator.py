import random
import string

pas_len=12
charVal=string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits

password="".join([random.choice(charVal) for i in range(pas_len)])
# password=""
# for i in range(pas_len):
#     password+=random.choice(charVal)


print("your password is =",password)

