# pizza sales insight

In this project i analysed sales data for a pizza company for one year. The dataset were taken from https://www.mavenanalytics.io/blog/maven-pizza-challenge. The goal of this project is to create a dashboard with an intent to answer these questions:

a) What days and times do we tend to be most engrossed?

b) How many customers do we have each day? Are there any peak hours?

c) How many orders are we expecting each day?

d) What are our best and worst selling pizzas?

e) What's our average order value?

f) How much money did we make this year?

g) Can we identify any seasonality in the sales?

h) Are there any pizzas we should take off the menu, or any promotions we could leverage?

Data organization:

            Dataset contains 4 tables in csv format. I went through it and search for duplicates, any null fields in excel and cleaned it. Then created tables and established relationships between them using popsql with a well defined schema. While feeding data into my table i encountered issues with one table and found out issue was with delimiter of one particular column and resolved it with python. 

The link to my database schema is https://popsql.com/queries/-NlSc5LnqMfZBoVmtJlL/restaurant-sql?access_token=5e51842d4546670948b495125b7faadb

Analysis:
      You could use my dashboard file to get visual. These are my conclusions from this analysis

a) Classic and Supreme pizza category has the most sales while Chicken and Veggie category is least

b) Large pizza size has done most sales while xl and xxl done very neglible sales

c) Fridays has peak orders while sundays are relatively quieter

d) Orders peaked at noon 12 - 1 and less orders at morning 9 - 10

e) July month has done most number of sales while october has least

Insights:

a) From the analysis customers do not prefer pizza on morning 9-10. So you could add breakfast options to up the sales during that time

b) While order numbers in sundays are concerning. So you could give discounts on that day 

Future:
  Could have done a comprehensive analysis if datasets include customer data, inventory management 

  Thank you for taking time and reading this.
