import random
import string

upper=string.ascii_uppercase #getting al the uppercase letter
lower=string.ascii_lowercase#getting al the lowercase letter
number=string.digits #getting al the gigit from 0 to 9
character=string.punctuation #getting al the special chareacter

n=int(input("Enter the lenght of pasword You want to generate\n"))
all =upper+lower+number+character
temp=random.sample(all,n)


password="".join(temp)
print(f"The random and strong password be is {password}")
