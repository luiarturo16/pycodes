import paramiko
import cryptography
import time

ip_address = "192.168.1.5"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Succesful Connection", ip_address)

#stdin,stdout,stderr = ssh_client.exec_command('who')
stdin,stdout,stderr = ssh_client.exec_command('conf t\n')
stdin,stdout,stderr = ssh_client.exec_command('int vlan 334\n')

#output = stdout.readlines()

#print '\n'.join(output)

#remote_connection = ssh_client.invoke_shell()

#remote_connection.send("config t\n")
#remote_connection.send("int vlan 335")


#output = remote_connection.recv(65535)
#print (output)
