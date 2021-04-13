# script by luciapintor90@gmail.com
import os
import time
import subprocess
from datetime import datetime


def start_sniffing(monitor_list, sniffing_duration=10):
    """ This function starts the sniffing in a list of interfaces
        that already activated the monitor mode
    """

    # manage data folder
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # ask mode
    mode_list = [
        'A - Active screen (WiFi on and no Power Saving)',
        'S - Standby (WiFi on and no Power Saving)',
        'PA - Power Saving with Active screen',
        'PS - Power Saving with Standby',
        'WA - WiFi off with Active screen',
        'WS - WiFi off with Standby',
    ]

    for mode in mode_list:
        print(mode)

    device_mode = input('Type the smartphone mode acronym:\n')

    # capture timestamp
    cap_ts = datetime.now().strftime("%Y-%b-%d-h%H-m%M-s%S")
    print("Capture started at {}".format(cap_ts))

    # subprocesses list
    cap_sub = []

    for m in monitor_list:
        phy_id, mon_id, channel = m

        filename = '{}/{}-ch{}-mode{}.pcap'.format(data_folder, cap_ts, channel, device_mode)

        # start the capture in a subprocess
        cap_sub.append(
            subprocess.Popen(['tcpdump',
                              '-i', mon_id,  # Select the interface
                              '-n',  # Don't convert addresses
                              '-tt',  # Timestamp seconds
                              '-e',  # Link level header is printed out
                              'type', 'mgt', 'subtype', 'probe-req',
                              '-w', filename,  # Save output
                              ], stdout=subprocess.PIPE))

    # sleep while sub processes make captures 
    time.sleep(sniffing_duration)

    for sub_proc in cap_sub:
        # terminate the subprocesses
        sub_proc.terminate()
