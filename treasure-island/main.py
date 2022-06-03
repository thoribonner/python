print('''
******************************************************
 ^ /|\/|\  ^      ___I_     /|\ ^   ^ /|\/|\ /|\/|\\
/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\\
******************************************************\n
''')
print("Welcome to Camp Terrestrial.")
print('''
Your mission....................
...should you accept............
......is to survive the night...
''')

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
go = '''
  ___     _     __  __   ___      ___   __   __  ___   ___ 
 / __|   /_\   |  \/  | | __|    / _ \  \ \ / / | __| | _ \\
| (_ |  / _ \  | |\/| | | _|    | (_) |  \ V /  | _|  |   /
 \___| /_/ \_\ |_|  |_| |___|    \___/    \_/   |___| |_|_\\    
'''

aliens = '''
************************************************************
 	            .-""""-.       .-""""-.
 	           /        \     /        \\
	          /_        _\   /_        _\\
	         // \      / \\\ // \      / \\\\
	         |\__\    /__/| |\__\    /__/|
	          \    ||    /   \    ||    /
	           \        /     \        /
	            \  __  /       \  __  /
	    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
	   /        \ |  |/        \ |  |/        \\
	  /_        _\|  /_        _\|  /_        _\\
	 // \      / \\\ // \      / \\\ // \      / \\\\
	 |\__\    /__/| |\__\    /__/| |\__\    /__/|
	  \    ||    /   \    ||    /   \    ||    /
	   \        /     \        /     \        /
	    \  __  /       \  __  /       \  __  /
	     '.__.'         '.__.'         '.__.'
	      |  |           |  |           |  |
	      |  |           |  |           |  |
  ___     _     __  __   ___      ___   __   __  ___   ___ 
 / __|   /_\   |  \/  | | __|    / _ \  \ \ / / | __| | _ \\
| (_ |  / _ \  | |\/| | | _|    | (_) |  \ V /  | _|  |   /
 \___| /_/ \_\ |_|  |_| |___|    \___/    \_/   |___| |_|_\\                                                         
************************************************************
				'''

sign = '''
   ___     _     ___   ___   _  _     _   ____
  / __|   /_\   | _ ) |_ _| | \| |   / | |__ /
 | (__   / _ \  | _ \  | |  | .` |   | |  |_ \\
  \___| /_/ \_\ |___/ |___| |_|\_|   |_| |___/                                              
         __  __
         \ \ \ \            |\ |\ |\\
          \ \ \ \           | \| \| \\
           \ \-\ \----------|  \  \  \\
           / /-/ /----------|  /  /  /
          / / / /           | /| /| /
         /_/ /_/            |/ |/ |/                                     
'''
win = '''
************************************************************
************************************************************
************************************************************
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\\
 .  :    .     . _ :::/:               .  ^ .  . .:\\
  .. . .   . - : :.:./.                        .  .:\\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\\
 __   __   ___    _   _    __      __  ___   _  _ 
 \ \ / /  / _ \  | | | |   \ \    / / |_ _| | \| |
  \ V /  | (_) | | |_| |    \ \/\/ /   | |  | .` |
   |_|    \___/   \___/      \_/\_/   |___| |_|\_|
************************************************************
************************************************************
************************************************************                                                  
'''

brave = input("Do you have what it takes?\nyes or no? ").lower()
if (brave == "y") or (brave == "yes") or (brave == "ya") or (brave == "sure") or (brave == "yeah") or (brave == "hell ya") or (brave == "fuck ya") or (brave == "hell yeah") or (brave == "fuck yeah") or (brave == "damn right"):
	print("\nVery well then. Your cabin is number 13 just over there. Enjoy your vist.\n")
	left_or_right = input("You've come to a split in the path. Which way would you like to go?\nleft or right? ").lower()
	if (left_or_right == "left") or (left_or_right == "l"):
		print("\nYou approach a sign.")
		read_sign = input("Read it or keep going?\n").lower()
		if read_sign == "read" or read_sign == "read it":
			print(sign)
			follow_sign = input("Do you follow the sign's directions?\nyes or no? ").lower()
			if (follow_sign == "yes") or (follow_sign == "y"):
				print(aliens)
				print("\nYou have wandered into forbidden territory and have been abducted.")
			else:
				print("\nYou see your cabin in the distance.")
				path_or_field = input("\nDo you stay on the path or go through the field?\npath or field? ").lower()
				if (path_or_field == "path") or (path_or_field == "p"):
					print("\nYou have fallen into a sinkhole.")
					print(go)
				else:
					print(win)
		else:
			print("\nYou see your cabin in the distance.")
			path_or_field = input("\nDo you stay on the path or go through the field?\npath or field? ").lower()
			if (path_or_field == "path") or (path_or_field == "p"):
				print("\nYou have fallen into a sinkhole.")
				print(go)
			else:
				print(win)
	else:
		print(win)
		print("\nYou've made it to your cabin early and found aliens doing strange things.\nTo keep you quiet they've given you a large treasure.")
else:
	print(aliens)
	print("You've insulted the aliens and have been abducted.")