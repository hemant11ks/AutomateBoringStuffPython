PASSWORD = {
    'email' : 'email123',
    'blog' : 'blog123',
    'stream' : 'stream123'

}

import sys, pypaperclip

if len(sys.argv) < 2:
    print("Incorrect set of argument passed !")
    sys.exit()
account = sys.argv[1]
if account in PASSWORD:
    pypaperclip.copy(PASSWORD[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no account name : " + account)