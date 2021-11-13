# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:12:55 2021

@author: benkr
"""
import pandas as pd


def output_data(input=None):

    # Load excel data into pandas dataframe
    #df = pd.read_excel('PA.xlsx')
    df = pd.read_csv("PA_dummy_data.csv")

    # Declare local cache and dataframe columns
    
    gpa = 3.2
    pce = 1000
    gre = "No"
    
    studentB = df.loc[df.GPA <= gpa][df.PCE_Hours <= pce][df.GRE == gre]
    studentB.sort_values(
        by = "GPA",
        ascending = False
    )
    studentB = studentB.sort_values(by='GPA', ascending=False)

    print(studentB.Program)


output_data()
