#!/usr/bin/python2

import sys
import os
import glob

os.system('apt-get -y install libssl-dev libnl-genl-3-dev')
os.system('wget http://w1.fi/releases/hostapd-2.2.tar.gz -O /opt/hostapd.tar.gz')
os.system('cd /opt && tar -zxf hostapd.tar.gz')
os.system('git clone https://github.com/OpenSecurityResearch/hostapd-wpe.git /opt/hostapd-wpe')
os.system('cd /opt/hostapd-2.2 && patch -p1 < ../hostapd-wpe/hostapd-wpe.patch')
os.system('cd /opt/hostapd-2.2/hostapd && sed -i "s/#CONFIG_LIBNL32=y/CONFIG_LIBNL32=y/" .config')
os.system('cd /opt/hostapd-2.2/hostapd && make')
os.system('cd /opt/hostapd-wpe/certs && ./bootstrap && cd /opt/arsenal')
