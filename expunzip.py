#Author:
#Amandeep Singh
#MS Computer Engineering
#NYU Polytechnic School Of Engineering '18

import zipfile
import os

dirConst = raw_input('Please enter the path of the directory where the file with students name is located \nSay for example: My file in /home/amn7168/Lab1vhdl contains all the folders with students name within which there are zip files \nSo I will enter \n\n--->/home/amn7168/Lab1vhdl\n\n\nPlease Enter the desired directory\n--->')
dirs = os.listdir(dirConst)
sub = 'Submission attachment(s)'
timestamp = 'timestamp.txt'

for dir in dirs:
	try:
		dirsOpen = os.listdir(dirConst+'/'+dir+'/'+sub)
		os.remove(dirConst+'/'+dir+'/'+timestamp)
		for files in dirsOpen:
			if(files.endswith('.zip')):
				zipdfile = files
				
				zip = zipfile.ZipFile(dirConst+'/'+dir+'/'+sub+'/'+zipdfile)
				zip.extractall(dirConst+'/'+dir+'/')
				os.remove(dirConst+'/'+dir+'/'+sub+'/'+zipdfile)
				os.rmdir(dirConst+'/'+dir+'/'+sub)
	except OSError:
		print(OSError)
		pass
	if len(dir) > 6:
		begin = dir.find('(')+1
		end = len(dir)-1
		name = dir[begin:end]
		print(name)
		os.rename(dirConst+'/'+dir, dirConst+'/'+name)

