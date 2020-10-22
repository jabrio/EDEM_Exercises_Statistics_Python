#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:01:44 2020

@author: javierbrionesgomez
"""

#01_IMPORT & QUALITY CONTROL

#01.1. IMPORT LIBRARIES

import os
import pandas as pd 
import  numpy as np
import matplotlib.pyplot as plt

#01.2. IMPORT & READ THE DATAFRAME

wbr= pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=";", decimal=",")

#01.3. CHECK THE DATAFRAME

wbr.shape
wbr.head
wbr.tail

#QUALITY CONTROL (QC) OK

#02_DATAFRAME ANALYSIS

#02.1 ANALYSIS OF VARIABLES: QUANTITATIVE
wbr.cnt.describe()
wbr.cnt.mean()
wbr.cnt.std()

#02.1.1 DESCRIPTIVE BASIC PARAMETERS

x=wbr["cnt"]
plt.hist(x)
plt.hist(x, edgecolor="black")
plt.title("Figure 1. washington bikeshare")
plt.ylabel("Frecuency")
plt.xlabel("Number of rented bicycles")

#02.1.2 DESCRIPTIVE ADVANCED PARAMETERS

plt.hist(x, edgecolor="black")
plt.title("Figure 1. washington bikeshare")
plt.ylabel("Frecuency")
plt.xlabel("Number of rented bicycles")
plt.axvline(x=4504,
            linewidth=1,
            linestyle="dashed",
            Color="red",
            label="Mean")
plt.text(6000,100, A)

A= "Mean=4504 \n std=1937 \n n=731"

props=dict(boxstyle="round", facecolor="white", lw=0.5)
T="$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$"%(4504, 1937, 731)
plt.text(6000,100,T, bbox=props)

#02.1.3 GRAPH RESULT

plt.hist(x, edgecolor="black")
plt.title("Figure 1. Daily Bicycle rentals in Washington DC")
plt.ylabel("Frecuency")
plt.xlabel("Number of rented bicycles")
plt.axvline(x=M,
            linewidth=1,
            linestyle="solid",
            Color="red",
            label="Mean")

plt.axvline(x=M+S,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="SD")

plt.axvline(x=M-S,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="SD")

props=dict(boxstyle="round", facecolor="white", lw=0.5)
T="$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$"%(4504, 1937, 731)
plt.text(6750,100,T, bbox=props)

B="$\mathrm{n}=%.0f$"%(N)
plt.text(0,100, B, bbox=props)

M=wbr.cnt.mean()
S=wbr.cnt.std()
N=wbr.cnt.count()

#02.1.4 ADD lEGEND

plt.hist(x, edgecolor="black")
plt.title("Figure 1. Daily Bicycle rentals in Washington DC")
plt.ylabel("Frecuency")
plt.xlabel("Number of rented bicycles")
plt.axvline(x=M,
            linewidth=1,
            linestyle="solid",
            Color="red",
            label="Mean")

plt.axvline(x=M+S,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="SD")

plt.axvline(x=M-S,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="-SD")

plt.legend(loc="upper left", bbox_to_anchor=(0.73,0.98))

B="$\mathrm{n}=%.0f$"%(N)
plt.text(0,128, B, bbox=props)

#02.1 ANALYSIS OF VARIABLES: QUALITATIVE

#PERCENTAGES

mytable=wbr.groupby(["weathersit"]).size()
n=mytable.sum()

mytable_A=(mytable/n)*100
print(mytable_A)

#PLOT

bar_list=["Sunny","Cloudy","Rainy"]
plt.bar(bar_list, mytable_A, edgecolor="black")
plt.title("Figure 1. Percentages of Weather situations")
props=dict(boxstyle="round", facecolor="white", lw=0.5)
B="$\mathrm{n}=%.0f$"%(n)
plt.text(2,59, B, bbox=props)

########### END OF SESSION 03 ###########