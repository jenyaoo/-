def f():
    a={}
    while True:
        z=input()
        if z=='':
            break
        w,e,r=z.split()
        r=int(r)
        key=w+' '+e
        a[key]=r
    return a

def get_name(a):
    for i in range(len(a)):
        if a[i]==' ':
            return a[i+1:]

q=int(input())
a=[0]*q
for i in range(q):
    z=f()
    a[i]=z
all={}
allfi={}
count=1
for i in a:
    for key in i:
        r=i[key]
        if all.get(key)==None:
            all[key]=r
            allfi[key]=str(count)+'_'+key[0]+'_'+str(len(get_name(key)))
            count+=1
        else:
            all[key]+=r


print(len(all))
for i in allfi:
    print(allfi.get(i),i)

print('Участвовали во всех олимпиадах:')
for i in a[0]:
    m=1
    for o in a:
        if o.get(i)==None:
            m=0
    if m==1:
        print(i)

o=-1
print(all)
for i in all:
    if int(all.get(i))>int(o):
        o=all.get(i)
        u=i
print(u)



