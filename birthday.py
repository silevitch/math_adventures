import random

tries = 100000
matches = 0

for x in range(tries):
	birthdays = {}
	for x in range(23):
		day = random.randint(1,365)
		if day in birthdays:
			matches = matches + 1
			break
		else:	
			birthdays[random.randint(1,365)] = 1


print matches
