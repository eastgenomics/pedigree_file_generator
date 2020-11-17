import pandas as pd
import os
import csv
import glob
import matplotlib.pyplot as plt
import numpy


# Get samples from the vcf file name and make ped files
def ped_files():

    ## Give path to the vcf files to workout sample names and create ped files
    path = os.getcwd()
    project_path = glob.glob(path + '/Data/vcf_files')
    tmp = ''.join(map(str, project_path))
    project_path = tmp
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
    os.popen('mkdir Data/Pedfiles')

    ped = '.ped'
    folder = 'Data/Pedfiles/'
    for sample in range(len(samplesID)):
        print(sample)
        filename = samplesID[sample]
        df2 = df.loc[[sample]]
        writePath = folder + filename + ped
        df2.to_csv(writePath, sep="\t", index=False, header = False)

# Get the outputs from peddy and make a Predicted sex csv file in results folder
def AllSexCheckCSV(): 
    # get all csv files from all subdirectories
    path = os.getcwd()
    print(path + '/Data/Peddy/*/*.sex_check.csv')
    all_files = glob.glob(path + '/Data/Peddy/*/*.sex_check.csv')
    
    #append the list of the rows together
    merged = []
    for file in all_files:
        dat = pd.read_csv(file)  
        merged.append(dat)

    #concat the lists into a dataframe then save csv file in results folder
    df = pd.concat(merged)
    print(df)
    print(path + '/Data/Peddy/' + 'PredictedSex.csv')
    writePath = path + '/Data/Peddy/' + 'PredictedSex.csv'
    df.to_csv(writePath, sep="\t", index=False)

# Plot functions
def PlotHetRatio(file, x, y):
    #file = PredictedSex file
    #x = colname1 (string)
    #y = colname2 (string)
    filepath = "../Data/Peddy/" + file
    dat = pd.read_table(filepath, sep = '\t', index_col=None)
    print(dat)
    # convert the table to dictionary where the keys are column names, then each value has a key where the key is the 
    # sample ID number and the value is the expected value
    dat2 = pd.DataFrame.to_dict(dat)

    # Take out the x values from the dic to a list
    xaxis = []
    for i in range(0,len(dat2[x])):
        xaxis.append(dat2[x][i])

    # Take out the y values from the dic to a list
    yaxis = []
    for i in range(0,len(dat2[y])):
        yaxis.append(dat2[y][i])

    plt.plot(xaxis,yaxis, 'ro')
    plt.axis([-1, len(xaxis), 0, 2]) #[xmin, xmax, ymin, ymax]
    plt.savefig('../Data/Peddy/PredictedSex.png')