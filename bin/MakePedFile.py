import pandas as pd
import os
import csv


# Get samples from the vcf file name. Set the file path at the main project path


def ped_files(project_path):

    ## Give path to the vcf files to workout sample names and create ped files

    files = os.listdir(project_path)
    print(files) #prints out the files names with vcf which includes sampleIDs
    # files = ['X111742_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf', 'X111741_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf', 'X011955_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf', 'X111743_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf']

    #split string for sample ID, for loop to iterate over filenames in file list
    samplesID = []
    for word in files:
        samplesID.append(word.split("_")[0])

    FamilyID = samplesID
    PaternalID = [0] * len(samplesID)
    MaternalID = [0] * len(samplesID)
    Sex = ['other'] * len(samplesID)
    Phenotype = [-9] * len(samplesID)

    print('PED files will contain')
    print('FamilyID:' , FamilyID)
    print('SampleID:' , samplesID)
    print('PaternalID:' , PaternalID)
    print('MaternalID:' , MaternalID)
    print('Sex:' , Sex)
    print('Phenotype:' , Phenotype)


    print("------Making PED FILES-----------")
    df = pd.DataFrame(list(zip(FamilyID, samplesID,  PaternalID, MaternalID, Sex, Phenotype)), columns =['FID', 'IID', 'PaternalID', 'MaternalID','Sex', 'Phenotype'])
    print(df)


    #make a directory to store the ped files
    os.popen('mkdir Pedfiles')

    ped = '.ped'
    folder = 'Pedfiles/'
    for sample in range(len(samplesID)):
        print(sample)
        filename = samplesID[sample]
        df2 = df.loc[[sample]]
        print(df2)
        writePath = folder + filename + ped
        with open(writePath, 'w') as f_output:
            tsv_output = csv.writer(f_output, delimiter='\t')
            tsv_output.writerow(df2)

ped_files(os.getcwd())