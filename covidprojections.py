import time
import math

def ispositive(x):
	if (x.isdigit()):
		x = float(x)
		if (0 <= x):
			return True
		else:
			return False
	else:
		return False

def isvalidpercent(y):
	if (y.isdigit()):
		y = float(y)
		if ((0 <= y) and (y <= 100)):
			return True
		else:
			return False
	else:
		return False

def round(z):
	if ((float(math.ceil(float(z))) - z) >= (z - (float(math.floor(float(z)))))):
		return math.ceil(float(z))
	else:
		return math.floor(float(z))

def dothemath(s, i, r, ir, rr, d, sr, f):
	originaldays = d
	ir = float(ir) / 100.0
	sr = float(sr) / 100.0
	while (d != 0):
		s2 = float(s) - (float(ir) * (float(s) * float(i)))
		i2 = float(i) + ((float(ir) * (float(s) * float(i))) - (float(rr) * float(i)))
		r2 = float(r) + (float(rr) * float(i))
		d = float(d) - 1.0
		s = s2
		i = i2
		r = r2
		if (s <= 1.0):
			i = s + i
			s = 0
		if (i <= 1.0):
			r = r + i
			i = 0
	s = round(s)
	i = round(i)
	r = round(r)
	survivors = sr * r
	dead = r - survivors
	survivors = round(survivors)
	dead = round(dead)
	f = "In " + str(originaldays) + " days' time, " + str(s) + " people will still be susceptible, " + str(i) + " people will still be infected, " + str(survivors) + " people will have recovered, and " + str(dead) + " people will have died."
	return f
goagain = True
while (goagain == True):
	validinput1 = False
	validinput2 = False
	validinput3 = False
	validinput4 = False
	validinput5 = False
	validinput6 = False
	print ("This is a program designed to predict the spread of COVID-19")
	print ("in a fixed population.")
	time.sleep(0.5)
	print ("The model we used can be found here: https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model")
	time.sleep(0.5)
	while (validinput1 == False):
		suscepted = input ("How many people in the population are susceptible to the virus, i.e. they have not been infected yet?")
		if (ispositive(suscepted)):
			validinput1 = True
		else:
			print ("That is not a valid input. Please enter a whole number.")
	while (validinput2 == False):
		infected = input ("How many people in the population are currently infected?")
		if (ispositive(infected)):
			validinput2 = True
		else:
			print ("That is not a valid input. Please enter a whole number.")
	removed = 0
	print("By default, the people that have recovered from the virus is set to 0.")
	time.sleep(0.5)
	while (validinput3 == False):
		dailycontacts = input ("On average, how many susceptible people are infected every day?")
		if (ispositive(dailycontacts)):
			validinput3 = True
		else:
			print ("That is not a valid input. Please enter a whole number.")
	while (validinput4 == False):
		recoveryrate = input ("On average, how much of the infected population either dies or recovers from the virus every day, as a percentage?")
		if (isvalidpercent(recoveryrate)):
			validinput4 = True
		else:
			print ("That is not a valid input. Please enter a percent, and do not include the % symbol.")
	while (validinput5 == False):
		survivalrate = input ("What is the survival rate of the virus?")
		if (isvalidpercent(survivalrate)):
			validinput5 = True
		else:
			print ("That is not a valid input. Please enter a percent, and do not include the % symbol.")
	while (validinput6 == False):
		days = input ("How many days into the future would you like to travel?")
		if (ispositive(days)):
			days = int(days)
			validinput6 = True
		else:
			print ("That is not a valid input. Please enter a whole number.")
	print ("Calculating...")
	time.sleep(1)
	finalresult = ""
	print (dothemath(suscepted, infected, removed, dailycontacts, recoveryrate, days, survivalrate, finalresult))
	time.sleep(0.5)
	gacheck = input ("Would you like to modify your variables? (y/n)")
	sensical = False
	while (sensical == False):
		if ((gacheck == "y") or (gacheck == "Y")):
			print ("Okay!")
			sensical = True
			time.sleep(0.5)
		elif ((gacheck == "n") or (gacheck == "N")):
			print ("Okay.")
			sensical = True
			goagain = False
		else:
			print ("Sorry, I didn't understand that. Please type only y or n.")
