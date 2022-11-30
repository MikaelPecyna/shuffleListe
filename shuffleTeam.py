import sys, random


def suffleTeam(file):
	with open(file,'r') as t:

	    lines = t.readlines()
	    lines = lines[2:]
	    ListeNameAndSurname = []
	    lines = lines[::-1]


	    for line in lines:
	    	name = line.split(";")
	    	nameAndSurname = name[2].replace('\"', '').upper() + " " + name[3].replace('\"', '').capitalize()
	    	ListeNameAndSurname.append(nameAndSurname)
	    
	    

	    random.shuffle(ListeNameAndSurname)
	    team = 0
	    nb = 6
	    
	    for i, name  in enumerate(ListeNameAndSurname):
	    	
	    	if i%nb==0:
	    		team += 1
	    		print("\033[0;31m" + "---------------------------------------------")
	    		print("      " + "Equipe n°: "  + str(team))
	    		print("---------------------------------------------" + "\033[00m")

	    	if team%2 == 1:

	    		print("[" + str(i+1) + "] " + "\033[00m"  + name)
	    	else: 
	    		print("\033[0;35m"  + "[" + str(i+1) + "] " + name )
	    	
	    	if team > 5:
	    		nb = 5







suffleTeam(sys.argv[1])