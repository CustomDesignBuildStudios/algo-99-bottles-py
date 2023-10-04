

def bottle_song(num_bottles):
	"""
	Returns a string with the # of bottles of beer on the wall song
	Arguments:
	num_bottles - int - Number of bottles the song should start with.
	"""
	bottle_song = ""
	orginial_bottles = num_bottles
	while num_bottles > 1:

		bottle_song += f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer. Take one down and pass it around, {num_bottles-1} {'bottles' if num_bottles > 2 else 'bottle' } of beer on the wall.\n"
		num_bottles = num_bottles -1

	bottle_song += f"Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {orginial_bottles} bottles of beer on the wall."

	return bottle_song



bottles_user_input = int(input("How many bottles do you want to start with?"))
print(bottle_song(bottles_user_input))
