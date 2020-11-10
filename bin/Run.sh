# This will zip and tbi the vcf files then run the python script
#install programs
bash Enviroment.sh


# 1. VCF file
cd Data/vcf_files
for f in *.vcf; do bgzip $f ; done
for f in *.gz; do tabix -p vcf  $f ; done

cd ../..

# 2. Run python script to create the ped files
python MakePedFile.py $1

# 3. Run peddy function for each file in vcf and ped - match filenames
array=(Data/vcf_files/*) #stores all file paths 
mkdir Data/Peddy
cd /home/dnanexus/

for each in "${array[@]}"; do   
    file=()
    echo $each
    echo "$(echo $each | cut -d"/" -f3 |   head -c 7)" #print filename
    file+="$(echo $each | cut -d"/" -f3 |   head -c 7)" #store in an array to easily pull out name
    echo Data/Pedfiles/${file[@]}.ped
    
    mkdir Data/Peddy/${file[@]} #make folder to run peddy file
    cd Data/Peddy/${file[@]} #move into folder to store results
    python -m peddy -p 4 --plot --prefix ${file[@]} ../../vcf_files/${file[@]}_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz ../../Pedfiles/${file[@]}.ped
    cd ~
    echo "Peddy completed";
done #prints out file paths

# 4. Make a csv to concatonate all the csv files into one csv file

cd Data/Peddy
cat X011955/X011955.sex_check.csv X111741/X111741.sex_check.csv X111742/X111742.sex_check.csv X111743/X111743.sex_check.csv > PredictedSex.csv
sed -i '3d;5d;7d' PredictedSex.csv

