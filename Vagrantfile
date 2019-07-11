#!/usr/bin/env ruby

routers = [
  {
    hostname: 'r1',
    ssh_port: 22001,
    interfaces: [
      {
        net: 'r1-r2',
        address: '10.1.1.10/24'
      },
      {
        net: 'r1-r3',
        address: '10.1.2.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0001.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r2',
    ssh_port: 22002,
    interfaces: [
      {
        net: 'r1-r2',
        address: '10.1.1.20/24'
      },
      {
        net: 'r2-r3',
        address: '10.2.1.10/24'
      },
      {
        net: 'r2-r4',
        address: '10.2.2.10/24'
      },
      {
        net: 'r2-r5',
        address: '10.2.3.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0010.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r3',
    ssh_port: 22003,
    interfaces: [
      {
        net: 'r1-r3',
        address: '10.1.2.20/24'
      },
      {
        net: 'r2-r3',
        address: '10.2.1.20/24'
      },
      {
        net: 'r3-r5',
        address: '10.2.4.10/24'
      },
      {
        net: 'r3-r6',
        address: '10.2.5.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0020.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r4',
    ssh_port: 22004,
    interfaces: [
      {
        net: 'r2-r4',
        address: '10.2.2.20/24'
      },
      {
        net: 'r4-r5',
        address: '10.3.1.10/24'
      },
      {
        net: 'r4-r7',
        address: '10.3.2.10/24'
      },
      {
        net: 'r4-r8',
        address: '10.3.3.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0100.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r5',
    ssh_port: 22005,
    interfaces: [
      {
        net: 'r2-r5',
        address: '10.2.3.20/24'
      },
      {
        net: 'r3-r5',
        address: '10.2.4.20/24'
      },
      {
        net: 'r4-r5',
        address: '10.3.2.10/24'
      },
      {
        net: 'r5-r6',
        address: '10.3.4.10/24'
      },
      {
        net: 'r5-r8',
        address: '10.3.5.10/24'
      },
      {
        net: 'r5-r9',
        address: '10.3.6.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s17
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s18
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0200.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r6',
    ssh_port: 22006,
    interfaces: [
      {
        net: 'r3-r6',
        address: '10.2.5.20/24'
      },
      {
        net: 'r5-r6',
        address: '10.3.4.20/24'
      },
      {
        net: 'r6-r9',
        address: '10.3.7.10/24'
      },
      {
        net: 'r6-r10',
        address: '10.3.8.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.0300.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r7',
    ssh_port: 22007,
    interfaces: [
      {
        net: 'r4-r7',
        address: '10.3.2.20/24'
      },
      {
        net: 'r7-r8',
        address: '10.4.1.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.1000.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r8',
    ssh_port: 22008,
    interfaces: [
      {
        net: 'r4-r8',
        address: '10.3.3.20/24'
      },
      {
        net: 'r5-r8',
        address: '10.3.5.20/24'
      },
      {
        net: 'r7-r8',
        address: '10.4.1.20/24'
      },
      {
        net: 'r8-r9',
        address: '10.4.2.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.2000.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r9',
    ssh_port: 22009,
    interfaces: [
      {
        net: 'r5-r9',
        address: '10.3.6.20/24'
      },
      {
        net: 'r6-r9',
        address: '10.3.7.20/24'
      },
      {
        net: 'r8-r9',
        address: '10.4.2.20/24'
      },
      {
        net: 'r9-r10',
        address: '10.4.3.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s10
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s16
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.3000.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  },

  {
    hostname: 'r10',
    ssh_port: 22010,
    interfaces: [
      {
        net: 'r6-r10',
        address: '10.3.8.20/24'
      },
      {
        net: 'r9-r10',
        address: '10.4.3.20/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      hostname "$1"
      echo "hostname $1" > /etc/frr/vtysh.conf
      echo "hostname $1" > /etc/frr/zebra.conf

      cat > /etc/frr/isisd.conf <<EOF
      interface enp0s8
       ip router isis testnet
       isis circuit-type level-1
      !
      interface enp0s9
       ip router isis testnet
       isis circuit-type level-1
      !
      router isis testnet
       net 10.0000.0000.0000.0000.0000.0000.0000.0000.4000.00
       redistribute ipv4 connected level-1
      !
      EOF

      systemctl restart frr
    SCRIPT
  }
]

Vagrant.configure('2') do |config|
  # Machines setup.
  config.vm.box = 'ietf-hackathon-br-201907'
  # Disable sharing local folder.
  config.vm.synced_folder '.', '/vagrant', disabled: true

  # Configure all routers.
  routers.each do |router|
    config.vm.define router[:hostname] do |node|
      # Configure network interfaces.
      router[:interfaces].each do |interface|
        node.vm.network :private_network,
          ip: interface[:address],
          virtualbox__intnet: interface[:net]
      end

      # Virtual Box settings.
      node.vm.provider :virtualbox do |provider|
        provider.default_nic_type = 'virtio'
        provider.linked_clone = true
        provider.customize ['modifyvm', :id, '--cpuexecutioncap', '50']
      end

      # VM settings.
      if router[:ssh_port]
        node.vm.network :forwarded_port, protocol: :tcp,
          guest: 22, host: router[:ssh_port]
      end

      # Apply provisions / configuration script.
      if router[:config]
        node.vm.provision :shell do |script|
          script.inline = router[:config]
          script.args = [router[:hostname]]
        end
      end
    end
  end
end
