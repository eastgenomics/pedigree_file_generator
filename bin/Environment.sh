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

# install pip
/usr/bin/python3 -m pip install --upgrade pip
sudo python -m pip install pandas


# ##############################     XYalign
# ### conda set up
# INSTALL_PATH=~/anaconda
# wget http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
# bash Miniconda2-latest* -fbp $INSTALL_PATH

# PATH=$INSTALL_PATH/bin:$PATH


# conda config --add channels defaults

# conda config --add channels conda-forge

# conda config --add channels bioconda

# conda create -n xyalign_env xyalign

# source activate xyalign_env


# xyalign --PREPARE_REFERENCE --ref ucsc_hg19.fa.fai \
# --output_dir sample1_output --sample_id sample1 --cpus 4 --reference_mask mask.bed \
# --x_chromosome chrX --y_chromosome chrY

# # par regions mask https://www.biostars.org/p/228498/
# curl -s ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.14_GRCh37.p13/GCA_000001405.14_GRCh37.p13_assembly_regions.txt | grep PAR > PARmask.bed

# xyalign --ANALYZE_BAM --ref ucsc_hg19.fa --bam X011955_markdup.bam \
# --output_dir sample1_output2 --sample_id sample1_2 --cpus 4 --window_size 10000 \
# --chromosomes chrX chrY --x_chromosome chrX --y_chromosome chrY

# xyalign --CHARACTERIZE_SEX_CHROMS --ref ucsc_hg19.fa --bam X011955_markdup.bam \
# --output_dir sample1_output --sample_id sample1 --cpus 4 --window_size 10000 \
# --chromosomes 19 X Y --x_chromosome X --y_chromosome Y --skip_compatibility_check
 
# sed -i 's/chrX/X/' PARmask.bed
# sed -i 's/chrY/Y/' PARmask.bed

# sed -i 's/chr//' ucsc_hg19.fa

# ###full pipeline
# xyalign --ref ucsc_hg19.fa --bam X011955_markdup.bam \
# --output_dir sample1_output --sample_id sample1 --cpus 4 --reference_mask PARmask.bed \
# --window_size 10000 --chromosomes X Y \
# --x_chromosome X --y_chromosome Y  --skip_compatibility_check