# firewalld

firewalld on systemd systems is easier to manage and configure than iptables.

systemctl enable firewalld      Be sure it started automatically with the server
systemctl start firewalld       Start it manually the first time
systemctl stop firewalld        When troubleshooting rules and connection issues
systemctl restart firewalld
systemctl status firewalld      is enabled, active, and running ?

### Configuring Rules

open ports, allow services, whitelist IPs for access…
include the `--permanent` flag:  rule is saved even after you restart/reboot

* Add a Port for TCP or UDP
firewall-cmd --permanent --add-port=22/TCP          open a port. Need to add rules for each protocol tcp/udp
firewall-cmd --permanent --add-port=53/UDP

* Remove a Port for TCP or UDP
firewall-cmd --permanent --remove-port=444/tcp      remove a currently open port, closing off that port

* Add a Service
These services assume the default ports configured within the /etc/services configuration file; if you wish to use a service on a non-standard port, you will have to open the specific port, as in the example above.
firewall-cmd --permanent --add-service=ssh
firewall-cmd --permanent --add-service=http

* Remove a Service
firewall-cmd --permanent --remove-service=mysql     Then close off the port that is defined for that service.

* Whitelist an IP Address
firewall-cmd --permanent --add-source=192.168.1.100     add a trusted source
firewall-cmd --permanent --add-source=192.168.1.0/24    a range of IPs using what is called CIDR notation

* Remove a Whitelisted IP Address
firewall-cmd --permanent --remove-source=192.168.1.100

* Block an IP Address
firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='192.168.1.100' reject"
firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='192.168.1.0/24' reject"   CIDR notation

* Whitelist an IP Address for a Specific Port (More Rich Rules)
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port protocol="tcp" port="3306" accept'

* Removing a Rich Rule
firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="192.168.1.100" port protocol="tcp" port="3306" accept'

* Saving Firewall Rules
After you have completed all the additions and subtraction of rules, you need to reload the firewall rules to make them active. 
firewall-cmd --reload

* Viewing Firewall Rules
After reloading the rules, you can confirm if the new rules are in place correctly with the following.
firewall-cmd --list-all

https://www.liquidweb.com/kb/an-introduction-to-firewalld/