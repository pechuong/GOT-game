#upload text file for storage
#ranking system, locked cities, locked inventory
#locked cities
#locked inventory
#input validation so it doesnt crash

def welcome_note(current_city, name):
	print("\n   *** Welcome to Game of Thrones Trader. Let's begin. ***")
	print("              *** Hello,", name,"! ***")
	print("         *** You are currently in", current_city," ***\n")
def main_menu():
	print("Main Menu\n1. Trade\n2. Travel\n3. Show Rank\n4. Exit Game\n")
def travel_menu(city_list,city_travel_cost):
	print("   *** Travel Menu ***")
	for i in range(len(city_list)):
		print(i+1,".", city_list[i],"................",city_travel_cost[i]," Gold")

def price_menu(city_list,current_city,item_list,item_prices):
	index=city_list.index(current_city)
	print("\n      *** PRICES in ",current_city," *** ")
	for i in range(len(item_list)):
		print("   ", i+1,".",item_list[i]," ",item_prices[index][i])

def trade_menu():
	print("\n  Trade Menu \n1. Buy\n2. Sell\n3. Exit Shop\n")
def print_inventory(inventory_list,inventory_amount):
	print("\n   ***   Inventory   *** ")
	for i in range(0,6):
		print("   ",i+1,".",inventory_list[i],":" ,inventory_amount[i])
	print("\n   *** You have ",inventory_amount[6]," cash ***")
def price_changer(item_prices,item_volatility):
	import random
	
	new_price_list=[]
	for i in item_prices:
		new_unit=[]
		for b in range(len(i)):
			random_sum=random.randint(-item_volatility[b],item_volatility[b])
			new_unit.append(i[b]+random_sum)
		
		new_price_list.append(new_unit)
	return(new_price_list)

def check_rank(inventory_amount):
	gold=int(inventory_amount[6])
	ranks=[1000,5000,10000,25000,50000,100000,500000,1000000]
	if gold<ranks[0]:
		print("   *****  Level 1: Apprentice  *****")
	elif gold>ranks[0] and gold<ranks[1]:
		print("   *****  Level 2: Crow  *****")
	elif gold>ranks[1] and gold<ranks[2]:
		print("   *****  Level 3: Hodor  *****")
	elif gold>ranks[2] and gold<ranks[3]:
		print("   *****  Level 4: Tyrion *****")
	elif gold>ranks[3] and gold<ranks[4]:
		print("   *****  Level 5: Stanis  *****")
	elif gold>ranks[4] and gold<ranks[5]:
		print("   *****  Level 6: Ned Stark *****")
	elif gold>ranks[5] and gold<ranks[6]:
		print("   *****  Level 7: John Snow *****")
	elif gold>ranks[6] and gold<ranks[7]:
		print("   *****  Level 8: King of Quarth *****")
	elif gold>ranks[7]:
		print("   *****  Level 9: Mother of Dragons *****")

def main():
	#opens saved games
	infile=open("saved1.txt","r")
	contents=infile.readlines()
	
	#updates name, current city, inventory
	inventory_amount=[]
	for aline in contents:
		line=aline.split(".")
		name=line[0]
		current_city=line[1]
		inventory_amount_1=int(line[2])
		inventory_amount.append(inventory_amount_1)
		
		inventory_amount_2=int(line[3])
		inventory_amount.append(inventory_amount_2)
		
		inventory_amount_3=int(line[4])
		inventory_amount.append(inventory_amount_3)	

		inventory_amount_4=int(line[5])
		inventory_amount.append(inventory_amount_4)

		inventory_amount_5=int(line[6])
		inventory_amount.append(int(inventory_amount_5))

		inventory_amount_6=int(line[7])
		inventory_amount.append(inventory_amount_6)

		inventory_amount_7=int(line[8])
		inventory_amount.append(inventory_amount_7)
	
	#cities and cost of travel
	city_list=["Bravos","Westeros","Dorn","Valantis","King's Landing","Yunkai"]
	city_travel_cost=[5,5,10,50,1000,5000]

	item_list=["Goats","Fish","Barrels of wine","Swords","Unsullied","Dragons"]
	item_prices=[[50,10,30,100,5000,100000],[50,10,30,100,5000,100000],[50,10,30,100,5000,100000],[50,10,30,100,5000,100000],[45,10,30,105,5000,100000],[53,10,35,105,5000,100000]]
	item_volatility=[10,6,20,30,1000,10000]
	#current_city=city_list[0]
	inventory_list=["Goats","Fish","Barrels of wine","Swords","Unsullied","Dragons","Gold"]
	#inventory_amount=[0,0,0,0,0,0,50]
	item_prices_2=item_prices
	

	welcome_note(current_city,name)
	main_menu()
	menu_input=input("What would you like to do? ")
	
	#input validation for main menu
	while menu_input!="1" and menu_input!="2" and menu_input!="3" and menu_input!="4":
		print("\n *** ERROR *** : Please enter valid input")
		main_menu()
		menu_input=input("What would you like to do? ")

	while menu_input!="4":
		#trading options
		if menu_input=="1":
			price_menu(city_list,current_city,item_list,item_prices_2)
			print_inventory(inventory_list,inventory_amount)
			trade_menu()
			trade_input=input("What would you like to do? ")

			#trade input validation
			while trade_input!="1" and trade_input!="2" and trade_input!="3":
				print("\n *** ERROR *** : Please enter valid input")
				trade_menu()
				trade_input=input("What would you like to do? ")


			while trade_input!="3":

				#buying options
				if trade_input=="1":
					item_choice=input("What would you like to buy?: ")
					#item choice validation
					while item_choice!="1" and item_choice!="2" and item_choice!="3" and item_choice!="4" and item_choice!="5" and item_choice!="6":
						print("\n *** ERROR *** : Please enter valid input")
						item_choice=input("What would you like to buy?: ")

					#still needs validation
					item_quantity=int(input("How many do you want to buy?: "))

					#buy verify
					item_cost=item_prices_2[city_list.index(current_city)][int(item_choice)-1]
					total_cost=item_quantity*item_cost
					
					if total_cost>int(inventory_amount[6]):
						print("You cannot afford!!! ")
					else:
						inventory_amount[int(item_choice)-1]=inventory_amount[int(item_choice)-1]+item_quantity
						inventory_amount[6]=inventory_amount[6]-total_cost
				#selling options
				if trade_input=="2":
					item_choice=input("What would you like to sell?: ")
					#item choice validation
					while item_choice!="1" and item_choice!="2" and item_choice!="3" and item_choice!="4" and item_choice!="5" and item_choice!="6":
						print("\n *** ERROR *** : Please enter valid input")
						item_choice=input("What would you like to sell?: ")
					
					item_quantity=int(input("How many do you want to sell?: "))

					#sell verify
					item_cost=item_prices_2[city_list.index(current_city)][int(item_choice)-1]
					total_cost=item_quantity*item_cost
					
					if item_quantity>inventory_amount[int(item_choice)-1]:
						print("\n *** You do not have enough to sell ***")
					else:
						inventory_amount[int(item_choice)-1]=inventory_amount[int(item_choice)-1]-item_quantity
						inventory_amount[6]=inventory_amount[6]+total_cost

				price_menu(city_list,current_city,item_list,item_prices_2)
				print_inventory(inventory_list,inventory_amount)
				trade_menu()
				trade_input=input("What would you like to do?: ")

				#trade input validation 2
				while trade_input!="1" and trade_input!="2" and trade_input!="3":
					print("\n *** ERROR *** : Please enter valid input")
					trade_menu()
					trade_input=input("What would you like to do? ")

			#exit shop
			if trade_input=="3":
				print("Leaving Shop...")
		
		#traveling options
		#changes prices on each travel
		if menu_input=="2":
			travel_menu(city_list,city_travel_cost)
			travel_select=input("Where would you like to travel?: ")

			#travel menu validation
			while travel_select!="1" and travel_select!="2" and travel_select!="3" and travel_select!="4" and travel_select!="5" and travel_select!="6":
				print("\n *** ERROR *** : Please enter valid input")
				travel_menu(city_list,city_travel_cost)
				travel_select=input("Where would you like to travel?: ")

			#price check for travel
			travel_cost=city_travel_cost[int(travel_select)-1]
			if travel_cost>int(inventory_amount[6]):
						print("\n ** You do not have enough gold **")

			#travel, changes prices
			else:
				current_city=city_list[int(travel_select)-1]
				inventory_amount[6]=inventory_amount[6]-travel_cost
				print("   *** Traveling to ",current_city,"***")
				item_prices_2=price_changer(item_prices,item_volatility)

		#show unlockables
		if menu_input=="3":
			check_rank(inventory_amount)
		
		main_menu()
		menu_input=input("What would you like to do? ")
		#input validation for main menu 2
		while menu_input!="1" and menu_input!="2" and menu_input!="3" and menu_input!="4":
			print("\n *** ERROR *** : Please enter valid input")
			main_menu()
			menu_input=input("What would you like to do? ")


	#exit game, write out text file
	if menu_input=="4":
		print("\n *** Saving Game ***")
		outfile=open("saved2.txt","w")
		new_string=""
		new_string=new_string+name+"."+current_city
		for i in inventory_amount:
			new_string+="."
			new_string+=str(i)
		outfile.write(new_string)
		outfile.close()
		infile.close()

main()