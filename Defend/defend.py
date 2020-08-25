import iwlist
import os

os.system("iwconfig")

interface = input("Please Choose Your Interface\n")

content = iwlist.scan(interface=interface)
cells = iwlist.parse(content)
        
for i in cells:

    # Same essid but different encryption key - attack alert
    
    if(cells.count(i['essid']) > 1 and cells.count(i['mac']) < 1):        
        raise Exception("You are currently under attack!!!\nplease do not enter any network\n") 

print('You Are Protected\n')