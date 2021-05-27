# Author: Katelyn Lindsey
# Date: 5/26/2021
# Question 2

import pandas


# Part 1
def dataTasks():
	"""
	Using a csv file of white house salaries, this function
	prepares the data by removing errors in the data and applying 
	feature engineering to make the data more usable. This is then 
	exported as a new csv file called "wh_salaries.csv".
	"""

	# first, get the csv file
	wh_salaries = pandas.read_csv("https://raw.githubusercontent.com/helloworlddata/white-house-salaries/master/data/converted/2017.csv")


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
dataTasks()
