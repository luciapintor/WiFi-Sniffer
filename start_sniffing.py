# script by luciapintor90@gmail.com
import os
import time
import subprocess
from datetime import datetime


def start_sniffing(monitor_list, sniffing_duration=1200, starting_delay=60):
    """
    This function starts the sniffing in a list of interfaces
    that already activated the monitor mode.
    """

    # manage data folder
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # ask device id
    print('Type the device id:')
    device_id = input()

    # ask mode
    mode_list = [
        'ND - No device (background noise measure)',
        'S - Standby screen (WiFi on and no Power Saving)',
        'A - Active screen (WiFi on and no Power Saving)',
        'PS - Power Saving with Standby screen',
        'PA - Power Saving with Active screen',
        'WS - WiFi off with Standby screen',
        'WA - WiFi off with Active screen',
    ]

    for mode in mode_list:
        print(mode)

    print('Type the device mode acronym:')
    device_mode = input()
    print("starting in {} secs".format(starting_delay))
    time.sleep(starting_delay)

    # capture timestamp
    cap_ts = datetime.now().strftime("%Y-%b-%d-h%H-m%M-s%S")
    print("Capture started at {}".format(cap_ts))
    print("Capture duration: {} minutes".format(int(sniffing_duration / 60)))

    # subprocesses list
    cap_sub = []

    for m in monitor_list:
        phy_id, mon_id, channel = m

        filename = '{}/{}-ts-{}-ch{}-mode{}.pcap'.format(data_folder, device_id, cap_ts, channel, device_mode)

        # start the capture in a subprocess
        cap_sub.append(
            subprocess.Popen(['tcpdump',
                              '-i', mon_id,  # Select the interface
                              '-n',  # Don't convert addresses
                              '-tt',  # Timestamp seconds
                              '-e',  # Link level header is printed out
                              '-w', filename,  # Save output
                              'type', 'mgt',
                              'subtype', 'probe-req',  # get probe requests
                              'subtype', 'probe-resp',  # get probe responses
                              'subtype', 'beacon',  # get AP beacons
                              ], stdout=subprocess.PIPE))

    # sleep while sub processes make captures 
    time.sleep(sniffing_duration)

    for sub_proc in cap_sub:
        # terminate the subprocesses
        sub_proc.terminate()

    print("Capture ended")
