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

    # capture timestamp
    cap_ts = datetime.now().strftime("%Y-%b-%d-h%H-m%M-s%S")

    # subprocesses list
    cap_sub = []

    for m in monitor_list:
        phy_id, mon_id, channel = m

        filename = '{}/{}-ch{}.pcap'.format(data_folder, cap_ts, channel)

        # start the capture in a subprocess
        cap_sub.append(
            subprocess.Popen(['tcpdump',
                              '-i', mon_id,  # Select the interface
                              '-n',  # Don't convert addresses
                              '-w', filename  # Save output
                              ], stdout=subprocess.PIPE))

    # sleep while sub processes make captures 
    time.sleep(sniffing_duration)

    for sub_proc in cap_sub:
        # terminate the subprocesses
        sub_proc.terminate()
