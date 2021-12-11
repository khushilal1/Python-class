
print("VOWEL COUNTING PROGRAM")

s1=input("Enter the string to find the no. of  vowel is present\n")
count=0
vowel=set("aeiouAEIOU")
for alphabet in s1:
    if alphabet in vowel:
        count=count+1
    else:
        continue
print(f"The no. of vowel in {s1} is :{count} ")