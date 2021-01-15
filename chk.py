import os
#print('Denix Sandbox')
appversion=2.0
appname='Updater'
space=' '
appcversion=2
print(str(appname)+str(space)+str(appversion))
print('Checking Version')
os.system('wget https://raw.githubusercontent.com/mojeg/test/main/versionchk -q')
f=open('versionchk','r')
f=f.read()
f=f.rstrip("\n")
if int(f) > int(appcversion):
  print('UPDATE IS AVALABLE')
  print('Creating Backup')
  os.system('cp chk.py chk.py.bk')
  os.system('rm versionchk')
  os.system('wget https://raw.githubusercontent.com/mojeg/test/main/versionchk --output-document=chk.py')
  os.system('python3 chk.py')
else:
  print('No updates UTD')
  os.system('rm versionchk')
