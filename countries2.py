# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

#get the population of china
china_pop = countries[0][2] 

#get the population of romania
romania_pop = countries[2][2]

multiple_pop = china_pop / romania_pop

print(multiple_pop)	