## Script runs modules needed

## 1. Peddy
INSTALL_PATH=~/anaconda
wget http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest* -fbp $INSTALL_PATH

PATH=$INSTALL_PATH/bin:$PATH

conda update -y conda
conda config --add channels bioconda
conda install -y peddy

## 2. bgzip
sudo apt-get install -y tabix




