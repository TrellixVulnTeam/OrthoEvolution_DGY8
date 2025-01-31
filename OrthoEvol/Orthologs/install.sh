#!/bin/bash
# For Debian/Ubuntu sudo users
# You may have to use apt-get for older versions of Ubuntu
sudo apt update; sudo apt upgrade

# Install the packages
sudo apt install clustalo paml phyml ncbi-blast+ phylip prank iqtree mafft clustalw
echo "All packages installed."

#-----------------------------------------------------------------------
# For installing/compiling from source
# Uncomment packages that you cannot install using apt or sudo.
# Pal2Nal and Guidance 2 must be installed from source and added to your path.

# Install clustal omega
#wget http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz -O /tmp/clustalo.tar.gz
#tar -xvf /tmp/clustalo.tar.gz
#export PATH=$PATH:$PWD/clustalo-1.2.4-Ubuntu-x86_64/bin/

# Install IQ-Tree
#wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.5.5/iqtree-1.5.5-Linux.tar.gz -O /tmp/iqtree.tar.gz
#tar -xvf /tmp/iqtree.tar.gz
#export PATH=$PATH:$PWD/iqtree-1.5.5-Linuxbin/

# Install PAL2NAL
wget http://www.bork.embl.de/pal2nal/distribution/pal2nal.v14.tar.gz -O /tmp/pal2nal.tar.gz
tar -xvf /tmp/pal2nal.tar.gz
export PATH=$PATH:$PWD/pal2nal.v14/bin/

# Install Guidance2
wget http://www.bork.embl.de/pal2nal/distribution/pal2nal.v14.tar.gz -O /tmp/pal2nal.tar.gz
tar -xvf /tmp/pal2nal.tar.gz
export PATH=$PATH:$PWD/pal2nal.v14/bin/