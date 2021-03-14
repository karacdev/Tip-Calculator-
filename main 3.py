
print('Welcome to the TIP Calculator')

total_Bill=float(input("What is the total of the bill? "))

split_Bill=int(input("How many people are splitting the bill? "))

tip_Percent=int(input("What percentage tip would you like to tip 12, 15, 18 ? "))

percent=tip_Percent/100

ind_Bill=((percent * total_Bill) + total_Bill)

total_Due=(ind_Bill/split_Bill)

amount_Due=print(f"Each person has to pay ${total_Due}")
