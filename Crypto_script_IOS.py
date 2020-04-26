import getpass
import sys
import telnetlib

HOST = raw_input("Enter Host IP address: ")
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("crypto isakmp policy 10\n")
tn.write("encr aes\n")
tn.write("authentication pre-share\n")
tn.write("group 2\n")
tn.write("crypto isakmp key cisco123 address 50.101.90.2\n")
tn.write("access-list 110 remark Interesting traffic access-list\n")
tn.write("access-list 110 permit ip 10.5.5.0 0.0.0.255 192.168.1.0 0.0.0.255\n")
tn.write("access-list 111 remark NAT exemption access-list\n")
tn.write("access-list 111 deny   ip 10.5.5.0 0.0.0.255 192.168.1.0 0.0.0.255\n")
tn.write("access-list 111 permit ip 10.5.5.0 0.0.0.255 any\n")
tn.write("route-map nonat permit 10\n")
tn.write("match ip address 111\n")
tn.write("ip nat inside source route-map nonat interface fa0/1 overload\n")
tn.write("crypto ipsec transform-set ESP-AES-SHA esp-aes esp-sha-hmac\n")
tn.write("mode tunnel\n")
tn.write("crypto map outside_map 10 ipsec-isakmp\n")
tn.write("set peer 50.101.90.2\n")
tn.write("match address 110\n")
tn.write("interface fa0/1\n")
tn.write("crypto map outside_map\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()