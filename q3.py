
# write a python code to compute a element wise sum of 3 tuples

t1=(1,2,3,4)
t2=(3,5,2,1)
t3=(2,2,3,1)

t4=[]
for i in range(3):
    t4.append(t1[i]+t2[i]+t3[i])

t4=tuple(t4)
print(t4)
