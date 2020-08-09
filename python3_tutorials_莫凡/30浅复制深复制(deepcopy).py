import copy
a = [[3,3],1,2]

# 一般copy
b = a   # id(b) = id(a)

#Shallow copy
c = copy.copy(a) #id(c) != id(a)
              #第二层： id(c[0]) = id(a[0])

#Deep copy
e = copy.deepcopy(a) #第二层id(e[0] ！= id(a[0]))
