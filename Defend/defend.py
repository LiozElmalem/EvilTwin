import iwlist
import os

os.system("iwconfig")

interface = input("Please Choose Your Interface\n")

content = iwlist.scan(interface=interface)
cells = iwlist.parse(content)

essids = []

for i in cells:
    essids.append(i['essid'])

print('Access Points...')
print(essids , '\n')
        
for i in essids:
    if(essids.count(i) > 1):        
        print("You are currently under attack!!!\nplease do not enter any network\n") 
        exit

print('You Are Protected\n')