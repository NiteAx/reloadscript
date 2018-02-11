from splinter import Browser as bro
from getch import getch, pause


#Input login info
user = input('Input Username: ')
pw = input('Input Password: ')

#Open browser
print('Opening browser...')
ff = bro('firefox')
reloadpage = 'https://selfcare.yes.my/myselfcare/doLogin.do'

#Html login form names
loginform = 'userId'
pwform = 'password'

#Html button xpaths
loginbtn = '/html/body/form/div/div[3]/div[2]/div[5]/div[1]/button'
accountbtn = '/html/body/form/div/div/div[1]/div/ul/li[2]/a'
managebtn = '/html/body/form/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[2]/button'
logoutbtn = '/html/body/div[2]/div[1]/div[1]/div/ul/li[6]/a'

#Html quota value xpath
value1 = '/html/body/div[2]/div[1]/form/div[1]/div[3]/div/div/div[2]/p[2]'
value2 = '/html/body/div[2]/div[1]/form/div[1]/div[3]/div/div/div[3]/p[2]'
#Go to login page
ff.visit(reloadpage)
print('Visiting Yes.my...')
ff.fill(loginform, user)
ff.fill(pwform, pw)
print('Filling in login info...')
ff.find_by_xpath(loginbtn).click()

ff.find_by_xpath(accountbtn).click()
print('Logged in.')
ff.find_by_xpath(managebtn).click()
quota1 = ff.find_by_xpath(value1)
quota1 = quota1.text

quota2 = ff.find_by_xpath(value2)
quota2 = quota2.text

print ('Data Left : ' + quota1 +', Data Right : ' + quota2)
pause()
ff.quit()
exit()
