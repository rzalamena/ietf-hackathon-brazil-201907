#! /usr/bin/env python3
#
# Get the running configuration.
#
# $ sudo ip vrf exec testnet ./netconf-get-config.py 10.254.254.7

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

def demo(host):
    with manager.connect(host=host, port=830, username="root", password='vagrant', hostkey_verify=False) as m:
        c = m.get_config(source='running').data_xml
        print(c)

if __name__ == '__main__':
    demo(sys.argv[1])
