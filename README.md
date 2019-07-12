# IETF Hackathon Brazil 2019/07

## Hardware Requirements

The minimal hardware specification in order to run the topology:

  * Dual core CPU (to help with interactivity);
  * 4 GB of RAM (2GB only to spawn the routers, 192MB each);
  * 8 GiB of storage space for VirtualBox images and snapshots;

    * 2 GiB of storage for the vagrant box image;
    * 6 GiB of storage for the unpacked box image and the VMs snapshots;


## Software Requirements

The virtualization software is portable and should run on a few OSes:

  * Linux;
  * Windows;
  * FreeBSD;
  * Mac OS X;
  * Solaris;

The following applications are required:

  * Vagrant: https://www.vagrantup.com/downloads.html ;
  * VirtualBox: https://www.virtualbox.org/wiki/Downloads ;


## Usage

  1. Install VirtualBox;
  2. Install Vagrant;
  3. Download the vagrant box for the IETF hackathon exercise;
  4. Download or clone the IETF hackathon exercise repository (where
     this file is located);
  5. Deploy the topology with vagrant:

         # Go to the appropriated directory.
         cd ietf-hackathon-br-201907;

         # Deploy the topology with vagrant.
         vagrant up

  6. Do the exercises;


## Notes

  * `root` account has no password;
  * `vagrant` user with password `vagrant` can become `root` with
    `sudo su -`;
  * Alternatively you can log in into the routers with
    `vagrant ssh r<number>`;


## Topology

![Network Topology](topology.png)
