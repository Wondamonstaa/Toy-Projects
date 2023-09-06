import pandas as pd

import matplotlib.pyplot as plt


"""Imported all the necessary modules to run the program."""

csvfile = open("SCDB_2021_01_justiceCentered_Citation.csv", encoding = 'ISO-8859-1')

#Using pandas (pd) to read the file and preparing to exploit csv format
scdb = pd.read_csv(csvfile)

pd.set_option('display.max_columns' , None)
pd.options.display.max_columns = None



# 1st question 

SCJsubset = scdb[scdb.term>= 2000]

# 2nd question

s = plt.figure(figsize=(10,10))
SCJsubset.groupby("term")["caseId"].nunique().plot(kind="bar", 
                                                     title = 'User', color='darkviolet')

# 3d question 

s = plt.figure(figsize=(20,20))
scdb.groupby(['justiceName' , 'direction'])["voteId"].nunique().plot(kind="bar",
                                                     title = 'User', color='darkviolet')

# 4th question 

csvfile_case = open("/Users/wondamonsta/Downloads/SCDB_2021_01_caseCentered_Citation.csv", encoding = 'ISO-8859-1') 

#Using pandas (pd) to read the file and preparing to exploit csv format
SCJ_pt2 = pd.read_csv(csvfile_case)

SCJ_pt2_subset = SCJ_pt2[SCJ_pt2.term >= 2008]

# 5th question 

s = plt.figure(figsize=(10,10))
SCJ_pt2_subset.groupby("caseDisposition")["caseIssuesId"].count().plot(kind="bar", 
                                                    title = 'User', color='limegreen')

# 6th question 

s = plt.figure(figsize=(10,10))
SCJ_pt2_subset.groupby("partyWinning")["caseId"].count().plot(kind="bar", 
                                                     title = 'User', color='magenta')

#The following plot depicts whether a party has won or not.
# 0.0 stands for  "The petitioning party received an unfavorable disposition" 
# 1.0 stands for "Favorable disposition to the petitioning party"
# 2.0 stands for "Unclear favorable disposition to the petitioning party"
# Analyzing the plot, we can notice that the petitioning party often received a favorable disposition.
