## Learning Networking Basics 2

## Task 0

The set of commands you provided is used to create a modified version of the /etc/hosts file by adding specific entries to it. Here's what each command does:

**cp /etc/hosts ~/hosts.new:**

This command makes a copy of the existing /etc/hosts file and saves it as ~/hosts.new in your user's home directory (the ~ represents your home directory).

**echo "127.0.0.2 localhost" > ~/hosts.new:**

This command appends a line to the ~/hosts.new file. The line specifies that the hostname "localhost" should resolve to the IP address 127.0.0.2. The > operator overwrites the content of the file, so if ~/hosts.new already exists, this command replaces its content.

**echo "8.8.8.8 facebook.com" >> ~/hosts.new:**

This command appends another line to the ~/hosts.new file. It specifies that the hostname "facebook.com" should resolve to the IP address 8.8.8.8. The >> operator appends the line to the end of the file, so it doesn't replace the previous entry.

**cp -f ~/hosts.new /etc/hosts:**

1. This command copies the modified ~/hosts.new file to the original /etc/hosts file, effectively replacing the original file with the new version.
2. The -f flag is used to force the copy, ensuring that it happens without asking for confirmation even if the target file (in this case, /etc/hosts) already exists.

## Task 1

The command you provided is a combination of several command-line utilities in a pipeline to extract IPv4 addresses from the system's network interfaces. Here's an explanation of each part of the command:

**ip -4 addr show:**

1. This command uses the ip tool to display information about network interfaces and their configurations.
2. The -4 option specifies that you want to display IPv4 addresses. This is used to filter the output to show only IPv4 addresses.
3. The addr show part is the subcommand to show address information for all network interfaces.

**| (Pipe):**

The pipe symbol (|) is used to pass the output of the previous command as input to the next command in the pipeline.

**awk '/inet / {print $2}':**

1. This part of the command uses awk, a powerful text processing tool, to filter and format the output.
2. /inet / is an awk pattern that looks for lines containing the word "inet," which is typically used to denote IP addresses in the output from the ip command.
3. {print $2} instructs awk to print the second field (delimited by spaces or tabs) on lines that match the pattern. This second field is the IP address itself.

**| (Pipe):**

Another pipe symbol is used to pass the output from the awk command to the next command.

**cut -d'/' -f1:**

1. This part uses the cut command to further refine the output.
2. -d'/' specifies the delimiter character as a forward slash (/). This is because the IP addresses in the output often include a subnet mask in CIDR notation (e.g., /24), and we want to remove it.
3. -f1 tells cut to select and output the first field before the delimiter (i.e., the IP address without the subnet mask).

## Task 3

The command nc -l localhost 98 is using the nc (netcat) tool to create a simple network listener on port 98 for the "localhost" (the current machine). Here's an explanation of each part of the command:

1. nc: This is the command for the netcat utility, which is a versatile networking tool that can be used for various network-related tasks, including creating network connections, transferring data, and network listening.

2. -l: This option stands for "listen." It tells nc to operate in listening mode, which means the tool will listen for incoming network connections on the specified host and port.

3. localhost: This is the hostname or IP address to which you want to bind the listening socket. In this case, "localhost" refers to the current machine, making the listener accessible only from within the same machine. It's equivalent to using the IP address 127.0.0.1.

4. 98: This is the port number to which the listener is bound. In this case, the listener will listen on port 98.


## What is 0.0.0.0

The IP address "0.0.0.0" has several different meanings depending on the context in which it's used:

1. Default Route: In the context of network routing, "0.0.0.0" often represents the default route or the default gateway. This is the route that is used when no specific route is available for a particular destination. In other words, it's a catch-all route that sends traffic to the default gateway for further routing decisions.

2. Unspecified Address: In some cases, "0.0.0.0" can be used to represent an unspecified or unknown IP address. It is used in software and protocols to indicate that a particular IP address is not yet assigned or is unknown.

3. Wildcard: In certain network configurations or access control lists, "0.0.0.0" can be used as a wildcard to match any IP address. It signifies that a rule or configuration should apply to all addresses.

## What is /etc/hosts

In Unix-like operating systems, including Linux, the "/etc/hosts" file is a plain text file used to map hostnames to IP addresses. It is a local DNS (Domain Name System) resolver, and its primary purpose is to help resolve hostnames to IP addresses without the need to query an external DNS server. Each line in the "/etc/hosts" file typically associates a hostname with an IP address.

Here's how it works:

1. Hostname to IP Resolution: When your computer needs to connect to another device on a network, it first checks the "/etc/hosts" file to see if the hostname and corresponding IP address are listed there.

2. Local Resolution: If the hostname is found in the "/etc/hosts" file, the computer uses the associated IP address for the connection, without querying an external DNS server. This is particularly useful for specifying local or private network resources.

3. Fallback Mechanism: If the hostname is not found in "/etc/hosts," the computer will resort to querying external DNS servers for IP address resolution.

A typical entry in the "/etc/hosts" file looks like this:
	127.0.0.1   localhost

In this example, it associates the hostname "localhost" with the IP address 127.0.0.1, which is the loopback address. The loopback address is used to refer to the local machine itself.

## How to display your machine’s active network interfaces

To display the active network interfaces on your machine, you can use various commands depending on your operating system. Here are the commands for different operating systems:

1. On Windows:

**Open a Command Prompt or PowerShell window.**
Use the ipconfig command to display network configuration information, including active network interfaces. Type ipconfig and press Enter.
	ipconfig

This will provide a list of all active network interfaces on your Windows machine, along with their respective IP addresses, subnet masks, and more.

2. On Linux (Ubuntu, Debian, CentOS, etc.):

**Open a terminal window.**
Use the ifconfig command or the more modern ip command to display active network interfaces. You may need superuser privileges to run these commands.
**Using ifconfig:**

	ifconfig

**Using ip:**

	ip addr

This will list all active network interfaces on your Linux machine, including their IP addresses and other configuration details.
