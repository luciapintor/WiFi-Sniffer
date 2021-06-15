# WiFi-Sniffer

This algorithm configures the sniffing interfaces,
starts the sniffing in each interface and
save collected data in files.

Superuser privileges are needed to run this script (`sudo -E python3 main.py`).

## Configure interfaces
Functions in the file configure_interfaces.py do the following steps:

1) get the names of the wi-fi interfaces
2) check if the interfaces support monitor mode
3) set to monitor mode the interfaces that supports it
3) assign a channel to each monitor interface

Some Wi-Fi interfaces don't support all channels, so there is a loop 
to try to assign correctly all of them.

## Start sniffing
Functions in the file start_sniffing.py do the following steps:
1) create a folder for the capture data
2) ask to type the device id 
3) ask to type the device mode
4) show the timestamp of the capture start and its duration
5) show the sniffing interfaces, and their assigned channels
6) prepare the capture filename structure
`{device_id}-ts-{timestamp}-ch{channel}-mode{device_mode}.pcap`
7) start a different process for the sniffing in each channel
8) terminate all captures

Note: steps 2 and 3 are meant for single device captures, 
     they affect only the title of the capture files.

## Environment variables
File env_variables_example.py is an example of how 
the env_variables.py file (excluded with gitignore) should look like. 
Example file is meant be copied and renamed correctly, in order to 
change the values of the input variables as desired. 

## Requirements
The algorithm requires the installation of `pyric` and `scapy` libraries 
through pip, and additionally tcpdump utility.

`pip install pyric`

`pip install scapy`

`sudo apt-get install tcpdump -y`
