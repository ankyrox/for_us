#this will work only on ppython >= 3.0.0


import os
want = input("Do you really want to kill me :) (y/n) ")
if want == 'n':
    exit()
else:
    os.system("shutdown -s -t 1")
