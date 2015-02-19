text = input ("Enter word:  ")

if (text.find("hello") != -1) or ((text.find("Hello") != -1)):
    print("Hello there, good stranger!")
elif (text.find("how are you") != -1 or (text.find("How are you") != -1)):
    print("I am fine, thanks. How are you?")
elif (text.find("feelings") != -1):
    print ("I am a machine. I have no feelings")
elif (text.find("age") != -1):
    print ("I have no age. Only current timestamp")
else:
    print("huh, what? does... not... compute")
    
