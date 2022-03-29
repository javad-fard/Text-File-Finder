import urllib
import re
import time
import httplib

print '''
 ____________________________________________
|                                            |
|           Text File Finder                 |
|          				     |
|	      		  		     |
|			                     |
|           Coded by Javad-Fard              |
|                                            |
|____________________________________________|
'''
#directory for text file
text = ['text.txt','file.txt','UserPass.txt','log.txt','user.txt','users.txt','pass.txt','password.txt','user-login.txt',
'users-login.txt','user-pass.txt','login.txt','logins.txt','test.txt','test1.txt','test2.txt','test3.txt','test4.txt','test5.txt','ist.txt','logs/logs.txt','passwords.txt','log-123.txt','logs-123.txt',
'user-123.txt','users-123.txt','password-123.txt','passwords-123.txt','123.txt','user/123.txt','test/123.txt','xml.txt','test1/123.txt','test2/123.txt','test3/123.txt','test/xml.txt','test1/xml.txt','test/ist.txt','test/log-123.txt','test1/log-123.txt','test2/log-123.txt','test3/log-123.txt','test4/log-123.txt','test5/log-123.txt','test/logs-123.txt',
'log.php','user.php','users.php','pass.php','password.php','user-login.php','users-login.php','user-pass.php','login.php','logins.php','test.php','test1.php','test2.php','test3.php','ist.php','logs.php','passwords.php','log-123.php','logs-123.php','user-123.php','users-123.php','password-123.php','passwords-123.php','123.php','user/123.php',
'test/123.php','xml.php','test1/123.php','test2/123.php','test/xml.php','test1/xml.php','test/ist.php','test1/ist.php','test/log-123.php']
#save in text file
Found = open('Found.txt','w')
Found.write('[!]This page are Found: ')
#code for finde directory
def find(pat , text , line):
    match=re.findall(pat, text)
    if match:
       print '[-] Not Found: ' + line
    else:
        print '[+] Found: '+ line
        Found.write('\n'+line)
#input url
url = raw_input('\n[!] Target (With out "http://") : ')

try:
    print ("[?] Checking website " + url + " ...")
    conn = httplib.HTTPConnection(url)
    conn.connect()
    print "\n[*] Yes... Server is On-line."
except:
    raw_input('\n[!] Error!Check Your Internet.')
print '\nStart at:'+' [ ' + time.ctime() + ' ] ' + '\n'
for line in text:
    url2 = 'http://' + url + '/' + line
    site = urllib.urlopen(url2)
    find('404', site.read(),url2)
print '\n[!] Finished at:'+' [ ' + time.ctime() + ' ] ' + '\n'
raw_input('\nFinished "ENTER" To Exit.')
