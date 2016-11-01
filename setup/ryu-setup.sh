#!/usr/bin/env bash

RYU_VERSION="v4.7"

cd ~

#  Dependencies for ryu
sudo apt-get install -y python-routes python-dev

sudo pip install -r ~/iSDX/setup/pip-ryu-requires

#  Ryu install
cd ~
git clone -b $RYU_VERSION git://github.com/osrg/ryu.git
sudo cat iSDX/setup/ryu-flags.py >>ryu/ryu/flags.py
cd ryu

# Below should be temporary until ryu's pip-requires file is fixed
sed -i "s/python_version < '2.7'/(python_version != '2.7' and python_version != '3.0')/" tools/pip-requires
sed -i "s/python_version >= '2.7'/(python_version == '2.7' or python_version == '3.0')/" tools/pip-requires

sudo python ./setup.py install
