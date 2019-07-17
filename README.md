# IETF Hackathon Brazil 2019/07

Table of Contents:

  * [Hardware Requirements](#hardware-requirements)
  * [Software Requirements](#software-requirements)
  * [Usage](#usage)
  * [Notes](#notes)
  * [Topology](#topology)
  * [Troubleshooting](#troubleshooting)


## Hardware Requirements

The minimal hardware specification in order to run the topology:

  * Dual core CPU (to help with interactivity);
  * 4 GB of RAM (2GB only to spawn the routers, 192MB each);
  * 8 GiB of storage space for VirtualBox images and snapshots;

    * 2 GiB of storage for the vagrant box image;
    * 6 GiB of storage for the unpacked box image and the VMs snapshots;


## Software Requirements

The virtualization software is portable and should run on a few OSes:

  * Linux
  * Windows PowerShell 3 or later
  * FreeBSD
  * Mac OS X
  * Solaris

The following applications are required:

  * Vagrant: https://www.vagrantup.com/downloads.html
  * VirtualBox: https://www.virtualbox.org/wiki/Downloads


## Usage

  1. Install VirtualBox;
  2. Install Vagrant (use the site installer even on Linux);
  3. Set up a new 'exercise' folder for all the download files;
  4. Download the vagrant box file for the IETF hackathon exercise
      from http://br-hackathon.netdef.org/ietf-hackathon-br-201907.box
  5. Download or clone the IETF hackathon exercise repository (where
     this file is located) to the same exercise folder;
  6. Deploy the topology with vagrant:

         # Clone the git repo.
         git clone \
           https://github.com/rzalamena/ietf-hackathon-brazil-201907.git

         # Go to the appropriated directory.
         cd ietf-hackathon-brazil-201907

         # Add the box to our local repository.
         vagrant box add --name ietf-hackathon-br-201907 \
           http://br-hackathon.netdef.org/ietf-hackathon-br-201907.box
         # or
         vagrant box add --name ietf-hackathon-br-201907 ietf-hackathon-br-201907.box

         # Deploy the topology with vagrant.
         vagrant up

  7. Do the exercises;


## Notes

  * `root` account has no password;
  * `vagrant` user with password `vagrant` can become `root` with
    `sudo su -`;
  * Alternatively you can log in into the routers with
    `vagrant ssh r<number>`;


## Topology

![Network Topology](topology.png)


## Troubleshooting

 * One of the VMs failed to boot or configure

       # Assuming VM h2 (host 2) failed for some reason or you want to
       # reset it, then you can do the following:

       # Destroy the VM
       vagrant destroy -f h2

       # Re-deploy it
       vagrant up h2

 * I want to manually ssh into the VM

       # Look up the `ssh_port` in the `Vagrantfile`.
       #
       # Example: ssh to host 1, ssh_port = 22101
       ssh -p 22101 vagrant@localhost

       # Password is `vagrant` and root can be accessed with `sudo`.

 * Testing host 1 or host 2 connectivity

       # Testing conectivity between host 1 and router 1.
       sudo ip vrf exec testnet ping 172.16.1.10

       # Testing connectivity between host 1 and host 2 (across the network).
       sudo ip vrf exec testnet traceroute -n 172.16.7.20
       sudo ip vrf exec testnet traceroute -n 172.16.8.20
       sudo ip vrf exec testnet traceroute -n 172.16.9.20
       sudo ip vrf exec testnet traceroute -n 172.16.10.20

       # Testing conectivity between host 2 and routers 7, 8, 9 and 10.
       sudo ip vrf exec r7-vrf ping 172.16.7.10
       sudo ip vrf exec r8-vrf ping 172.16.8.10
       sudo ip vrf exec r9-vrf ping 172.16.9.10
       sudo ip vrf exec r10-vrf ping 172.16.10.10

       # Testing conectivity between host 2 and host 1 (across the network).
       sudo ip vrf exec r7-vrf traceroute -n 172.16.1.20
