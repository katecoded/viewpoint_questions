# Author: Katelyn Lindsey
# Date: 5/26/2021
# Testing file for question_1bc.py


import pandas

from question_1bc import *


# create name table
name_table = {
	"StudentID": ["V001", "V002", "V003", "V004"],
	"Name": ["Abe", "Abhay", "Acelin", "Adelphos"]
}

name_table = pandas.DataFrame(name_table)


# create mark table
mark_table = {
	"StudentID": ["V001", "V002", "V003", "V004"],
	"Total_marks": [95, 80, 74, 81]
}

mark_table = pandas.DataFrame(mark_table)


# test that this returns a name_table with names lowercased
# and uppercased as needed
print(upperLower(name_table))

# test that this returns a dataframe with average marks
# for uppercase and lowercase names
print(markAverages(upperLower(name_table), mark_table))
