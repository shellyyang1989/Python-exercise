# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:03:56 2018

@author: yangyang43
"""

import sys
import re
import os
import tarfile
from importlib.util import find_spec
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain
#fp = os.popen("pip install paramiko")
#fp.close()

package = 'paramiko'
'''
try:
    if importlib.util.find_spec(package) is None:
        pipmain(['install', package])
except:
    print ("The error is " + sys.exc_info()[0])
    exit(1)'''
    
if find_spec(package) is None:    
    pipmain(['install', 'paramiko'])    
import paramiko 

HOST = "10.245.32.221"
USER = "root"
PASSWORD = "Lenovo!23"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASSWORD)

#(stdin, stdout, stderr) = ssh.exec_command("esxcli system version get |grep Version")
#type(stdin)
#print (str(stdout.read()))
ssh.close()

'''
global ROOTPATH
ROOTPATH = os.getcwd()
IMAGEDIR =  os.path.join(ROOTPATH, "image")
OVFPATH = os.path.join(ROOTPATH, "VMware-ovftool-4.1.0-2459827-win.x86_64.msi")
VMWAREOVFINSTALLPATH = os.path.join(ROOTPATH, "VMware")
OVFINSTALLPATH = os.path.join(VMWAREOVFINSTALLPATH, "ovftool")
print (ROOTPATH, IMAGEDIR, OVFPATH, OVFINSTALLPATH, VMWAREOVFINSTALLPATH)

def main():
    
    HOST = sys.argv[1]
    PASSWORD = sys.argv[2]
    VMNAME = sys.argv[3]
    IMAGEURL = sys.argv[4]
    URLUSERNAME = sys.argv[5]
    URLPASSWORD = sys.argv[6]
    
    print (sys.argv)
#    print (HOST, PASSWORD, VMNAME, IMAGEURL, URLUSERNAME, URLPASSWORD)
if __name__ == '__main__':
    main()'''    