import os

output1 = os.system ("sudo ifconfig")
output2 = os.system ("sudo netstat -rn")

os.system ("sudo ifconfig eth0 down")
os.system ("sudo ifconfig eth0 192.168.1.4/24")
os.system ("sudo ifconfig eth0 up")
os.system ("route add default gw 192.168.1.1")

print output1
print output2

os.system ("ping 192.168.1.1")
