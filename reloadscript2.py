from splinter import Browser as bro
from getch import getch, pause
import csv


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


with open('Book2.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	usernames = []
	passwords = []
	for row in readCSV:
		username = row[0]
		password = row[1]

		usernames.append(username)
		passwords.append(password)
		
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
for user, pw in zip(usernames,passwords):
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

	#logout
	ff.find_by_xpath(logoutbtn).click()

pause()
ff.quit()
