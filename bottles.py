

def bottle_song_loop(num_bottles):
	"""
	Returns a string with the # of bottles of beer on the wall song using a while loop
	Arguments:
	num_bottles - int - Number of bottles the song should start with.
	"""
	bottle_song = ""
	orginial_bottles = num_bottles
	while num_bottles > 0:

		bottle_song += f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer. Take one down and pass it around, {num_bottles-1 if num_bottles > 1 else 'No more'} {'bottles' if num_bottles > 2 else 'bottle' } of beer on the wall.\n"
		num_bottles = num_bottles -1

	bottle_song += f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {orginial_bottles} bottles of beer on the wall."

	return bottle_song

def bottle_song_func_loop(bottle_song, orginial_bottles, current_bottles):
	"""
	Returns a string with the # of bottles of beer on the wall song using function calls
	Arguments:
	battle_song  - string - The song we have so far. Function keeps adding to string until num_bottles is zero.
	num_bottles  - int    - Number of bottles the song is currently on.
	"""
	if current_bottles > 0:
		bottle_song += f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer. Take one down and pass it around, {current_bottles-1 if current_bottles > 1 else 'No more'} {'bottles' if current_bottles > 2 else 'bottle' } of beer on the wall.\n"
		current_bottles -= 1

		return bottle_song_func_loop(bottle_song, orginial_bottles, current_bottles)
	else:
		bottle_song += f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {orginial_bottles} bottles of beer on the wall."
		return bottle_song
	


print("Menu\n1 - Create song with loop\n2 - Create song with function recursion")
user_input = int(input("Which method do you want to use?"))

if user_input == 1:
	bottles_user_input = int(input("How many bottles do you want to start with?"))
	print(bottle_song_loop(bottles_user_input))
elif user_input == 2:
	bottles_user_input = int(input("How many bottles do you want to start with?"))
	print(bottle_song_func_loop("",bottles_user_input,bottles_user_input))
else:
	print("Incorrect Input")