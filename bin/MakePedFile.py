import pandas as pd
import os


# df = pd.read_csv("/home/aisha/Downloads/SampleSheet2.csv")

# # Pull out the column we want and make it to the right object type(list)
# colnames = df.loc[[20]]
# colnames = colnames.values.tolist()
# colnames = colnames[0]
# print(colnames[0])

# # Drop irrelevant data and rename header 
# df = df.drop(df.index[0:21])
# df.columns = colnames
# print(df.head(10))

# # Pull out unique Sample_IDs
# sampleIDs = df.iloc[:,1]
# sampleIDs = list(set(sampleIDs))
# print(sampleIDs)

#######################
# Get samples from the vcf file name

#import os
#arr = os.listdir('/home/dnanexus/Project/Data/vcf_files')
#print(arr)

arr = ['X111742_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf', 'X111741_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz', 'X111741_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz.tbi', 'X011955_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz', 'X011955_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz.tbi', 'X111743_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz', 'X111743_markdup_recalibrated_Haplotyper.refseq_nirvana_2010.annotated.vcf.gz.tbi']

#split string for sample ID, for loop to iterate over words array
samplesID = []
for word in arr:
    samplesID.append(word.split("_")[0])

FamilyID = samplesID
PaternalID = [0] * len(samplesID)
MaternalID = [0] * len(samplesID)
Sex = [1] * len(samplesID)
Phenotype = [-9] * len(samplesID)

print('PED files will contain')
print('FamilyID:' , FamilyID)
print('SampleID:' , samplesID)
print('PaternalID:' , PaternalID)
print('MaternalID:' , MaternalID)
print('Sex:' , Sex)
print('Phenotype:' , Phenotype)

from collections import OrderedDict

print("------Making PED FILE-----------")
df = {'FID':FamilyID, 'IID': samplesID, 'PaternalID':PaternalID, 'MaternalID':MaternalID, 'Phenotype':Phenotype, 'Sex':Sex}
print(df)


df = pd.DataFrame(df)
print(df)

writePath = "SamplePEDs.ped"
f = open(writePath, 'w')
with open(writePath, 'w') as f:
    f.write(
        df.to_string(header = True, index = False)
    )
f.close()

df2 = df.loc[[0]]

writePath = "Sample1.ped"
f = open(writePath, 'w')
with open(writePath, 'w') as f:
    f.write(
        df2.to_string(header = False, index = False)
    )
f.close()


