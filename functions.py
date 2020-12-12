import random
import string

def get_random_email():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(7))
    return(result_str+'@email.com')



def is_display(a):
    if True:
        print (a, '  - displayed')
    else:
        print(a, '  - not displayed')
