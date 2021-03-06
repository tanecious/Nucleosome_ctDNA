#! /usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import numpy

#Initialize binning matrix
matrix_fpkm = [[0 for x in range(30)] for y in range(30)] 
for x in range(30):
    for y in range(30):
        matrix_fpkm[x][y]=list()

#Initialize binning matrix for percentiles
matrix_perc = [[0 for x in range(30)] for y in range(30)] 
for x in range(30):
    for y in range(30):
        matrix_perc[x][y]=list()

input_file="./output/Quantitative/MergedControls_FPKM.txt"
INFILE = open(input_file,"r")
header=INFILE.readline()

output_file="./output/Quantitative/MergedControls_FPKM_binned.txt"
OUTFILE = open(output_file,"w")

for line in INFILE.readlines():
    info = line.rstrip().split("\t")
    TwoK_TSS = float(info[2])
    NDR = float(info[3])
    fpkm = float(info[4])
    perc = float(info[6])
    if TwoK_TSS >= 30 or NDR >= 30:
        continue
    matrix_fpkm[int(math.floor(TwoK_TSS))][int(math.floor(NDR))].append(fpkm)
    matrix_perc[int(math.floor(TwoK_TSS))][int(math.floor(NDR))].append(perc)

OUTFILE.write("2K-TSS\tNDR\tFPKM\tCount\tFPKM_percentile\n")
for x in range(30):
    for y in range(30):
        if len(matrix_fpkm[x][y]) == 0:
            OUTFILE.write(str(x)+"\t"+str(y)+"\tNA\t0\tNA\n") 
        else:
            OUTFILE.write(str(x)+"\t"+str(y)+"\t"+str(numpy.mean(matrix_fpkm[x][y]))+"\t"+str(len(matrix_fpkm[x][y]))+"\t"+str(numpy.mean(matrix_perc[x][y]))+"\n")

