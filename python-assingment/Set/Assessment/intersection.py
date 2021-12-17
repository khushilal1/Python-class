from types import _StaticFunctionType


# write a python program to find the intersecgion elemnt in given two set



l1=(1,275,7,9.0,6,3,2,45.6)
l2=(1,275,7,45.6)
s1=set(l1)
s2=set(l2)
i=s1.intersection(s2)

if(s1.intersection(s2)):
    print(f"the given two set have common elemnt be:{i}")
else:
    print("the given two set have no any  common elemnt")
