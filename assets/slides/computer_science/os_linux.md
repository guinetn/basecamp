# Linux

- ![linux-file-system](assets/slides/computer_science/assets/linux-file-system.jpg)

## logs

/var/log
less file.log
head/tail/grep file.log


## systemd
2015
An init system ¤ used by several common Linux Distributions
Unit files that contain the initialization instructions for the daemons which it controls. 
To control services with systemd, the systemctl command is used

¤ Linux init system 
    First process or daemon started on a system after the initial boot process
    Manages services, daemons and other system processes. 

    Starting:   systemctl start httpd           start a service one time
    Stopping:   systemctl stop httpd            stop a service one time
    Restart:    systemctl restart httpd         Fully stops and starts a service
    Reload:     systemctl reload httpd          Reloads a service’s configuration without restarting it. 
                                                Not all services accept that reload command.
    Enable on Boot:     systemctl enable httpd
                        Created symlink from /etc/systemd/system/multi-user.target.wants/httpd.service
                                        to /etc/systemd/system/httpd.service.
    Disable on Boot     systemctl disable httpd
                        Removed symlink /etc/systemd/system/multi-user.target.wants/httpd.service.
    Check Status:       systemctl status httpd

    man 1 systemctl

## Firewall

download.md(assets/slides/security/firewalld.md)

## Secure My Linux Server    

Ensure your Server is Up-To-Date: apt-get update && apt-get upgrade

Create a Secondary User and Disable Root Logins
    adduser bob
    Add it to the sudo’ers file, so he can temporarily increase his rights and permissions as needed to accomplish root level tasks.
    echo 'Bob ALL=(ALL) ALL' >> /etc/sudoer
    Next, log out and then SSH back into the server as the new user to ensure that their login works as expected. Once in, confirm they can ‘su’ up to root. Next, login into the server in a second terminal. This is important! Now, let’s disable the root users SSH login. To accomplish this, we’re going to edit the  /etc/ssh/sshd_config file:
    vim /etc/ssh/sshd_config    
    #PermitRootLogin yes   →    PermitRootLogin no
    Restart the SSH service:    /etc/init.d/sshd restart Stopping sshd: [ OK ] Starting sshd: [ OK ]

Setup SSH Keys
    SSH keys allow for you to connect to the server securely with a stored key pair. 
    SSH into your server as the root user. Next, run:
    ssh-keygen -t rsa -C "you@example.com"
    Press <Enter> to accept the default locations and file names, then enter, and then re-enter a passphrase for your user. Next, we’ll add your public key to the local authorized_keys file.
    cd ~/.ssh cp id_rsa.pub authorized_keys
    Next, copy the new public key to the root user’s SSH directory on the server.
    cd ~/.ssh scp authorized_keys root@host.servername.com:/root/.ssh/
    Now you can simply connect with:
    ssh host.servername.com

Check and Configure the Firewall
    root@server:~# ufw app list Available applications: OpenSSH
    root@server:~# ufw status Status: active To Action From -- ------ ---- 22/tcp ALLOW Anywhere 22 ALLOW Anywhere 8080/tcp ALLOW Anywhere 80/tcp ALLOW Anywhere Anywhere DENY 58.218.92.34 80 DENY 202.54.1.5 22 (v6) ALLOW Anywhere (v6) 22/tcp (v6) ALLOW Anywhere (v6) 8080/tcp (v6) ALLOW Anywhere (v6) 80/tcp (v6) ALLOW Anywhere (v6)

Limit Open Ports
    Testing for open ports can be accomplished using the command netstat -tulpn:
    root@server:~# /home# netstat -tulpn Active Internet connections (only servers) Proto Recv-Q Send-Q Local Address           Foreign Address State PID/Program name tcp        0 0 0.0.0.0:22              0.0.0.0:* LISTEN   69941/sshd tcp6       0 0 :::22                   :::* LISTEN   69941/ss

Turn Off IPv6
    If you are not using IPv6, you can go to the network configuration file and add the following lines to disable it.
    vim /etc/sysconfig/network
    NETWORKING_IPV6=no IPV6INIT=no

Be Aware/Cautious of All Applications You Install
Check and Disable Unneeded Startup Processes
Review Logs Regularly


https://www.liquidweb.com/kb/security-for-your-linux-server/