-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Network Scanner Script:

This script is a command-line tool that can be used to scan a network and identify all available devices. It works by sending a single ping packet to each IP address in a specified range and checking if a response is received.

Usage:

To use the script, save it as a .cmd file and run it from the command prompt. The script will prompt you to enter the starting and ending IP addresses for the range you want to scan. The script will then scan each IP address in the range and print a message for each device found.

C:\> scan_network.cmd

Enter the starting IP address: 192.168.1.1
Enter the ending IP address: 192.168.1.254

Scanning network...

Device found: 192.168.1.1
Device found: 192.168.1.2
Device found: 192.168.1.10
Device found: 192.168.1.100

Notes:

The script may take some time to complete, depending on the size of the range being scanned.
Some devices may not respond to ping requests, so the script may not be able to detect all devices on the network.

Scanning a network without proper authorization may be illegal and can result in serious consequences.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Password Generator:

This is a Python code for a simple password generator that generates a random password of a specified length. The password can contain uppercase and lowercase letters, digits, and punctuation characters.

Usage:

To use the password generator, simply call the generate_password function with the desired length of the password.

This code uses the following modules:

random
string

This will generate a random password of length 12 and print it to the console. You can change the length to generate passwords of different lengths. The characters string defines the set of characters that can be used in the password; you can modify this string to customize the character set if desired.
