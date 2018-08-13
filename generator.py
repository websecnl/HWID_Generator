import pyperclip
import base64
import binascii
from uuid import getnode as get_mac
import socket
mac = get_mac()
plain = (str(mac) + '-' + str(socket.gethostname()))
hwid = base64.b64encode(plain)
license = binascii.hexlify(hwid).upper())[::-1]

banner = ("######################################\n"
          "## HWID GENERATOR - BY JOEL A. OSSI ##\n"
          "######################################")
print(banner)
print("")
print('[+] Your HWID: ' + str(license)
pyperclip.copy(str(license)
print('[+] HWID Set to Clipbaord')
raw_input("")
