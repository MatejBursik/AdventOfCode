import time

a = list(map(lambda a:[False,False,False,False,False,False,False],range(10000)))
a[50][1] = True

timer = time.time()
for i,level in enumerate(a):
    for l in level:
        if l:
            print(i,level,len(a))
            break
print(time.time()-timer)

timer = time.time()
for i,level in enumerate(a):
    if True in level:
        print(i,level,len(a))
        break
print(time.time()-timer)

