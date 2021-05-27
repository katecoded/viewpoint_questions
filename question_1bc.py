# Author: Katelyn Lindsey
# Date: 5/26/2021
# Question 1.b. - 1.c.

import pandas as pd


# Question 1.b.
def upperLower(name_table):
	"""
	Takes a pandas data frame of StudentIDs and Names and 
	returns a new data frame version of name_table where 
	names containing "e" are uppercased, and lowercased otherwise.
	"""

	# create a deep copy of the name_table 
	new_names = pd.DataFrame.copy(name_table)


	# iterate through all rows in new_names, changing names that
	# contain "e" or "E" to uppercase, lowercase otherwise
	for index in range(len(new_names.index)):

		# if the name contains an "e" or "E", change it to uppercase
		if "E" in new_names.iloc[index]["Name"].upper():
			new_names.iloc[index]["Name"] = new_names.iloc[index]["Name"].upper()

		# else, change the name to lowercase
		else:
			new_names.iloc[index]["Name"] = new_names.iloc[index]["Name"].lower()

	# return the new version of name_table
	return new_names


# Question 1.c.
def markAverages(name_table, mark_table):
	"""
	Takes a name table with StudentIDs and Names (that are either all uppercase
	or all lowercase) and a mark_table with StudentIds and Total_marks,
	and returns a dataframe that summarizes the average marks of uppercase
	names and lowercase names.
	"""

	# first, create a merged dataframe with both names and marks of students
	students = pd.merge(name_table, mark_table, on="StudentID")


	# storage for the averages for uppercase and lowercase names
	upper_average = 0
	lower_average = 0

	# storage for the number of uppercase names
	num_upper = 0


	# iterate through the students data frame, adding the marks to 
	# each total to calculate the average
	for index in range(len(students.index)):

		# if the student's name is uppercase, add to the upper average total
		# and increment the number of uppercase names found
		if students.iloc[index]["Name"] == students.iloc[index]["Name"].upper():
			upper_average += students.iloc[index]["Total_marks"]
			num_upper += 1

		# otherwise, add to the lower average total
		else:
			lower_average += students.iloc[index]["Total_marks"]


	# calculate the averages based on the totals while avoiding dividing by 0
	if num_upper > 0:
		upper_average = upper_average / num_upper

	if num_upper < len(students.index):
		lower_average = lower_average / (len(students.index) - num_upper)


	# finally, create the dataframe of averages using a dictionary
	averages = {
		"Lowercase_Average": [lower_average],
		"Uppercase_Average": [upper_average]
	}

	averages = pd.DataFrame(averages)


	# return the dataframe of averages
	return averages
