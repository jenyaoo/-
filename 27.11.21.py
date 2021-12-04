a={}
b={}
c={}
all={}
allfi={}
q=1
while True:
    z=input()
    if z=='':
        break
    w,e,r=z.split()
    r=int(r)
    key=w+' '+e[0]
    a[key]=r
    if all.get(key)==None:
        all[key]=r
        allfi[key]=str(q)+'_'+w[0]+'_'+str(len(e))
        q+=1
    else:
        all[key]+=r

while True:
    z=input()
    if z=='':
        break
    w,e,r=z.split()
    r=int(r)
    key=w+' '+e[0]
    b[key]=r
    if all.get(key)==None:
        all[key]=r
        allfi[key]=str(q)+'_'+w[0]+'_'+str(len(e))
        q+=1
    else:
        all[key]+=r

while True:
    z=input()
    if z=='':
        break
    w,e,r=z.split()
    r=int(r)
    key=w+' '+e[0]
    c[key]=r
    if all.get(key)==None:
        all[key]=r
        allfi[key]=str(q)+'_'+w[0]+'_'+str(len(e))
        q+=1
    else:
        all[key]+=r

print(len(all))
for i in allfi:
    print(allfi.get(i),i)

for i in a:
    if b.get(i)!=None and c.get(i)!=None:
        print(i)

o=-1
print(all)
for i in all:
    if int(all.get(i))>int(o):
        o=all.get(i)
        u=i
print(u)


