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
      },
      {
        net: 'h1-r1',
        address: '172.16.1.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.1/32
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
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.2/32
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
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.3/32
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
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.4/32
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
        address: '10.3.1.20/24'
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
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.5/32
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
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.6/32
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
      },
      {
        net: 'h2-r7',
        address: '172.16.7.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.7/32
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
      },
      {
        net: 'h2-r8',
        address: '172.16.8.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.8/32
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
      },
      {
        net: 'h2-r9',
        address: '172.16.9.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.9/32
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
      },
      {
        net: 'h2-r10',
        address: '172.16.10.10/24'
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
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

      cat >> /etc/frr/zebra.conf <<EOF
      interface lo
       ip address 10.254.254.10/32
      !
      EOF

      systemctl restart frr
    SCRIPT
  }
]

hosts = [
  {
    hostname: 'h1',
    ssh_port: 22101,
    interfaces: [
      {
        net: 'h1-r1',
        address: '172.16.1.20/24',
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
      hostname "$1"

      apt install -y tcpreplay
    SCRIPT
  },

  {
    hostname: 'h2',
    ssh_port: 22102,
    interfaces: [
      {
        net: 'h2-r7',
        address: '172.16.7.20/24',
      },
      {
        net: 'h2-r8',
        address: '172.16.8.20/24',
      },
      {
        net: 'h2-r9',
        address: '172.16.9.20/24',
      },
      {
        net: 'h2-r10',
        address: '172.16.10.20/24',
      }
    ],
    config: <<~SCRIPT
      echo "$1" > /etc/hostname
      echo "127.0.1.1 $1" >> /etc/hosts
      hostname "$1"

      cat > /home/vagrant/bin/network-setup.sh <<EOF
      sudo ip link add r7-vrf type vrf table 7
      sudo ip link add r8-vrf type vrf table 8
      sudo ip link add r9-vrf type vrf table 9
      sudo ip link add r10-vrf type vrf table 10

      sudo ip link set r7-vrf up
      sudo ip link set r8-vrf up
      sudo ip link set r9-vrf up
      sudo ip link set r10-vrf up

      sudo ip link set enp0s8 vrf r7-vrf
      sudo ip link set enp0s9 vrf r8-vrf
      sudo ip link set enp0s10 vrf r9-vrf
      sudo ip link set enp0s16 vrf r10-vrf

      sudo ip route add default via 172.16.7.10 vrf r7-vrf
      sudo ip route add default via 172.16.8.10 vrf r8-vrf
      sudo ip route add default via 172.16.9.10 vrf r9-vrf
      sudo ip route add default via 172.16.10.10 vrf r10-vrf
      EOF

      chmod a+x /home/vagrant/bin/network-setup.sh
      sudo bash /home/vagrant/bin/network-setup.sh
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
        # Use virt interfaces to help reduce CPU usage on emulation.
        provider.default_nic_type = 'virtio'

        # Cheap copy VM disk.
        provider.linked_clone = true

        # Attempt to avoid utilizing all host CPU cycles.
        provider.cpus = 1
        provider.customize ['modifyvm', :id, '--cpuexecutioncap', '50']

        # Select the amount of memory the VMs will have.
        provider.memory = 192
        #provider.memory = 256
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

  # Configure all hosts.
  hosts.each do |host|
    config.vm.define host[:hostname] do |node|
      # Configure network interfaces.
      host[:interfaces].each do |interface|
        node.vm.network :private_network,
          ip: interface[:address],
          virtualbox__intnet: interface[:net]
      end

      # Virtual Box settings.
      node.vm.provider :virtualbox do |provider|
        # Use virt interfaces to help reduce CPU usage on emulation.
        provider.default_nic_type = 'virtio'

        # Cheap copy VM disk.
        provider.linked_clone = true

        # Attempt to avoid utilizing all host CPU cycles.
        provider.cpus = 1
        provider.customize ['modifyvm', :id, '--cpuexecutioncap', '50']

        # Select the amount of memory the VMs will have.
        provider.memory = 200
      end

      # VM settings.
      if host[:ssh_port]
        node.vm.network :forwarded_port, protocol: :tcp,
          guest: 22, host: host[:ssh_port]
      end

      # Apply provisions / configuration script.
      if host[:config]
        node.vm.provision :shell do |script|
          script.inline = host[:config]
          script.args = [host[:hostname]]
        end
      end
    end
  end
end
