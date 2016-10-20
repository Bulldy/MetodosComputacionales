file=open('salida.txt','r')
l=file.readlines()
file.close()

n=len(l)

f=open('lineas.dat','w')
f.write('{}\n'.format(n))
f.close()
