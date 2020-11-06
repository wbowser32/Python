prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\n\nWhat is your first name? "
name =  input(prompt)
age=input("How old are you? ")
age=int(age)
height=input("How tall are you, in inches? ")
height = int(height)
height= height / 12
if height >= 3:
	print("\n\nYou are tall enough to ride this ride, "+name+". You are "+str(age)+" after all")
else:
	print("\n\nYou are not tall enough, "+name+". You are only "+str(age)+". come back in a few years.")