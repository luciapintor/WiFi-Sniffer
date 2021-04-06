# script by luciapintor90@gmail.com

from configure_interfaces import configure_interfaces
from start_sniffing import start_sniffing
from env_variables import channels, sniffing_duration

monitor_list = configure_interfaces(channels)
print(monitor_list)
start_sniffing(monitor_list, sniffing_duration)
