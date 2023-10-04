

def bottle_song_loop(num_bottles):
	"""
	Returns a string with the # of bottles of beer on the wall song using a while loop
	Arguments:
	num_bottles - int - Number of bottles the song should start with.
	"""
	bottle_song = ""
	orginial_bottles = num_bottles
	while num_bottles > 0:

		bottle_song += f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer. Take one down and pass it around, {num_bottles-1} {'bottles' if num_bottles > 2 else 'bottle' } of beer on the wall.\n"
		num_bottles = num_bottles -1

	bottle_song += f"Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {orginial_bottles} bottles of beer on the wall."

	return bottle_song

def bottle_song_func_loop(bottle_song, orginial_bottles, current_bottles):
	"""
	Returns a string with the # of bottles of beer on the wall song using function calls
	Arguments:
	battle_song  - string - The song we have so far. Function keeps adding to string until num_bottles is zero.
	num_bottles  - int    - Number of bottles the song is currently on.
	"""
	if current_bottles > 0:
		bottle_song += f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer. Take one down and pass it around, {current_bottles-1} {'bottles' if current_bottles > 2 else 'bottle' } of beer on the wall.\n"
		current_bottles -= 1

		return bottle_song_func_loop(bottle_song, orginial_bottles, current_bottles)
	else:
		bottle_song += f"Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {orginial_bottles} bottles of beer on the wall."
		return bottle_song
	





bottles_user_input = int(input("How many bottles do you want to start with?"))
print(bottle_song_loop(bottles_user_input))


bottles_user_input = int(input("How many bottles do you want to start with?"))
print(bottle_song_func_loop("",bottles_user_input,bottles_user_input))