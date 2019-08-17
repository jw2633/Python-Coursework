# open the file and read a list of lines
with open("INCounties2015.txt", "r") as f:
    counties = f.readlines()

county_stats = {}

for i in range(len(counties)):
    
    name, population = counties[i].strip().split("\t ")

    county_stats[name] = int(population.replace(",",''))

# print all counties (keys), comma-seperated
print("The counties in Indiana area:")
print(", ".join(sorted(county_stats.keys())))
print()

# print monroe population
monroe = county_stats["Monroe"]
print("The population of 2015 Monroe County was:", monroe)

# state population is a sum
in_pop = sum(county_stats.values())
print("The total IN population as of 2015 was:", in_pop)

# percentage calculation
print("Monroe County accounts for", (monroe / in_pop * 100), \
      "% of IN's population.")
    
