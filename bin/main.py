## This is the run script 
import Functions as func
import os

# Make ped files
func.ped_files()

# Run  peddy
os.system("bash bin/Peddy.sh")

# Predict Sex
func.AllSexCheckCSV()

# Plots
func.PlotHetRatio('PredictedSex.csv','sample_id', 'het_ratio')