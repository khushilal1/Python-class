# write a program to find the max anbd min elemet of the set

print("pogram finding the smallest and  greatest elemnt in the set\n")

l1=[12,3,45,6,7,7,8,9,6,0,9,8,7,6,6,3]
s=set(l1)
def greatest():
    f=max(s)
    print(f"the graetes element in the give list be:{f}")

def smallest():
    l=min(s)
    print(f"the smalest element in the given lis be :{l}")

smallest()
greatest()
