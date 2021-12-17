

# # copy
a={1,2,3,4,54,"string"}
s1=set(a)
s2={}
s2=s1.copy()
print(s2)

# union
a={1,2,3,4,54,"string"}
s1=set(a)
s2={1,2,3,4,0,8,877}
s3=s1.union(s2)
print(s3)

#difference

s1={1,2,3,4,54,"string"}

s2={1,2,3,4,0,8,877}
s3=s1.difference(s2)  #s1-s2
print(s3)

s4=s2.difference(s1)  #s2-s1
print(s4)


#intersection

s1={1,2,3,4,54,"string"}

s2={1,2,3,4,0,8,877}
s3=s1.intersection(s2)  #s1-s2
print(s3)

#isdisjoint

s1={1,2,3,4,54,"string"}

s2={1,2,3,4,0,8,877}
s3=s1.isdisjoint(s2)  #s1-s2
print(s3)


s1={0,1,2,3,4,5,6,7,8,9}

s2={0,1,2,3,4,8,}
s3=s1.issubset(s2)  #s1-s2
print(s3)


s1={0,1,2,3,4,5,6,7,8,9}
s2={0,1,2,3,4,8,}
s3=s2.issubset(s1)  #s1-s2
print(s3)


#superset
s1={0,1,2,3,4,5,6,7,8,9}
s2={0,1,2,3,4,8,}
s3=s2.issuperset(s1)  #s1-s2
print(s3)

s1={0,1,2,3,4,5,6,7,8,9}
s2={0,1,2,3,4,8,}
s3=s2.symmetric_difference(s1)  #s1-s2
print(s3)

s1={0,1,2,3,4,5,6,7,8,9}
s2={0,1,2,3,4,8,}
s3=s2.symmetric_difference_update(s1)  #s1-s2
print(s3)