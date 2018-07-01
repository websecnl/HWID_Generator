import pyperclip
import base64
import binascii
from uuid import getnode as get_mac
import socket
mac = get_mac()
license = (str(mac) + '-' + str(socket.gethostname()))


hwid = base64.b64encode(license)

print("##################")
print("# HWID Generator #")
print("##################")
print("")
print('[+] Your HWID: ' + str(binascii.hexlify(hwid).upper())[::-1])
pyperclip.copy(str(hwid)[::-1])
print('[+] HWID Set to Clipbaord')
print("")
print("Coded By Joel Aviad Ossi")
raw_input("")
