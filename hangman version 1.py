import random
randomWords=[["p","i","g"],["b","a","l","l"],["h","e","r","o"],["c","a","t"],["n","e","t"]]
continuation=True
while continuation==True:
	correctAnswer=random.choice(randomWords)
	lettersEnteredByUser=[]
	wrongLettersEnteredByUser=[]
	numberOfTries=10
	numberOfCorrectLettersEntered=0
	print("Hangman.Inc\n")
	for value in correctAnswer:
		print(" _ ",end ="")
	print("\n")
	while numberOfTries>=1:
		userInput=input("\nEnter a letter: ")
		if len(userInput)>1:
			print("Enter a letter only\n")
		else:
			correctLetterEntered=False
			if userInput not in lettersEnteredByUser:
				for letter in correctAnswer:
					if letter == userInput:
						lettersEnteredByUser.append(letter)
						numberOfCorrectLettersEntered=numberOfCorrectLettersEntered+1
						correctLetterEntered=True
						print("Correct Letter entered\n")
						for i in range(0,len(correctAnswer)):
							if correctAnswer[i] in lettersEnteredByUser:
								print(correctAnswer[i],end=" ")
							else:
								print(" _ ",end =" ")
						print("\n")
			else:
				print("You have already entered the word")
				continue
			if numberOfCorrectLettersEntered < len(correctAnswer):
				if correctLetterEntered == False:	
					if userInput==" " or userInput=="":
						print("No letter detected. Please enter a letter.")
					elif userInput not in wrongLettersEnteredByUser:
						wrongLettersEnteredByUser.append(userInput)
						numberOfTries=numberOfTries-1
						if numberOfTries != 0:
							print("The entered letter is not found in the correct answer.\n Number of tries left:",numberOfTries)
						else:
							print("\n...You Loose...")
							str1=""
							print ("The correct word was",str1.join(correctAnswer))
							break
					
					else:
						print("You have already entered the letter. Please try a different letter.\n")
			else:
				print("!!! You Won !!!\n")
				break
				
	userTermination=False
	while userTermination==False:
		askingContinuation=input("Do you want to play again? (Y/N) ").lower()
		if askingContinuation=="n" or askingContinuation=="no" :
			print("\n------------Thank You------------")
			print("--------(c) Pratik Amatya--------")
			continuation=False
			break
		elif askingContinuation == "y" or askingContinuation == "yes":
			break
		else:
			print("Please enter Y or N only.\n")
		
