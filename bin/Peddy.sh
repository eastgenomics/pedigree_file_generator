#!/bin/bash 
# 1. VCF file
cd Data/vcf_files
for f in *.vcf; do bgzip $f ; done
for f in *.gz; do tabix -p vcf  $f ; done

cd ../..

echo VCF files are zipped 

# 2. Run peddy function for each file in vcf and ped - match filenames
array=(Data/vcf_files/*)
mkdir Data/Peddy

for each in "${array[@]}"; do   
    file=()
    echo "$(echo $each | cut -d"/" -f3 |   head -c 7)" #print filename
    file+="$(echo $each | cut -d"/" -f3 |   head -c 7)" #store in an array to easily pull out name
    echo Data/Pedfiles/${file[@]}.ped
    
    mkdir Data/Peddy/${file[@]} #make folder to run peddy file
    cd Data/Peddy/${file[@]} #move into folder to store results
    python -m peddy -p 4 --plot --prefix ${file[@]} ../../vcf_files/${file[@]}_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz ../../Pedfiles/${file[@]}.ped
    cd ~;
done #prints out file paths
