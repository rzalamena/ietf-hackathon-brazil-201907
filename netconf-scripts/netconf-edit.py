#! /usr/bin/env python3
#
# Change the running configuration using edit-config
# and the test-option provided by the :validate capability.
#
# $ sudo ip vrf exec testnet ./netconf-edit.py 10.254.254.7

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

def demo(host):
    snippet = """
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <isis xmlns="http://frrouting.org/yang/isisd">
          <instance>
            <area-tag>testnet</area-tag>
            <is-type>level-1</is-type>
          </instance>
        </isis>
      </config>"""

    with manager.connect(host=host, port=830, username="root", password='vagrant', hostkey_verify=False) as m:
        assert(":validate" in m.server_capabilities)
        m.edit_config(target='running', config=snippet,
                      test_option='test-then-set')

if __name__ == '__main__':
    demo(sys.argv[1])
