# WiFi-Sniffer

This algorithm aims to set up Wi-Fi interfaces and to create pcap captures of Wi-Fi management messages simultaneously on different channels (by default it selects the non-overlapping channels 1, 6 and 11).
The software was designed to create a dataset containing captures of individual devices in an environment shielded from radio interference in order to study the ground truth of various smartphone models.
In order to study the signature of each device independently, it is necessary to take capture in an isolated environment (anechoic chamber) in which the only Wi-Fi equipment present are the sniffer and the smartphone to examine. 
This allows also to identify transmission patterns or features that distinguish each smartphone from the others, considering different vendors and operating systems.

The purpose of the study is to realize people counting systems based on probe request sniffing, that can overcome the issue of mac address randomization, that is performed in most of new [Android](https://source.android.com/devices/tech/connect/wifi-mac-randomization) and [iOS](https://support.apple.com/en-gb/guide/security/secb9cb3140c/web) devices.

This simple script can be used to capture Wi-Fi packets via interfaces that support [monitor mode](https://en.wikipedia.org/wiki/Monitor_mode).

This algorithm configures the sniffing interfaces, starts the sniffing in each interface and saves collected data in files.

Files are renamed specifying device ID, timestamp (as yyyy-month-dd-hour-minute-second, mode and channel (i.e. A-ts-2021-May-21-h11-m57-s24-modeS-ch-1.pcap).

Superuser privileges are needed to run this script (`sudo -E python3 main.py`).

## Configure interfaces
Functions in the file configure_interfaces.py do the following steps:

1) get the names of the wi-fi interfaces;
2) check if the interfaces support monitor mode;
3) set to monitor mode the interfaces that supports it;
3) assign a channel to each monitor interface.

Some Wi-Fi interfaces do not support all channels, so there is a loop to try to assign all of them correctly.

## Start sniffing
Functions in the file start_sniffing.py do the following steps:
1) create a folder for the capture data;
2) ask to type the device id;
3) ask to type the device mode;
4) show the timestamp of the capture start and its duration;
5) show the sniffing interfaces, and their assigned channels;
6) prepare the capture filename structure
`{device_id}-ts-{timestamp}-ch{channel}-mode{device_mode}.pcap`;
7) start a different process for the sniffing in each channel;
8) terminate all captures.

Note: steps 2 and 3 are meant for single device captures, they affect only the title of the capture files.

Each sniffing sub-process uses the tcpdump utility and selects the specific interface for capture (‘-i’ followed by the monitor interface ID), avoids address conversion (‘-n’), uses timestamps in  seconds (‘-tt’), prints out the link level header (‘-e’), defines the output pcap file (‘-w’ followed by the filename) and filters only probe requests and beacons ('type mgt subtype probe-req subtype probe-resp subtype beacon’).


## Environment variables
File env_variables_example.py is an example of how the env_variables.py file (excluded with gitignore) should look like.
Example file is meant to be copied and renamed correctly (env_variables.py), in order to change the values of the input variables as desired.

## Requirements
The algorithm requires the installation of `pyric` and `scapy` libraries through pip, and additionally tcpdump utility.

`pip install pyric`

`pip install scapy`

`sudo apt-get install tcpdump -y`
