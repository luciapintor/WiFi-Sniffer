# script by luciapintor90@gmail.com
import pyric.pyw as pyw  # iw functionality
import pyric.utils.channels as pych


def configure_interfaces(channels=None):
    """
    This function sets the monitor mode and assigns the channels.
    """

    # set default channels, if not defined
    if channels is None:
        channels = [1, 6, 11]

    # list for the interfaces that support monitor mode
    # [[phy_id, mon_id, channel_id], ...]
    monitor_list = []

    # check all wi-fi interfaces
    for w_id in pyw.winterfaces():

        # get the interface info
        # es: Card(phy=0, dev='wlan0', ifindex=2)
        w_card = pyw.getcard(w_id)

        # activate the interface
        pyw.up(w_card)

        # check if it supports monitor mode
        if 'monitor' in pyw.devmodes(w_card):

            if pyw.modeget(w_card) == 'monitor':
                # it is already in monitor mode
                m_card = w_card

            else:
                m_card = set_monitor(w_card)

            if m_card is not None:
                # activate the monitor interface
                pyw.up(m_card)

                # set the first unset suitable channel
                for ch in channels:
                    is_ch_set = set_channel_verified(m_card, ch)
                    if is_ch_set:
                        monitor_list.append(['phy{}'.format(m_card.phy), m_card.dev, ch])
                        channels.remove(ch)
                        break

                if len(channels) < 1:
                    break

    return monitor_list


def set_monitor(w_card):
    """
    This function sets the interface to monitor mode as airmon-ng.
    """

    # standard name for the monitor interfaces
    mon_id = "mon{}".format(w_card.phy)

    if mon_id not in pyw.winterfaces():
        # this monitor interface is not set
        # then create a new one
        m_card = pyw.devadd(w_card, mon_id, 'monitor')

        # remove obsolete interface
        pyw.devdel(w_card)

        return m_card

    return None


def set_channel_verified(m_card, channel):
    """
    This function sets the channel and verifies if it is set correctly.
    """

    # set the channel
    pyw.chset(m_card, channel)

    # verify
    ch_freq = pych.ch2rf(channel)
    device_freq = pyw.devinfo(m_card).get('CF', None)

    if device_freq != ch_freq:
        # the channel frequency of the device is not the selected one
        return False

    # the channel frequency of the device is the selected one
    return True
