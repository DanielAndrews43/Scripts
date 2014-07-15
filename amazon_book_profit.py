#all costs are in dollars, and all times are in decimal-minutes

shipping_cost = 2.68 #media mail 9" x 11"
container_cost = 0.40 #b-flute method
paid_shipping = 3.99
time_to_list_item = 2.00 #take book, make sure pic is good, put cost, put in stack
time_to_find_item = 0.50 #find item after it was sold
time_to_package_item = 3.00 #b-flute method (food wrap -> cardboard -> tape -> staple -> write address)
percent_books_sold = 0.5 #assume 50% of books wont be bought due to competition
average_book_price = 0.99 #hardcovers sell for quite a bit, while most paperbacks are cheap
minutes = 60.00


def profit_per_book():
	return average_book_price + paid_shipping - shipping_cost - container_cost


def operations_per_hour():
	return minutes / (time_to_list_item + time_to_ship_item())


def time_to_ship_item():
	#You only need to package books that are sold
	return percent_books_sold * (time_to_list_item + time_to_find_item)


def profit():
	wage = operations_per_hour() * profit_per_book()
	return "In {0} minutes you make {1}".format(minutes, wage)


print profit()