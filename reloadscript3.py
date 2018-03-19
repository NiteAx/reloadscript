from splinter import Browser as bro
from getch import getch, pause
import csv
import time

#Input login info
#def manualinputdata():
	#user = input('Input Username: ')
	#pw = input('Input Password: ')

#Html login form names
loginform = 'userId'
pwform = 'password'

#Html button xpaths
loginbtn = '/html/body/form/div/div[3]/div[2]/div[5]/div[1]/button'
accountbtn = '/html/body/form/div/div/div[1]/div/ul/li[2]/a'
managebtn = '/html/body/form/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/button'
logoutbtn = '/html/body/div[2]/div[1]/div[1]/div/ul/li[6]/a'
			
#Html quota value xpaths
value1 = '/html/body/div[2]/div[1]/form/div[1]/div[3]/div/div/div[2]/p[2]'
value2 = '/html/body/div[2]/div[1]/form/div[1]/div[3]/div/div/div[3]/p[2]'

with open('reloadscriptlog.csv') as inputfile:
	inputlog = csv.reader(inputfile, delimiter=',')
	inputtimes = []
	inputdatas = []
	for row in inputlog:
		if len(row) < 3:
			inputtimes.append('0')
			inputdatas.append('0')
		elif len(row) == 3:
			inputtimes.append(row[2])
			inputdatas.append('0')
		elif len(row) == 4:
			inputtimes.append(row[2])
			inputdatas.append(row[3])
with open('Book2.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	usernames = []
	passwords = []
	for row in readCSV:
		username = row[0]
		password = row[1]

		usernames.append(username)
		passwords.append(password)
		
print(inputdatas)
print(inputtimes)
print("Opened and zipped usernames and passwords.")
print('Opening browser...')

#Headless mode or nah
mode = input("GUI mode? [Y] : ")
if mode == "Y":
	ff = bro('firefox')
elif mode == "y":
	ff = bro('firefox')	
else:
	ff = bro('firefox', headless=True)

index=0
n=0
userdata = list(map(list,zip(usernames,passwords)))
for user, pw in userdata:
	currenttime = time.time()
	differencecheck = currenttime - float(inputtimes[n])
	if differencecheck < 86400:
		userdata[n].append(inputtimes[n])
		userdata[n].append(inputdatas[n])
	
		with open('reloadscriptlog.csv', 'w', newline='') as outputfile:
			writer = csv.writer(outputfile, delimiter=',')
			writer.writerows(userdata)
		n=n+1
		continue
	elif differencecheck > 86400:	
		print("Username : " + user)
		#login
		reloadpage = 'https://selfcare.yes.my/myselfcare/doLogin.do'
		ff.visit(reloadpage)
		print('Visiting Yes.my...')
		ff.fill(loginform, user)
		ff.fill(pwform, pw)
		print('Filling in login info...')
		#find quota
		
		#while True:
		#	try:
		#		ff.find_by_xpath(loginbtn).click()
		#		break
		#	except IndexError:
		#		print("Oopsie!")
		#		bro.reload()	
		ff.find_by_xpath(loginbtn).click()
		while True:
			try:
				ff.find_by_xpath(accountbtn).click()
				break
			except:
				print("Ooopsie!")
				ff.reload()
		print('Logged in.')
		#ff.find_by_xpath(managebtn).click()
		while True:
			try:
				ff.find_by_xpath(managebtn).click()
				break
			except:
				print("Ooopsie!")
				ff.reload()
		quota1 = ff.find_by_xpath(value1)
		quota1 = quota1.text
		quota2 = ff.find_by_xpath(value2)
		quota2 = quota2.text
		#print quota
		print ('4G LTE : ' + quota1 +', BB : ' + quota2)
		time1 = time.time()
		print(time1)
		userdata[n].append(str(time1))
		userdata[n].append(quota2)
		print(userdata[n])
		with open('reloadscriptlog.csv', 'w', newline='') as outputfile:
			writer = csv.writer(outputfile, delimiter=',')
			writer.writerows(userdata)
		n=n+1
		#logout
		ff.find_by_xpath(logoutbtn).click()
pause()
ff.quit()
