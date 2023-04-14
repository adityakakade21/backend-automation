import csv

import paramiko as paramiko
from utilities.configurations import *

#connection

username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# run commands

#stdin,stdout,stderr = ssh.exec_command("ls -a")

#print(stdout.readlines())

stdin,stdout,stderr = ssh.exec_command("cat demofile")

lines = stdout.readlines()

print(lines[3])

#file transfer

sftp = ssh.open_sftp()
destinationPath = "script.py"
sourcePath = "batchFiles/script.py"
sftp.put(sourcePath, destinationPath)

destinationPath = "loanasa.csv"
sourcePath = "batchFiles/loanasa.csv"
sftp.put(sourcePath, destinationPath)

#trigger the batch commands

stdin,stdout,stderr = ssh.exec_command("python script.py")

#download the file to your system

sftp.get("Dockerfile", "outputFiles/Dockerfile")

with open('outputFiles/loanasa.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    for row in csvReader:
        if row[0] == "32321":
            assert row[1] == "rejected"

ssh.close()














