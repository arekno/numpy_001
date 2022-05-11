import numpy as np

a=np.arange(8)
print(a)

b=[2,3,4]
c=[6,7,8]

d=np.array([b,c])
print(d)

e=np.array([[3,4,5],[6,7,8]])
print(e)
poz1=e[1,2]
print('Element z wiersza 2 i kolumny 3 to',poz1)

f=np.array(np.mat('1,2;3,4'))
print(f)
print(e.shape,e.size,e.ndim)

g=np.array([np.arange(5),np.arange(5)])
print(g)

zera=np.zeros((3,3))
print(zera)

jedynki=np.ones((3,3))
print(jedynki)
print(jedynki*5)
print(zera.dtype,jedynki.dtype)

pusta=np.empty((2,2))
print(pusta)

h=np.arange(3,15,3)
print(h)

i=np.linspace(3,15,10)
print(i)

j=np.indices((5,5))
print(j)