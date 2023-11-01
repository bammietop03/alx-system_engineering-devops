## LEARNING NETWORKING BASICS

## OSI model
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or networking system into seven distinct layers. These layers help in understanding and organizing the various processes and protocols involved in network communication. The seven layers of the OSI model, from bottom to top, are:

1. Physical Layer: Deals with the physical transmission of data, such as cables, switches, and electrical signals.

2. Data Link Layer: Responsible for framing data into packets, addressing, and error detection and correction at the link level.

3. Network Layer: Manages routing and addressing to enable data to travel between different networks or subnets.

4. Transport Layer: Ensures end-to-end communication, reliability, and data flow control between devices.

5. Session Layer: Establishes, manages, and terminates sessions or connections between applications.

6. Presentation Layer: Translates, encrypts, or compresses data for transmission, making sure it's in a format that can be understood by the application layer.

7. Application Layer: Provides a user interface for accessing network services and applications, such as web browsers, email clients, and file transfer programs.

## Different types of network

**LAN (Local Area Network):**

	Think of a LAN like your home or a small office network.
	It's a small, private network that connects devices like computers, printers, and smartphones within a limited area, like a single building or your home.
	It's like the local community of devices that can talk to each other, share files, and printers, but they don't extend too far beyond your home or office.

**WAN (Wide Area Network):**

	A WAN is like a vast network that covers a much larger area, like a city, country, or even the whole world.
	It connects multiple LANs and other networks over long distances, often using the internet as the backbone.
	Imagine it as the highways that connect different cities; it helps devices in one city (LAN) communicate with devices in other cities.
**WLAN (Wireless Local Area Network):**

	A WLAN is like a wireless version of a LAN.
	Instead of using cables to connect devices, it uses Wi-Fi signals.
	So, it's like having a local network in your home or office, but you can connect to it wirelessly with your laptop, smartphone, or tablet without plugging in any cables.

## How the internet works 

1. Devices and Data: The internet is a massive network of interconnected devices like computers, servers, and smartphones. These devices send and receive data in the form of text, images, videos, and more.

2. Data Packets: When you send information over the internet, it's broken down into small packets of data. Each packet contains a piece of your message, along with the destination address.

3. Routers: Data packets travel through a web of routers, which are like the traffic cops of the internet. Routers examine the destination address on each packet and decide where to send it next.

4. Internet Service Providers (ISPs): Your data may pass through various ISPs, which are companies that provide internet access. ISPs act as gateways to the global internet network.

5. Backbone Networks: There are high-speed data highways known as backbone networks, which carry massive amounts of data across long distances. These networks connect continents and countries.

6. Protocols: The internet relies on a set of rules and protocols (like TCP/IP) to ensure that data is transmitted correctly and reliably. These protocols help devices communicate effectively.

7. Servers: When you visit a website or use an app, you're typically connecting to a server. Servers store and provide the content or services you're accessing.

8. Domain Name System (DNS): The DNS system translates human-readable website addresses (like www.example.com) into IP addresses that computers understand. This allows your device to find the right server.

9. Encryption: To keep data secure during transmission, many websites and services use encryption (e.g., HTTPS). This means that data is scrambled and can only be unscrambled by the intended recipient.

10. User Devices: Your computer, smartphone, or other devices act as clients. They send requests for data (e.g., loading a web page) and receive the data in response.

11. Two-Way Communication: The internet is bidirectional, meaning that data flows back and forth. When you click a link, the request goes out, and the response (the web page) comes back to your device.

12. Global Network: The internet is a global network because it connects devices all around the world. It doesn't matter where you are; you can access data and services from anywhere with internet access.

## What is MAC Address

A Media Access Control (MAC) address is a string of characters that identifies a device on a network. It’s tied to a key connection device in your computer called the network interface card, or NIC. The NIC is essentially a computer circuit card that makes it possible for your computer to connect to a network. A NIC turns data into an electrical signal that can be transmitted over the network. 
[READ MORE](https://whatismyipaddress.com/mac-address)

## What is an IP Address

Every machine on the the Internet has a unique number assigned to it, called an IP address. Without a unique IP address on your machine, you will not be able to communicate with other devices, users, and computers on the Internet. You can look at your IP address as if it were a telephone number, each one being unique and used to identify a way to reach you and only you.
[READ MORE](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)

## Localhost

"Localhost" is a hostname used to refer to the current device that a program is running on. It is used to establish a connection with the device itself through the loopback network interface. In other words, when a program or service refers to "localhost," it is communicating with its own system, rather than with another device on a network or the internet.

Localhost is often associated with the IP address 127.0.0.1, which is the loopback address for IPv4. In IPv6, the equivalent loopback address is "::1". Both IPv4 and IPv6 loopback addresses are used for the same purpose: to enable communication within the device itself.

Common uses of "localhost" and the loopback address include:

1. Testing and Debugging: Developers use localhost to test and debug software locally without the need for an external network connection.

2. Web Development: Web developers often use localhost to test websites and web applications on their own computer before deploying them to a web server.

3. Database Access: Database systems like MySQL or PostgreSQL can be accessed through localhost for local development and testing.

4. Server Services: Many server services and applications, such as web servers (e.g., Apache, Nginx) and email servers, can be configured to run on localhost for testing purposes.

## What's the Difference Between TCP and UDP?

TCP/IP is a suite of protocols used by devices to communicate over the Internet and most local networks. It is named after two of it's original protocols---the Transmission Control Protocol (TCP) and the Internet Protocol (IP). TCP provides apps a way to deliver (and receive) an ordered and error-checked stream of information packets over the network.

The User Datagram Protocol (UDP) is used by apps to deliver a faster stream of information by doing away with error-checking. When configuring some network hardware or software, you may need to know the difference.

UDP is used when speed is desirable and error correction isn't necessary. For example, UDP is frequently used for live broadcasts and online games.
[READ MORE](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

## TCP and UDP ports

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

	22 for SSH
	80 for HTTP
	443 for HTTPS

## What is ping /ICMP

ping is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It is available for virtually all operating systems that have networking capability, including most embedded network administration software.
[READ MORE](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)

## Task 4

**Write a Bash script that displays listening ports:**

	Answer -  netstat -lp

The netstat command is a network utility tool available on many Unix-like operating systems, including Linux.

It is used to display various network-related information, such as network connections, routing tables, interface statistics, masquerade connections, and more.

The -lp option is used with netstat to display a list of active network connections and listening ports along with the associated processes.

## Task 5

**Write a Bash script that pings an IP address passed as an argument**

	if [ "$1" == "" ]; then
    		echo "Usage: 5-is_the_host_on_the_network {IP_ADDRESS}"
	else
    		ping -c 5 "$1"
	fi

**if [ "$1" == "" ]; then:** 
This line starts an if statement. It checks whether the first command-line argument (referred to as $1) is an empty string. The double equals (==) is used for string comparison. If there are no command-line arguments, it means the user did not provide an IP address.

**echo "Usage: 5-is_the_host_on_the_network {IP_ADDRESS}":**
This line is within the if block and is executed if there are no command-line arguments. It displays a usage message indicating how to use the script, which is to provide an IP address as an argument.

**else:**
If there is at least one command-line argument, the script proceeds to the else block.

**ping -c 5 "$1":**
Within the else block, this line uses the ping command to send ICMP (Internet Control Message Protocol) echo requests to the IP address provided as the first command-line argument. It pings the IP address five times (-c 5). The IP address is obtained from the value of $1, which is the first argument passed to the script when it was executed.
