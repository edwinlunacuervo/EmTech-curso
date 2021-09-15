#############Favor de trabajar con el archivo listas_lifestore.py, ya que cambie el nombre de las listas originales.####
from operator import itemgetter
from listas_lifestore import *  

ventas_ordenmens=[]

####Añado a las listas en la lista de productos una entrada que corresponda al mes
for k in ventas_prod:

  mes=int(k[3][3:5])
  k.append(mes)
  #print(k)

for k in ventas_prod:
  ventas_ordenmens.append(k)
  #print(k)

ventas_ordenmens=sorted(ventas_ordenmens, key=itemgetter(5))
#####ordeno por mes

#####declaro variables para meter los elementos en la lista del mes correspondiente
enero=[]
febrero=[]
marzo=[]
abril=[]
mayo=[]
junio=[]
julio=[]
agosto=[]
septiembre=[]
octubre=[]
noviembre=[]
diciembre=[]

#Veo los reembolsos que hay en un mes
eneroreem=[]
febreroreem=[]
marzoreem=[]
abrilreem=[]
mayoreem=[]
junioreem=[]
julioreem=[]
agostoreem=[]
septiembrereem=[]
octubrereem=[]
noviembrereem=[]
diciembrereem=[]


#añado los reembolsos a las listas, junto con otros datos
for k in ventas_ordenmens:

  if k[4]==1 and k[5]==1:

    eneroreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==2:

    febreroreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==3:

    marzoreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==4:

    abrilreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==5:

    mayoreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==6:

    junioreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==7:

    julioreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==8:

    agostoreem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==9:

    septiembrereem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==10:

    octubrereem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==11:

    noviembrereem.append([k[1],k[2],k[4]]) 

  if k[4]==1 and k[5]==12:

    diciembrereem.append([k[1],k[2],k[4]]) 

#Añado las ventas  a los meses incluyendo reembolsos
for k in ventas_ordenmens:

  if k[5]==1:

    enero.append([k[1],k[2],k[4]]) 

  if k[5]==2:

    febrero.append([k[1],k[2],k[4]]) 

  if k[5]==3:

    marzo.append([k[1],k[2],k[4]]) 

  if k[5]==4:

    abril.append([k[1],k[2],k[4]]) 

  if k[5]==5:

    mayo.append([k[1],k[2],k[4]]) 

  if k[5]==6:

    junio.append([k[1],k[2],k[4]]) 

  if k[5]==7:

    julio.append([k[1],k[2],k[4]]) 

  if k[5]==8:

    agosto.append([k[1],k[2],k[4]]) 

  if k[5]==9:

    septiembre.append([k[1],k[2],k[4]]) 

  if k[5]==10:

    octubre.append([k[1],k[2],k[4]]) 

  if k[5]==11:

    noviembre.append([k[1],k[2],k[4]]) 

  if k[5]==12:

    diciembre.append([k[1],k[2],k[4]]) 


#Hago un bucle para restar los rembolsos a cada mes, menos a octubre y diciembre, ya que no hay ventas
mese=1

while 13>mese and (mese!=12 and mese!=10):

  if mese==1:
    mes=enero
    mesreem=eneroreem

  elif mese==2:
    mes=febrero
    mesreem=febreroreem

  elif mese==3:
    mes=marzo
    mesreem=marzoreem

  elif mese==4:
    mes=abril
    mesreem=abrilreem

  elif mese==5:
    mes=mayo
    mesreem=mayoreem

  elif mese==6:
    mes=junio
    mesreem=junioreem

  elif mese==7:
    mes=julio
    mesreem=julioreem

  elif mese==8:
    mes=agosto
    mesreem=agostoreem

  elif mese==9:
    mes=septiembre
    mesreem=septiembrereem

  elif mese==10:
    mes=octubre
    mesreem=octubrereem

  elif mese==11:
    mes=noviembre
    mesreem=noviembrereem

  elif mese==12:
    mes=diciembre
    mesreem=diciembrereem

  contador=1
  idventa=0

  cuentas_lista=[1]
  ####cuento las diferencias entre posiciones de la primera y la ultima venta en cada mes para ubicar las posiciones, hacer una diferencia e identificar el numero de ventas de un producto en un mes
  while len(mes)-1>idventa:
    
    if mes[idventa][0]-mes[idventa+1][0]==0:

      contador=contador+1
      idventa=idventa+1
      cuentas_lista.append(contador)

    else:
      contador=1
      idventa=idventa+1
      cuentas_lista.append(contador)
  ##################
  x_mes=0

  mes_vent=[]
  ####añado las posiciones de las ventas a una lista nediante comparaciones entre un elemento y el siguiente
  while len(cuentas_lista)-1>x_mes:

    if cuentas_lista[x_mes]>=cuentas_lista[x_mes+1]:
      mes_vent.append(cuentas_lista[x_mes])
      x_mes=x_mes+1


    else:
      x_mes=x_mes+1


  #añado el último numero relacionado con la venta del ultimo prodcuto, ya que no habra elemento siguiente para comparar
  if cuentas_lista[len(cuentas_lista)-1]==1:

    mes_vent.append(1)

  else:

    mes_vent.append(cuentas_lista[len(cuentas_lista)-1])
  ###########  


  xx_mes=0
  mes_ord=[]

  while len(mes_vent)>xx_mes:
    
    vv=mes_vent[xx_mes]
    vv+=sum(mes_vent[0:xx_mes])
    
    mes_ord.append([mes_vent[xx_mes],mes[vv-1][0]])
    xx_mes=xx_mes+1
  ######
  xrem=0
  xmesord=0


  if len(mesreem)!=0:

    for k in mes_ord:

      if k[1]==mesreem[xrem][0]:

        k[0]=k[0]-1
  ####ordeno por numero de ventas
  mes_ord=sorted(mes_ord, key=itemgetter(0))
    
  #####asigno los meses
  if mese==1:
    enero_ord=mes_ord
    
  elif mese==2:
    febrero_ord=mes_ord

  elif mese==3:
    marzo_ord=mes_ord

  elif mese==4:
    abril_ord=mes_ord

  elif mese==5:
    mayo_ord=mes_ord

  elif mese==6:
    junio_ord=mes_ord

  elif mese==7:
    julio_ord=mes_ord

  elif mese==8:
    agosto_ord=mes_ord

  elif mese==9:
    septiembre_ord=mes_ord

  elif mese==11:
    noviembre_ord=mes_ord


  if mese==9 or mese==12:
    octubre_ord=[]
    diciembre_ord=[]
    mese=mese+2

  else:
    mese=mese+1

####Hago una lista de ceros para poder comparar lista a lista.
o=0

ceros=[]

z=range(1,97)

for k in z:
  
  ceros.append([0,k])

numero=0


####Hago una lista nueva a la que le añadire los ceros
enero_ordceros=enero_ord
febrero_ordceros=febrero_ord
marzo_ordceros=marzo_ord
abril_ordceros=abril_ord
mayo_ordceros=mayo_ord
junio_ordceros=junio_ord
julio_ordceros=julio_ord
agosto_ordceros=agosto_ord
septiembre_ordceros=septiembre_ord
octubre_ordceros=octubre_ord
noviembre_ordceros=noviembre_ord
diciembre_ordceros=diciembre_ord

#añado por conviencia el ultimo producto que no tiene ninguna venta
enero_ordceros.append([0,96])
febrero_ordceros.append([0,96])
marzo_ordceros.append([0,96])
abril_ordceros.append([0,96])
mayo_ordceros.append([0,96])
mayo_ordceros.remove([1,31])
junio_ordceros.append([0,96])
julio_ordceros.append([0,96])
agosto_ordceros.append([0,96])
septiembre_ordceros.append([0,96])
octubre_ordceros.append([0,96])
noviembre_ordceros.append([0,96])
diciembre_ordceros.append([0,96])

######Hago un bucle para meter los elementos que no tienen ventas a cada mes y reacomodo para que ahora esten ordenados por numoer de producto y no por ventas. Esto para todos los meses

while o<95:

  if ceros[o][1]!=enero_ordceros[o][1]:
    enero_ordceros.append([0,ceros[o][1]])      
    o=o+1
    enero_ordceros=sorted(enero_ordceros, key=itemgetter(1))

  else:
    enero_ordceros=sorted(enero_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0
while 96>x1:    
  if enero_ordceros[x1][1]==productos[x1][0]:
    enero_ordceros[x1].append(productos[o][1])
    enero_ordceros[x1].append(productos[o][2])
    enero_ordceros[x1].append(productos[o][3])
    enero_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1
enero_ordceros=sorted(enero_ordceros, key=itemgetter(0))

o=0

while o<95:

  if ceros[o][1]!=febrero_ordceros[o][1]:
    febrero_ordceros.append([0,ceros[o][1]])      
    o=o+1
    febrero_ordceros=sorted(febrero_ordceros, key=itemgetter(1))

  else:
    febrero_ordceros=sorted(febrero_ordceros, key=itemgetter(1))
    o=o+1


x1=0
o=0 
while 96>x1:    
  if febrero_ordceros[x1][1]==productos[x1][0]:
    febrero_ordceros[x1].append(productos[o][1])
    febrero_ordceros[x1].append(productos[o][2])
    febrero_ordceros[x1].append(productos[o][3])
    febrero_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

febrero_ordceros=sorted(febrero_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=marzo_ordceros[o][1]:
    marzo_ordceros.append([0,ceros[o][1]])      
    o=o+1
    marzo_ordceros=sorted(marzo_ordceros, key=itemgetter(1))

  else:
    marzo_ordceros=sorted(marzo_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0
    
while 96>x1:    
  if marzo_ordceros[x1][1]==productos[x1][0]:
    marzo_ordceros[x1].append(productos[o][1])
    marzo_ordceros[x1].append(productos[o][2])
    marzo_ordceros[x1].append(productos[o][3])
    marzo_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

marzo_ordceros=sorted(marzo_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=abril_ordceros[o][1]:
    abril_ordceros.append([0,ceros[o][1]])      
    o=o+1
    abril_ordceros=sorted(abril_ordceros, key=itemgetter(1))

  else:
    abril_ordceros=sorted(abril_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0  
while 96>x1:    
  if abril_ordceros[x1][1]==productos[x1][0]:
    abril_ordceros[x1].append(productos[o][1])
    abril_ordceros[x1].append(productos[o][2])
    abril_ordceros[x1].append(productos[o][3])
    abril_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

abril_ordceros=sorted(abril_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=mayo_ordceros[o][1]:
    mayo_ordceros.append([0,ceros[o][1]])      
    o=o+1
    mayo_ordceros=sorted(mayo_ordceros, key=itemgetter(1))

  else:
    mayo_ordceros=sorted(mayo_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0  
while 96>x1:    
  if mayo_ordceros[x1][1]==productos[x1][0]:
    mayo_ordceros[x1].append(productos[o][1])
    mayo_ordceros[x1].append(productos[o][2])
    mayo_ordceros[x1].append(productos[o][3])
    mayo_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

mayo_ordceros=sorted(mayo_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=junio_ordceros[o][1]:
    junio_ordceros.append([0,ceros[o][1]])      
    o=o+1
    junio_ordceros=sorted(junio_ordceros, key=itemgetter(1))

  else:
    junio_ordceros=sorted(junio_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0
while 96>x1:    
  if junio_ordceros[x1][1]==productos[x1][0]:
    junio_ordceros[x1].append(productos[o][1])
    junio_ordceros[x1].append(productos[o][2])
    junio_ordceros[x1].append(productos[o][3])
    junio_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

junio_ordceros=sorted(junio_ordceros, key=itemgetter(0))
o=1
while o<95:

  if ceros[o][1]!=julio_ordceros[o][1]:
    julio_ordceros.append([0,ceros[o][1]])      
    o=o+1
    julio_ordceros=sorted(julio_ordceros, key=itemgetter(1))

  else:
    julio_ordceros=sorted(julio_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0   
while 96>x1:    
  if julio_ordceros[x1][1]==productos[x1][0]:
    julio_ordceros[x1].append(productos[o][1])
    julio_ordceros[x1].append(productos[o][2])
    julio_ordceros[x1].append(productos[o][3])
    julio_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

julio_ordceros=sorted(julio_ordceros, key=itemgetter(0))
o=0

while o<95:

  if ceros[o][1]!=agosto_ordceros[o][1]:
    agosto_ordceros.append([0,ceros[o][1]])      
    o=o+1
    agosto_ordceros=sorted(agosto_ordceros, key=itemgetter(1))

  else:
    agosto_ordceros=sorted(agosto_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0   
while 96>x1:    
  if agosto_ordceros[x1][1]==productos[x1][0]:
    agosto_ordceros[x1].append(productos[o][1])
    agosto_ordceros[x1].append(productos[o][2])
    agosto_ordceros[x1].append(productos[o][3])
    agosto_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

agosto_ordceros=sorted(agosto_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=septiembre_ordceros[o][1]:
    septiembre_ordceros.append([0,ceros[o][1]])      
    o=o+1
    septiembre_ordceros=sorted(septiembre_ordceros, key=itemgetter(1))

  else:
    septiembre_ordceros=sorted(septiembre_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0    
while 96>x1:    
  if septiembre_ordceros[x1][1]==productos[x1][0]:
    septiembre_ordceros[x1].append(productos[o][1])
    septiembre_ordceros[x1].append(productos[o][2])
    septiembre_ordceros[x1].append(productos[o][3])
    septiembre_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

septiembre_ordceros=sorted(septiembre_ordceros, key=itemgetter(0))
o=0
while o<95:

  if ceros[o][1]!=noviembre_ordceros[o][1]:
    noviembre_ordceros.append([0,ceros[o][1]])      
    o=o+1
    noviembre_ordceros=sorted(noviembre_ordceros, key=itemgetter(1))

  else:
    noviembre_ordceros=sorted(noviembre_ordceros, key=itemgetter(1))
    o=o+1

x1=0
o=0
    
while 96>x1:    
  if noviembre_ordceros[x1][1]==productos[x1][0]:
    noviembre_ordceros[x1].append(productos[o][1])
    noviembre_ordceros[x1].append(productos[o][2])
    noviembre_ordceros[x1].append(productos[o][3])
    noviembre_ordceros[x1].append(productos[o][4])
  x1=x1+1
  o=o+1

noviembre_ordceros=sorted(noviembre_ordceros, key=itemgetter(0))

################Listas con todas las ventas ordenadas de menor a mayor ventas######
enero_finalv=[]
febrero_finalv=[]
marzo_finalv=[]
abril_finalv=[]
mayo_finalv=[]
junio_finalv=[]
julio_finalv=[]
agosto_finalv=[]
septiembre_finalv=[]
noviembre_finalv=[]

for k in enero_ordceros:
  if k[0]!=0:

    enero_finalv.append(k)

for k in febrero_ordceros:
  if k[0]!=0:

    febrero_finalv.append(k)

for k in marzo_ordceros:
  if k[0]!=0:

    marzo_finalv.append(k)

for k in abril_ordceros:
  if k[0]!=0:

    abril_finalv.append(k)

for k in mayo_ordceros:
  if k[0]!=0:

    mayo_finalv.append(k)

for k in junio_ordceros:
  if k[0]!=0:

    junio_finalv.append(k)

for k in julio_ordceros:
  if k[0]!=0:

    julio_finalv.append(k)

for k in agosto_ordceros:
  if k[0]!=0:

    agosto_finalv.append(k)

for k in septiembre_ordceros:
  if k[0]!=0:

    septiembre_finalv.append(k)

for k in noviembre_ordceros:
  if k[0]!=0:

    noviembre_finalv.append(k)

########volver a ordenar por producto y sumar todas las primeras entradas para poder tener los totales anuales
 
enero_ordceros=sorted(enero_ordceros, key=itemgetter(1))
febrero_ordceros=sorted(febrero_ordceros, key=itemgetter(1))
marzo_ordceros=sorted(marzo_ordceros, key=itemgetter(1))
abril_ordceros=sorted(abril_ordceros, key=itemgetter(1))
mayo_ordceros=sorted(mayo_ordceros, key=itemgetter(1))
junio_ordceros=sorted(junio_ordceros, key=itemgetter(1))
julio_ordceros=sorted(julio_ordceros, key=itemgetter(1))
agosto_ordceros=sorted(agosto_ordceros, key=itemgetter(1))
septiembre_ordceros=sorted(septiembre_ordceros, key=itemgetter(1))
noviembre_ordceros=sorted(noviembre_ordceros, key=itemgetter(1))


#################VENTAS ANUALES
t=0
totallist=[]

while t<96:

  total=enero_ordceros[t][0]+febrero_ordceros[t][0]+marzo_ordceros[t][0]+abril_ordceros[t][0]+mayo_ordceros[t][0]+junio_ordceros[t][0]+julio_ordceros[t][0]+agosto_ordceros[t][0]+septiembre_ordceros[t][0]+noviembre_ordceros[t][0]

  totallist.append([total,productos[t][0],productos[t][1],productos[t][2],productos[t][3],productos[t][4]])

  t=t+1
  
###########VENTAS ANUALES (Variable: totallist)


######Por categoria. Hago una lista para cada mes
enero_finalcat=[]
febrero_finalcat=[]
marzo_finalcat=[]
abril_finalcat=[]
mayo_finalcat=[]
junio_finalcat=[]
julio_finalcat=[]
agosto_finalcat=[]
septiembre_finalcat=[]
noviembre_finalcat=[]
####Hago una lista de todas las categorias
p=0
categ=[]
while p<95:

  if productos[p][3]!=productos[p+1][3]:
    categ.append(productos[p][3])
    p=p+1
  else:
    p=p+1
####por conveniencia añado audifonos
categ.append("audifonos")
 ####Hago un bucle para comparar las ventas de cada producto con la categoria y sumar el total de ventas, haciendo una lista al final donde añado ventas y categorias 
pm=1

while pm<13:
  procesadores=0
  tarjetas_de_video=0
  tarjetas_madre=0
  discos_duros=0
  memorias_usb=0
  pantallas=0
  bocinas=0
  audifonos=0

  if pm==1:
    mes_finalcat=enero_finalcat
    mes_finalv=enero_finalv
  if pm==2:
    mes_finalcat=febrero_finalcat
    mes_finalv=febrero_finalv
  if pm==3:
    mes_finalcat=marzo_finalcat
    mes_finalv=marzo_finalv
  if pm==4:
    mes_finalcat=abril_finalcat
    mes_finalv=abril_finalv
  if pm==5:
    mes_finalcat=mayo_finalcat
    mes_finalv=mayo_finalv
  if pm==6:
    mes_finalcat=junio_finalcat
    mes_finalv=junio_finalv
  if pm==7:
    mes_finalcat=julio_finalcat
    mes_finalv=julio_finalv
  if pm==8:
    mes_finalcat=agosto_finalcat
    mes_finalv=agosto_finalv
  if pm==9:
    mes_finalcat=septiembre_finalcat
    mes_finalv=septiembre_finalv

  for k in mes_finalv:
    if k[4]==categ[0]:
      procesadores=procesadores+k[0]
    elif k[4]==categ[1]:
      tarjetas_de_video=tarjetas_de_video+k[0]
    elif k[4]==categ[2]:
      tarjetas_madre=tarjetas_madre+k[0]
    elif k[4]==categ[3]:  
      discos_duros=discos_duros+k[0]
    elif k[4]==categ[4]:
      memorias_usb=memorias_usb+k[0]
    elif k[4]==categ[5]:
      pantallas=pantallas+k[0]
    elif k[4]==categ[6]:
      bocinas=bocinas+k[0]
    elif k[4]==categ[7]:
      audifonos=audifonos+k[0]
    
  mes_finalcat.append(["procesadores",procesadores])
  mes_finalcat.append(["tarjetas de video",tarjetas_de_video])
  mes_finalcat.append(["tarjetas madre",tarjetas_madre])
  mes_finalcat.append(["discos duros",discos_duros])
  mes_finalcat.append(["memorias usb",memorias_usb])
  mes_finalcat.append(["pantallas",pantallas])
  mes_finalcat.append(["bocinas",bocinas])
  mes_finalcat.append(["audifonos",audifonos])
  pm=pm+1

zz=0
totalcat=[]
while zz<8:
  totalcat.append([enero_finalcat[zz][0] ,enero_finalcat[zz][1]+febrero_finalcat[zz][1]+marzo_finalcat[zz][1]+abril_finalcat[zz][1]+mayo_finalcat[zz][1]+junio_finalcat[zz][1]+julio_finalcat[zz][1]+agosto_finalcat[zz][1]])
  zz=zz+1



totalcat=sorted(totalcat, key=itemgetter(1))
enero_finalcat=sorted(enero_finalcat, key=itemgetter(1))
febrero_finalcat=sorted(febrero_finalcat, key=itemgetter(1))
marzo_finalcat=sorted(marzo_finalcat, key=itemgetter(1))
abril_finalcat=sorted(abril_finalcat, key=itemgetter(1))
mayo_finalcat=sorted(mayo_finalcat, key=itemgetter(1))
junio_finalcat=sorted(junio_finalcat, key=itemgetter(1))
julio_finalcat=sorted(julio_finalcat, key=itemgetter(1))
agosto_finalcat=sorted(agosto_finalcat, key=itemgetter(1))



#####Calificaciones promedio
####Extraemos los datos de las ventas que corresponden a cada mes y en la última aparición de la venta la segunda entrada será la calificación promediada. Posteriormente se anexan a una lista (califord) únicamente el identificador del producto y la calificacion promedio

xe=0
enero_calif=[]
s=0
count=1
while len(enero)-1>=xe:

  if xe==len(enero)-1 and enero[len(enero)-1][0]!=enero[len(enero)-2][0]:
    enero_calif.append([enero[len(enero)-1][0],enero[len(enero)-1][1]])
    xe=xe+1
    
  elif enero[xe][0]==enero[xe+1][0]:
    s=s+enero[xe][1]
    enero_calif.append([enero[xe][0],s])
    xe=xe+1
    count=count+1
  elif enero[xe][0]<enero[xe+1][0]:
    s=s+enero[xe][1]
    enero_calif.append([enero[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
enero_califord=[]

while x<len(enero_calif)-1:
  if enero_calif[x][0]!=enero_calif[x+1][0]:
    enero_califord.append([enero_calif[x][0],enero_calif[x][1]])
    x=x+1
  else:
    x=x+1

if enero_calif[len(enero_calif)-1] and enero_calif[len(enero_calif)-1][0]!=enero_calif[len(enero_calif)-2][0]:
  enero_califord.append([enero_calif[len(enero_calif)-1][0],enero_calif[len(enero_calif)-1][1]])
#######
xe=0
febrero_calif=[]
s=0
count=1
while len(febrero)-1>xe:

  if xe==len(febrero)-1 and febrero[len(febrero)-1][0]!=febrero[len(febrero)-2][0]:
    febrero_calif.append([febrero[len(febrero)-1][0],febrero[len(febrero)-1][1]])
    xe=xe+1
    
  elif febrero[xe][0]==febrero[xe+1][0]:
    s=s+febrero[xe][1]
    febrero_calif.append([febrero[xe][0],s])
    xe=xe+1
    count=count+1
  elif febrero[xe][0]<febrero[xe+1][0]:
    s=s+febrero[xe][1]
    febrero_calif.append([febrero[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
febrero_califord=[]

while x<len(febrero_calif)-1:
  if febrero_calif[x][0]!=febrero_calif[x+1][0]:
    febrero_califord.append([febrero_calif[x][0],febrero_calif[x][1]])
    x=x+1
  else:
    x=x+1

if febrero_calif[len(febrero_calif)-1][0]!=febrero_calif[len(febrero_calif)-2][0]:
  febrero_califord.append([febrero_calif[len(febrero_calif)-1][0],febrero_calif[len(febrero_calif)-1][1]])


#######
xe=0
marzo_calif=[]
s=0
count=1
while len(marzo)-1>=xe:

  if xe==len(marzo)-1 and marzo[len(marzo)-1][0]!=marzo[len(marzo)-2][0]:
    marzo_calif.append([marzo[len(marzo)-1][0],marzo[len(marzo)-1][1]])
    xe=xe+1
    
  elif marzo[xe][0]==marzo[xe+1][0]:
    s=s+marzo[xe][1]
    marzo_calif.append([marzo[xe][0],s])
    xe=xe+1
    count=count+1
  elif marzo[xe][0]<marzo[xe+1][0]:
    s=s+marzo[xe][1]
    marzo_calif.append([marzo[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
marzo_califord=[]

while x<len(marzo_calif)-1:
  if marzo_calif[x][0]!=marzo_calif[x+1][0]:
    marzo_califord.append([marzo_calif[x][0],marzo_calif[x][1]])
    x=x+1
  else:
    x=x+1

if marzo_calif[len(marzo_calif)-1][0]!=marzo_calif[len(marzo_calif)-2][0]:
  marzo_califord.append([marzo_calif[len(marzo_calif)-1][0],marzo_calif[len(marzo_calif)-1][1]])


##########
xe=0
abril_calif=[]
s=0
count=1
while len(abril)-1>=xe:

  if xe==len(abril)-1 and abril[len(abril)-1][0]!=abril[len(abril)-2][0]:
    abril_calif.append([abril[len(abril)-1][0],abril[len(abril)-1][1]])
    xe=xe+1
    
  elif abril[xe][0]==abril[xe+1][0]:
    s=s+abril[xe][1]
    abril_calif.append([abril[xe][0],s])
    xe=xe+1
    count=count+1
  elif abril[xe][0]<abril[xe+1][0]:
    s=s+abril[xe][1]
    abril_calif.append([abril[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
abril_califord=[]

while x<len(abril_calif)-1:
  if abril_calif[x][0]!=abril_calif[x+1][0]:
    abril_califord.append([abril_calif[x][0],abril_calif[x][1]])
    x=x+1
  else:
    x=x+1

if abril_calif[len(abril_calif)-1][0]!=abril_calif[len(abril_calif)-2][0]:
  abril_califord.append([abril_calif[len(abril_calif)-1][0],abril_calif[len(abril_calif)-1][1]])
#####
xe=0
mayo_calif=[]
s=0
count=1
while len(mayo)-1>=xe:

  if xe==len(mayo)-1 and mayo[len(mayo)-1][0]!=mayo[len(mayo)-2][0]:
    mayo_calif.append([mayo[len(mayo)-1][0],mayo[len(mayo)-1][1]])
    xe=xe+1
    
  elif mayo[xe][0]==mayo[xe+1][0]:
    s=s+mayo[xe][1]
    mayo_calif.append([mayo[xe][0],s])
    xe=xe+1
    count=count+1
  elif mayo[xe][0]<mayo[xe+1][0]:
    s=s+mayo[xe][1]
    mayo_calif.append([mayo[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
mayo_califord=[]

while x<len(mayo_calif)-1:
  if mayo_calif[x][0]!=mayo_calif[x+1][0]:
    mayo_califord.append([mayo_calif[x][0],mayo_calif[x][1]])
    x=x+1
  else:
    x=x+1

if mayo_calif[len(mayo_calif)-1][0]!=mayo_calif[len(mayo_calif)-2][0]:
  mayo_califord.append([mayo_calif[len(mayo_calif)-1][0],mayo_calif[len(mayo_calif)-1][1]])
######
xe=0
junio_calif=[]
s=0
count=1
while len(junio)-1>=xe:

  if xe==len(junio)-1 and junio[len(junio)-1][0]!=junio[len(julio)-2][0]:
    junio_calif.append([junio[len(junio)-1][0],junio[len(junio)-1][1]])
    xe=xe+1
    
  elif junio[xe][0]==junio[xe+1][0]:
    s=s+junio[xe][1]
    junio_calif.append([junio[xe][0],s])
    xe=xe+1
    count=count+1
  elif junio[xe][0]<junio[xe+1][0]:
    s=s+junio[xe][1]
    junio_calif.append([junio[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
junio_califord=[]

while x<len(junio_calif)-1:
  if junio_calif[x][0]!=junio_calif[x+1][0]:
    junio_califord.append([junio_calif[x][0],junio_calif[x][1]])
    x=x+1
  else:
    x=x+1

if junio_calif[len(junio_calif)-1][0]!=junio_calif[len(junio_calif)-2][0]:
  junio_califord.append([junio_calif[len(junio_calif)-1][0],junio_calif[len(junio_calif)-1][1]])
######
xe=0
julio_calif=[]
s=0
count=1
while len(julio)-1>=xe:

  if xe==len(julio)-1 and julio[len(julio)-1][0]!=julio[len(julio)-2][0]:
    julio_calif.append([julio[len(julio)-1][0],julio[len(julio)-1][1]])
    xe=xe+1
    
  elif julio[xe][0]==julio[xe+1][0]:
    s=s+julio[xe][1]
    julio_calif.append([julio[xe][0],s])
    xe=xe+1
    count=count+1
  elif julio[xe][0]<julio[xe+1][0]:
    s=s+julio[xe][1]
    julio_calif.append([julio[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
julio_califord=[]

while x<len(julio_calif)-1:
  if julio_calif[x][0]!=julio_calif[x+1][0]:
    julio_califord.append([julio_calif[x][0],julio_calif[x][1]])
    x=x+1
  else:
    x=x+1

if julio_calif[len(julio_calif)-1][0]!=julio_calif[len(julio_calif)-2][0]:
  julio_califord.append([julio_calif[len(julio_calif)-1][0],julio_calif[len(julio_calif)-1][1]])  
  ########
xe=0
agosto_calif=[]
s=0
count=1
while len(agosto)-1>xe:

  if xe==len(agosto)-1 and agosto[len(agosto)-1][0]!=agosto[len(agosto)-2][0]:
    agosto_calif.append([agosto[len(agosto)-1][0],agosto[len(agosto)-1][1]])
    xe=xe+1
    
  elif agosto[xe][0]==agosto[xe+1][0]:
    s=s+agosto[xe][1]
    agosto_calif.append([agosto[xe][0],s])
    xe=xe+1
    count=count+1
  elif agosto[xe][0]<agosto[xe+1][0]:
    s=s+agosto[xe][1]
    agosto_calif.append([agosto[xe][0],s/count])
    xe=xe+1    
    s=0
    count=1

x=0
agosto_califord=[]

while x<len(agosto_calif)-1:
  if agosto_calif[x][0]!=agosto_calif[x+1][0]:
    agosto_califord.append([agosto_calif[x][0],agosto_calif[x][1]])
    x=x+1
  else:
    x=x+1

if agosto_calif[len(agosto_calif)-1][0]!=agosto_calif[len(agosto_calif)-2][0]:
  agosto_califord.append([agosto_calif[len(agosto_calif)-1][0],agosto_calif[len(agosto_calif)-1][1]]) 

agosto_califord.remove([54,4])
agosto_califord.append([54,4.5])
###############

septiembre_califord=[[17,1]]
noviembre_califord=[[2,3]]

enero_califord=sorted(enero_califord, key=itemgetter(1))
febrero_califord=sorted(febrero_califord, key=itemgetter(1))
marzo_califord=sorted(marzo_califord, key=itemgetter(1))
abril_califord=sorted(abril_califord, key=itemgetter(1))
mayo_califord=sorted(mayo_califord, key=itemgetter(1))
junio_califord=sorted(junio_califord, key=itemgetter(1))
julio_califord=sorted(julio_califord, key=itemgetter(1))
agosto_califord=sorted(agosto_califord, key=itemgetter(1))
septiembre_califord=sorted(septiembre_califord, key=itemgetter(1))
noviembre_califord=sorted(noviembre_califord, key=itemgetter(1))
diciembre_califord=[]

for k in enero_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)
for k in febrero_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in marzo_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)

for k in abril_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)

for k in mayo_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in junio_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in julio_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in julio_califord:
  c=k[1]  
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in agosto_califord:
  c=k[1]   
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)

for k in septiembre_califord:
  c=k[1]   
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)


for k in noviembre_califord:
  c=k[1]
  if k[0]==productos[k[0]-1][0]:
    k.append(productos[k[0]-1][1])
  k.remove(c)
  k.insert(2,c)
###########################




#######
#######sumo el dinero total anual
dinerototalanual=0
for k in totallist:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalanual=dinerototalanual+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalenero=0
for k in enero_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalenero=dinerototalenero+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalfebrero=0
for k in febrero_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalfebrero=dinerototalfebrero+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalmarzo=0
for k in marzo_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalmarzo=dinerototalmarzo+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalabril=0
for k in abril_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalabril=dinerototalabril+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalmayo=0
for k in mayo_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalmayo=dinerototalmayo+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototaljunio=0
for k in junio_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototaljunio=dinerototaljunio+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototaljulio=0
for k in julio_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototaljulio=dinerototaljulio+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

dinerototalagosto=0
for k in agosto_finalv:
  dinero=k[0]*k[3]
  k.append(dinero)
  dinerototalagosto=dinerototalagosto+dinero
  k[3]="Precio unitario: $"+str(k[3])
  k[6]="Ventas totales: $"+str(k[6])

#######Imprimimos la primera posición en donde se encuentra un producto
x=0

ls_pos=[]

for ls in busqueda_prod:

  if ls[1]>x:
    
    x=ls[1]
    k=[ls[0],x]
    ls_pos.append(k)
    
x=x+1

ls_pos.append([len(busqueda_prod),95])

###Agregamos un último valor, por conveniencia 
#######

########Hacemos restas entre identificadores para encontrar cuantas veces se busco cada producto, con busquedas diferentes de cero
y=0

busquedas=[]

while y <=len(ls_pos):

  if y<len(ls_pos)-2:
    
    num=[ls_pos[y+1][0]-ls_pos[y][0],ls_pos[y][1]]

    
    busquedas.append(num)

    y=y+1

  

  else:
   num=[1034-ls_pos[y][0],ls_pos[y][1]] ###Aquí anexamos la cantidad de busquedas para el producto 95

   busquedas.append(num)

   y=len(ls_pos)+1

########print(busquedas)

orden=sorted(busquedas, key=itemgetter(1))


#####Hasta aquí ya tenemos los productos con busquedas diferentesde cero ordenados por producto.


#####Generamos una lista con la primera entrada ceros y la segunda el producto, desde 1 hasta 97 (total de productos)

o=1

ceros=[]

z=range(1,97)

for k in z:
  
  ceros.append([0,k])
####Hasta aquí ya está la lista

#Aquí comparamos la primera entrada de la lista de ceros con la lista de productos con busquedas diferentes de cero. Si vemos que la primera entrada de las listas de productos de cero busquedas es distinta a la primera entrada de productos con busquedas diferentes de cero, entonces anexamos esa entrada y reorganizamos la lista con busquedas diferentes de cero, de modo que vamos anexando los productos con busqueda cero para tener una sola lista.
while o<95:

  if ceros[o][1]!=orden[o][1]:

    orden.append([0,ceros[o][1]])
    orden=sorted(orden, key=itemgetter(1))
    o=o+1
 
  else:

    o=o+1

#####Hasta aqui ya tenemos anexados los productos con cero busquedas y ademas, la lista se encuentra organizada por numero de producto.




###HAcemos un ciclo para anexar a la lista el nombre del producto identificador, para saber a que producto nos estamos refiriendo.
contador=0

for k in orden:

  if k[1]==productos[contador][0]:

    k.append(productos[contador][1])
    contador=contador+1
 ###nombre de producto anexado   
    


orden.append([0,96])####anexamos por conveniencia el producto 96 que tambien tiene cero busquedas
x=0
for k in orden:
  if k[1]==productos[x][0]:
    k.append(productos[x][1])
    k.append(productos[x][3])
    k.append(productos[x][4])
    x=x+1

orden=sorted(orden, key=itemgetter(0))####ordenamos por ventas, de menor a mayor



print("Crea un nombre de usuario el cual contenga máximo 10 caracteres y mínimo 5")

nom_usuario=input()

while len(nom_usuario)>10 or len(nom_usuario)<=4:

  if len(nom_usuario)>10:

    print("Tu usuario contiene más de 10 caracteres. Por favor intenta de nuevo.")

    nom_usuario=input()

  elif len(nom_usuario)<=4:

    print("Tu usuario contiene menos de 5 caracteres. Por favor, intenta de nuevo.")

    nom_usuario=input()

print("Nombre de usuario válido.")

print("Ingrese una contraseña de mínimo 5 caracteres que contenga al menos una letra mayúscula y un número")

con_usuario=input()

mayus = [l for l in con_usuario if l.isupper()]
numero = [l for l in con_usuario if l.isdigit()]

if len(con_usuario) <5:
  print("Tu contraseña tiene menos de 5 caracteres. Intenta de nuevo")
  con_usuario=input()

while len(mayus)==0 or len(numero)==0:
  mayus = [l for l in con_usuario if l.isupper()]
  numero = [l for l in con_usuario if l.isdigit()]

  if len(mayus)==0 and len(numero)!=0:
    print("Tu contraseña no tiene mayúsculas. Intenta de nuevo")
    con_usuario=input()
    

  if len(numero)==0 and len(mayus)!=0:
    print("Tu contraseña no tiene números. Intenta de nuevo.")
    con_usuario=input()

  if len(mayus)==0 and len(numero)==0:
    print("Tu contraseña no tiene numeros ni mayusculas. Intenta de nuevo")
    con_usuario=input()

print("Contraseña valida. \nHas quedado registrado, por favor inicia sesión. \n Ingresa tu nombre de usuario")

inicio_usuario=input()


while inicio_usuario!=nom_usuario:
  print("Nombre de usuario invalido. Intenta de nuevo")
  inicio_usuario=input()
  
print("Ingresa tu contraseña.")
inicio_cont=input()

while inicio_cont!=con_usuario:
  print("Contraseña incorrecta. Intenta de nuevo")
  inicio_cont=input()
continuar="s"

while continuar=="s":
  x=0
  print("Que información desea conocer:\nPresione 1 para busquedas, presione 2 para ventas, presione 3 para ver los productos y sus calificaciones\n(La información que se presente a partir de aquí contendra en la primera columna el número de busquedas(ventas) y en la segunda el símbolo identificador del producto)")
  paso1=input()

  if paso1=="1":
    print("Para obtener los productos con cero busquedas presione 0, para obtener los 10 productos con menores busquedas presione 1, para ver los 10 productos con mayores busquedas presione 2, para ver las busquedas de todos los productos presione 3")
    paso2busq=input()
      
    if paso2busq=="0":
      print("[Busquedas,Identificador de producto, Producto,Categoría,Stock]")
      for k in orden:
        if k[0]==0:
          print(k)
    
    if paso2busq=="1":
      kmd=[]
      print("[Busquedas,Identificador de producto, Producto,Categoría,Stock]")      
      for k in orden:
        if k[0]!=0:
          kmd.append(k)
      for x in kmd[:10]:
        print(x)
  
    if paso2busq=="2":
      kmd=[]
      print("[Busquedas,Identificador de producto, Producto,Categoría,Stock]")        
      for k in orden:
        if k[0]!=0:
          kmd.append(k)
      for x in kmd[-10:]:
        print(x)

    if paso2busq=="3":     
      print("[Busquedas,Identificador de producto, Producto,Categoría,Stock]")        
      for k in orden:
        print(k)
        
    print("¿Desea consultar otro dato? Sí (s) o No (n)")
    continuar=input()

  if paso1=="2":
    print("¿Te interesa consultar los datos anuales o las ventas por mes? Presiona 1 para los datos anuales, 2 si te interesan las ventas mensuales\nSi te interesa ver las categorías más vendidas presiona 3.\n")
    paso2vent=input()

    if paso2vent=="1":
      print("Productos con cero ventas\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
      for k in totallist:
        if k[0]==0:
          print(k)    
      at=[]
      print("\n\nLos 10 productos con menores ventas en el año\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
      for k in totallist:
        if k[0]!=0:
          at.append(k)
      at=sorted(at,key=itemgetter(0))
      for k in at[:10]:
        print(k)
      print("\n\nLos 10 productos con mayores ventas en el año\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
      for k in at[-10:]:
        print(k)

      print("\n Ingresos Totales Anuales: ","$"+str(dinerototalanual)) 

    if paso2vent=="2":

      print("¿De que mes deseas obtener información? Presiona 1 si es enero, 2 si es febrero, 3 si es marzo, etc.(Se han considerado los reembolsos restandolos a la cantidad de ventas)")
      mesdatos=input()

      if mesdatos=="1":
        print("Productos con cero ventas de enero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in enero_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 5 productos con menores ventas de enero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in enero_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:5]:
          print(k)
        print("\n\nLos 5 productos con mayores ventas en enero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-5:]:
          print(k)

        print("\n\nVentas totales enero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in enero_finalv:
          print(k)

        print("\n Ingresos Totales Enero: ","$"+str(dinerototalenero)) 
##########################
      if mesdatos=="2":
        print("Productos con cero ventas de febrero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in febrero_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 5 productos con menores ventas de febrero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in febrero_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:5]:
          print(k)
        print("\n\nLos 5 productos con mayores ventas en febrero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-5:]:
          print(k)

        print("\n\nVentas totales Febrero\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in febrero_finalv:
          print(k)

        print("\n Ingresos Totales Febrero: ","$"+str(dinerototalfebrero))

############################
      if mesdatos=="3":
        print("Productos con cero ventas de marzo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in marzo_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 10 productos con menores ventas de marzo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in marzo_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:10]:
          print(k)
        print("\n\nLos 10 productos con mayores ventas en marzo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-10:]:
          print(k)
  
        print("\n\nVentas totales marzo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in marzo_finalv:
          print(k)
        print("\n Ingresos Totales Marzo: ","$"+str(dinerototalenero)) 
############
      if mesdatos=="4":
        print("Productos con cero ventas de abril\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in abril_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 10 productos con menores ventas de abril\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in abril_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:10]:
          print(k)
        print("\n\nLos 10 productos con mayores ventas en abril\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-10:]:
          print(k)

        print("\n\nVentas totales abril\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in abril_finalv:
          print(k)

        print("\n Ingresos Totales Abril: ","$"+str(dinerototalabril))        
############       
      if mesdatos=="5":
        print("Productos con cero ventas de mayo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in mayo_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 5 productos con menores ventas de mayo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in mayo_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:5]:
          print(k)
        print("\n\nLos 5 productos con mayores ventas en mayo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-5:]:
          print(k)

        print("\n\nVentas totales mayo\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in mayo_finalv:
          print(k)

        print("\n Ingresos Totales Mayo: ","$"+str(dinerototalmayo)) 

########## 
      if mesdatos=="6":
        print("Productos con cero ventas de junio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in junio_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 4 productos con menores ventas de junio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in junio_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:4]:
          print(k)
        print("\n\nLos 4 productos con mayores ventas en junio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-4:]:
          print(k)

        print("\n\nVentas totales junio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in junio_finalv:
          print(k)

        print("\n Ingresos Totales Junio: ","$"+str(dinerototaljunio)) 
               
########
      if mesdatos=="7":
        print("Productos con cero ventas de julio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in julio_ordceros:
          if k[0]==0:
            print(k)    
        ef=[]        
        print("\n\nLos 4 productos con menores ventas de julio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in julio_finalv:
          if k[0]!=0:
            ef.append(k)

        for k in ef[:4]:
          print(k)
        print("\n\nLos 4 productos con mayores ventas en julio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")
        for k in ef[-4:]:
          print(k)

        print("\n\nVentas totales julio\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in julio_finalv:
          print(k)

        print("\n Ingresos Totales Julio: ","$"+str(dinerototaljulio)) 

############################      
      if mesdatos=="8":
        print("¡Solo hubo dos ventas en agosto!")
        print("\nVentas totales agosto\n[Ventas,identificador de producto,Nombre del Producto,Precio unitario, Categoría, Stock,Ingresos totales]")

        for k in agosto_finalv:
          print(k)

        print("\n Ingresos Totales Agosto: ","$"+str(dinerototalagosto)) 
################################
      if mesdatos=="9":
        print("¡No hubo ventas totales en septiembre!")
      if mesdatos=="10":
        print("¡No hubo ventas totales en octubre!")
      if mesdatos=="11":
        print("¡No hubo ventas totales en noviembre!")
      if mesdatos=="12":
        print("¡No hubo ventas totales en dicembre!")
        
      print("¿Desea consultar otro dato? Sí (s) o No (n)")
      continuar=input()
    
    if paso2vent=="3":
      print("¿Quieres ver las ventas anules o mensuales de las categorias?. Presiona 1 si quieres las ventas anuales, 2 si prefieres las mensuales")
      ventcateg=input()
      if ventcateg=="1":
        print("Ventas anuales de las categorias\n[Categoría,Ventas]")
        for k in totalcat:
          print(k)

      if ventcateg=="2":
        print("¿Que mes te interesa? Presiona 1 para enero, 2 para febrero, 3 para marzo, etc.")
        cat=input()

        if cat=="1":
          print("Ventas por categoría en enero\n[Categoría,Ventas]")
          for k in enero_finalcat:
            print(k)
          
        if cat=="2":
          print("Ventas por categoría en febrero\n[Categoría,Ventas]")
          for k in febrero_finalcat:
            print(k)
        
        if cat=="3":
          print("Ventas por categoría en marzo\n[Categoría,Ventas]")
          for k in marzo_finalcat:
            print(k)

        if cat=="4":
          print("Ventas por categoría en abril\n[Categoría,Ventas]")
          for k in abril_finalcat:
            print(k)

        if cat=="5":
          print("Ventas por categoría en mayo\n[Categoría,Ventas]")
          for k in mayo_finalcat:
            print(k)

        if cat=="6":
          print("Ventas por categoría en junio\n[Categoría,Ventas]")
          for k in junio_finalcat:
            print(k)
       
        if cat=="7":
          print("Ventas por categoría en julio\n[Categoría,Ventas]")
          for k in julio_finalcat:
            print(k)

        if cat=="8":
          print("Ventas por categoría en agosto\n[Categoría,Ventas]")          
          for k in agosto_finalcat:
            print(k)   

        if cat=="9":
          print("\nNo hay ventas en septiembre\n")
  
        if cat=="10":
          print("\nNo hay ventas en octubre\n")
   
        if cat=="11":
          print("\nNo hay ventas en noviembre\n")
  
        if cat=="12":
          print("\nNo hay ventas en diciembre\n")
  

      print("\n¿Desea consultar otro dato? Sí (s) o No (n)\n")
      continuar=input()

  if paso1=="3":
    print("\n¿De que mes te interesa ver las? Presiona 1 para enero, 2 para febrero, 3 para marzo, etc.\n")
    calf=input()

    if calf=="1":
      print("\nLos 5 productos peores calificados en enero son\n[Identificador, Producto, Calificacion]")
      for k in enero_califord[:5]:
        print(k)
      print("\nLos 5 productos mejores calificados en enero son\n[Identificador, Producto, Calificacion]")
      for k in enero_califord[-5:]:
        print(k)
          
    if calf=="2": 
      print("\nLos 5 productos peores calificados en febrero son\n[Identificador, Producto, Calificacion]")
      for k in febrero_califord[:5]:
        print(k)
      print("\nLos 5 productos mejores calificados en febrero son\n[Identificador, Producto, Calificacion]")
      for k in febrero_califord[-5:]:
        print(k)

    if calf=="3": 
      print("\nLos 10 productos peores calificados en marzo son\n[Identificador, Producto, Calificacion]")
      for k in febrero_califord[:10]:
        print(k)
      print("\nLos 10 productos mejores calificados en marzo son\n[Identificador, Producto, Calificacion]")
      for k in marzo_califord[-10:]:
        print(k)

    if calf=="4": 
      print("\nLos 10 productos peores calificados en abril son\n[Identificador, Producto, Calificacion]")
      for k in abril_califord[:10]:
        print(k)
      print("\nLos 10 productos mejores calificados en abril son\n[Identificador, Producto, Calificacion]")
      for k in abril_califord[-10:]:
        print(k)

    if calf=="5": 
      print("\nLos 5 productos peores calificados en mayo son\n[Identificador, Producto, Calificacion")
      for k in mayo_califord[:5]:
        print(k)
      print("\nLos 5 productos mejores calificados en mayo son\n[Identificador, Producto, Calificacion]")
      for k in mayo_califord[-5:]:
        print(k)

    if calf=="6": 
      print("\nLos 4 productos peores calificados en junio son\n[Identificador, Producto, Calificacion]")
      for k in junio_califord[:4]:
        print(k)
      print("\nLos 4 productos mejores calificados en junio son\n[Identificador, Producto, Calificacion]")
      for k in junio_califord[-4:]:
        print(k)

    if calf=="7": 
      print("\nLos 4 productos peores calificados en julio son\n[Identificador, Producto, Calificacion]")
      for k in julio_califord[:4]:
        print(k)
      print("\nLos 4 productos mejores calificados en julio son\n[Identificador, Producto, Calificacion]")
      for k in julio_califord[-4:]:
        print(k)

    if calf=="8": 
      print("¡Solo hay dos productos que calificar en agosto!")
      for k in agosto_califord:
        print(k)

    if calf=="9": 
      print("¡Solo hay un producto que calificar en septiembre!")
      for k in septiembre_califord:
        print(k)

    if calf=="10": 
      print("¡No hay productos que calificar en octubre!")

    if calf=="11": 
      print("¡Solo hay un producto que calificar en noviembre!")
      for k in noviembre_califord:
        print(k)

    if calf=="12": 
      print("¡No hay productos que calificar en diciembre!")
    
    print("¿Desea consultar otro dato? Sí (s) o No (n)")
    continuar=input()