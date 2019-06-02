#
# Script to Install
# Linux Tools
#
# The Python Quants GmbH
#
apt-get update
apt-get upgrade -y

# Linux System Tools
apt-get install -y wget bzip2 screen htop vim man less

# Python3 via Linux
apt-get install -y python3 python3-pip
pip3 install pip --upgrade
pip install ipython pandas pyzmq q nose

cp 04_vimrc.txt /root/.vimrc
