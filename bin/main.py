## This is the run script 
import Functions as func
import os

# Make ped files
func.ped_files()

# Run  peddy
os.system("sh bin/Peddy.sh")

# Predict Sex
func.AllSexCheckCSV()

# Plots
