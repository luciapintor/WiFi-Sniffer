# WiFi-Sniffer

This simple script can be used to capture Wi-Fi packets via interfaces 
that support [monitor mode][1].

[1]: https://en.wikipedia.org/wiki/Monitor_mode

Here the steps of the algorithm:

1) gets the names of the wi-fi interfaces
2) sets to monitor mode the interfaces that supports it
3) assigns a channel to each interface
4) starts the sniffing in each interface
5) saves collected data in files

Superuser privileges are needed to run this script (`sudo -E python3 main.py`).

## Configure interfaces
Functions in the file configure_interfaces.py do steps 1, 2 and 3.

## Start sniffing
Functions in the file start_sniffing.py do steps 4 and 5.
Additionally, the algorithm will ask for the device mode and 
for the device acronym.

## Environment variables
File env_variables_example.py is an example of how 
the env_variables.py file, excluded with gitignore, should look like. 
Example can then be copied and renamed correctly 
to change the values of the variables as desired. 

## Requirements
The algorithm requires the installation of `pyric` and `scapy` libraries 
through pip, and additionally tcpdump utility.

`pip install pyric`

`pip install scapy`

`sudo apt-get install tcpdump -y`
