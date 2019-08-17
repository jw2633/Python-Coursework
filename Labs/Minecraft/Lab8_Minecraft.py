import random
import minecraft

def dig(mine):
	materials_found = {}
	
	# part 2
	try:
		how_deep = eval(input("How deep would you like to dig? "))
		if (how_deep < 10) or (how_deep > 100):
			print("Please choose a depth between 10 and 100.")
			return {}
	except NameError:
		print("Try again. You did not enter a number.")
		return {}

	else:
		for i in range(how_deep):
			try:
				item = mine[i].strip()
			except IndexError:
				print("\nYOU HIT LAVA!")
				print("All of your materials were destroyed.")
				print("You died.")
				return {}
			else:
				print("You found", item + "!")
				if item in materials_found:
					materials_found[item] += 1
				else:
					materials_found[item] = 1

	return(materials_found)

## main
# part 1
try:
	file = open("mining_list.txt", "r")
	materials = file.readlines()
	file.close()
except:
	print("Materials not found.")
else:
	print("Materials found.")

my_mine = minecraft.create_mine(materials)

#part 2
minerals = dig(my_mine)


# part 3
if minerals:
	if "gold" in minerals or "obsidian" in minerals or "diamond" in minerals:
		if "gold" in minerals:
			print("Eureka, you found", minerals["gold"], "gold!")

		if "obsidian" in minerals:
			print("YES! You found the rarest mineral, obsidian!")

		if "diamond" in minerals:
			print("Excellent, you found", minerals["diamond"], "diamonds!")
	else:
		print("You found nothing of great value.")


                                      
