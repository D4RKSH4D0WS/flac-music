#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author D4RKSH4D0WS
#Di kala gabut melanda...
try:
	import requests as r
	import os,re
except:
	os.system('pip2 install requests;python2 flac.py')
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
os.system('clear')
print '''%s
╔═╗╦  ╔═╗╔═╗  ╔╦╗╦ ╦╔═╗╦╔═╗
╠╣ ║  ╠═╣║    ║║║║ ║╚═╗║║  
╚  ╩═╝╩ ╩╚═╝  ╩ ╩╚═╝╚═╝╩╚═╝
%sPowered by https://flacless.com
'''%(G1,W1)
cari=raw_input('%s╔═%s[ %sMasukkan judul lagu %s]\n%s╚═%s[ %sInput %s]%s>%s '%(P1,G1,W1,G1,P1,G1,W1,G1,Y1,W1))
a=r.get('https://flacless.com/search?q='+cari).text
c=re.findall('<div class="card-title">(.*?) </div>',a)
b=re.findall('''<a
                     href="(.*?)"
                    class="w-full sm:w-1/2 xl:w-1/3"
                >''',a)
print
cnt=0
for x in c:
    cnt += 1
    print(str(cnt)+'%s). %s%s'%(G1,W1,x))
tanya = int(raw_input('\n%s╚═%s[ %sSelect %s]%s>%s '%(P1,G1,R1,G1,C1,W1)))
if tanya == '':
	print 'Pilih yg bener !'
	exit()
link = b[tanya - 1]
print
print('%s[%s>%s] %sResult: https://flacless.com%s'%(G1,Y1,G1,W1,link))
print
raw_input(W1+'['+R1+'!'+W1+'] Tekan enter untuk kunjungi link')
os.system('xdg-open https://flacless.com'+link)





