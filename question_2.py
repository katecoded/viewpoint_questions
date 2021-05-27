# Author: Katelyn Lindsey
# Date: 5/26/2021
# Question 2

import pandas as pd
import matplotlib.pyplot as plt


# Part 1
def dataTasks():
	"""
	Using a csv file of white house salaries, this function
	prepares the data by removing errors in the data and applying 
	feature engineering to make the data more usable. This is then 
	exported as a new csv file called "wh_salaries.csv".
	"""

	# first, read the csv file
	wh_salaries = pd.read_csv("https://raw.githubusercontent.com/helloworlddata/white-house-salaries/master/data/converted/2017.csv")


	# fix errors in the csv file - some enties for position title are mistakenly
	# in the pay basis column, so they must be moved

	# first, get all of the columns that have missing positions
	need_positions = wh_salaries.loc[wh_salaries["POSITION TITLE"].isnull()]

	# iterate through those indices, taking the position from the 
	# pay basis and moving it to the position title
	for index in need_positions.index:

		# get the pay basis string and chop off the pay basis 
		# to get the position
		position = wh_salaries.iloc[index]["PAY BASIS"]
		position = position[10:]

		# now, get just the pay basis
		pay_basis = wh_salaries.iloc[index]["PAY BASIS"]
		pay_basis = pay_basis[:10]

		# finally, update the position title and pay basis for that row
		wh_salaries.iloc[index]["POSITION TITLE"] = position
		wh_salaries.iloc[index]["PAY BASIS"] = pay_basis


	# next, remove the pay basis column since it has no variety in its data
	del wh_salaries["PAY BASIS"]


	# next, remove the outliers in the data that have salaries of $0.00
	wh_salaries = wh_salaries[wh_salaries["SALARY"] > "$0.00"]


	# finally, export the new csv file as "wh_salaries.csv"
	wh_salaries.to_csv('wh_salaries.csv')

# perform the data preparation
# dataTasks()


# Part 2
def describeData():
	"""
	Using a csv file of numerical values, this function calculates
	the minimum, maximum, median, and mean (average) of the data, and then 
	calculates the standard deviation of the data. Returns a data frame
	of the calculated values.
	"""

	# first, read the csv file and sort the second column in ascending order
	num_data = pd.read_csv("https://raw.githubusercontent.com/fractalbass/data_engineer/master/data.csv", header=None)	
	num_data.sort_values(num_data.columns[1], inplace = True)


	# an empty dictionary to store the descriptive statistics for the given data
	desc_stats = {}


	# get the minimum and maximum and add them to the dictionary
	desc_stats["minimum"] = [num_data[1].min()]
	desc_stats["maximum"] = [num_data[1].max()]

	# calculate the median and adds it to the dictionary
	desc_stats["median"] = [(num_data.iloc[len(num_data.index) // 2][1] + num_data.iloc[len(num_data.index) // 2 + 1][1]) / 2]

	# calculate and add the mean to the dictionary
	desc_stats["mean"] = [num_data[1].mean()]

	# finally, calculate the standard deviation
	desc_stats["std_deviation"] = [num_data[1].std()]

	# create a histogram of the data
	num_data[1].plot.hist()
	plt.xlabel("Num Data")
	plt.ylabel("Frequency")
	plt.title("Data Distribution of data.csv")
	# plt.show()


	# return the information as a data frame
	desc_stats = pd.DataFrame(desc_stats)
	return desc_stats


# describe the data
# print(describeData())
