import os
import time
import subprocess


gpio=17
f = open ('/proyecto/horainicio.txt','r')
hi=f.read()

f = open ('/proyecto/minutoinicio.txt','r')
mi=f.read()

f = open ('/proyecto/horafinal.txt','r')
hf=f.read()

f = open ('/proyecto/minutofinal.txt','r')
mf=f.read()

tab=" "
hi=str(hi).strip()
mi=str(mi).strip()
hf=str(hf).strip()
mf=str(mf).strip()
dia="*"
mes="*"
ano="*"
tab=" "
user="root"
if hi != "" and mi != "" and hf != "" and hf != "":
	path="python3 /proyecto/activarGPIO17.py"
	path2=" python3 /proyecto/desactivarGPIO17.py"
	cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
	print(str(cadena))

	os.system("sudo chmod -R 777 /etc/cron.d/on17")
	pf=open(r'/etc/cron.d/on{var}'.format(var=gpio),'w')
	pf.write(cadena)
	pf.write("\n")
	pf.close()
	cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2)) 
	print(str(cadena2))
	os.system("sudo chmod -R 777 /etc/cron.d/off"+str(gpio)+"")
	pf2=open(r'/etc/cron.d/off{var}'.format(var=gpio),'w')
	pf2.write(cadena2)
	pf2.write("\n")
	pf2.close()
	os.system("sudo chmod -R 755 /etc/cron.d/on"+str(gpio)+"")
	os.system("sudo chmod -R 755 /etc/cron.d/off"+str(gpio)+"")
	os.system("sudo /etc/init.d/cron restart")
