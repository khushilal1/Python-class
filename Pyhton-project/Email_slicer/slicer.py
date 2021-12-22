print("WELCOME TO TEH EMAIL SLICING")
print("You  can able to get your uername and domain name:")
email=input("Enter your email address:\n")
domain=email[-9:-1]
username=email.index("@")
user_name=email[0:username]
print(f"The username  of your email is :{user_name}")
print(f"The domain  name of your email is :{domain}")