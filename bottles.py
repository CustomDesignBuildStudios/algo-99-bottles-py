def bottle_song():
	user_input = int(input("How many bottles do you want to start with?"))
	count = user_input
	while count > 1:

		print(f"{count} bottles of beer on the wall, {count} bottles of beer. Take one down and pass it around, {count-1} {'bottles' if count > 2 else 'bottle' } of beer on the wall.")
		count = count -1

	print(f"Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {user_input} bottles of beer on the wall.")
	pass

bottle_song()
