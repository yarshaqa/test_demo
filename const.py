from functions import random_email
from functions import random_name_surname
from functions import random_pass

name = '/html/body/div/div/div[2]/form/div[1]/input'
surname = '/html/body/div/div/div[2]/form/div[2]/input'
email = '/html/body/div/div/div[2]/form/div[3]/input'
phone = '/html/body/div/div/div[2]/form/div[4]/input'
password = '/html/body/div/div/div[2]/form/div[5]/input'
submit_password = '/html/body/div/div/div[2]/form/div[6]/input'
submit = '/html/body/div/div/div[2]/form/div[8]/button'
checkbox = '/html/body/div/div/div[2]/form/div[7]/label/input'



email_value = random_email()
name_value = random_name_surname()
pass_value = random_pass()