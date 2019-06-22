# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

 with open(csvpath, newline="")as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
 print csvreader

 #Variables
  total_months = 0
  total_revenue = 0  

  prev_revenue = 0
  revenue_change = 0
  greatest_increase = ["", 0]
  greatest_decrease = ["", 1]

  revenue_chnages =[]

  # Read files
  with_open(file_to_load) as revenue_data:
  reader = csv.DictReader(revenue_data)

  # Loop through all the rows of data we collect
  for row in reader:

      # Calculate the totals
      total_months = total_months + 1
      total_revenue = total_revenue + int (row["Revenue"])
      # print (row)

      # keep track of changes
      revenue_change = int(row["Revenue"]) - prev_revenue
      # print (revenue_chnage)

      # Reset the value of prev_revenue to the row I completed my analysis
      prev_revenue = int(row["Revenue"])
      # print(prev_revenue)

      #Determine the greatest increase
      if (revenue_chnage > greatest_increase[1]):
          greatest_increase[1] = revenue_chnage
          greatest_increase[0] row["Date"]

      if (revenue_changee < greatest_decrease[1]):
          greatest_decrease[1] = revenue_change
          greatest_decrease[0] = row["Date"]

          revenue_changes.append(int(row["Revenue"]))



      #Calculate the totals
      total_months = total_months + 1
      total_revenue = total_revenue + int(row["Revenue"])


# The total number of months included in the dataset
months = input("what is the total number of months included in the dataset?")

# The net total amount of "Profit/Losses" over the entire period
profit/loss = input("The net total amount of "profit/loss" over the entire period?")

# the average of the changes in "Profit/Losses" over the entire period
Profit/loss = input("the average of the changes in "Profit/Losses" over the entire period?")

# The greatest increase in profits (date and amount) over the entire period
date_amount = input("The greatest increase in profits "date_amount" over the entire period? ")

# The greatest decrease in losses (date and amount) over the entire period
date_amount = input("The greatest decrease in losses "date_amount" over the entire period?")



