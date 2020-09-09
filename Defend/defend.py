import iwlist
import os
import sys

os.system("iwconfig")

interface = input('Choose interface to protect on\n')

# Scanning the networks
content = iwlist.scan(interface=interface)

# Parse the networks to objects
cells = iwlist.parse(content)
        
for i in cells:

    # Same essid but different encryption key - attack alert
    
    if(cells.count(i['essid']) > 1 and cells.count(i['mac']) < 1):        
        raise Exception("You are currently under attack!!!\nplease do not enter any network\n") 

print('\n\n\nYou Are Protected\n')