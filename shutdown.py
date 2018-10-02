want = input("Do you really want to kill me :) (y/n) ")
if want == 'n':
    exit()
else:
    sys.os("shutdown -s -t 1")
