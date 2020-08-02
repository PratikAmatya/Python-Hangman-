import random
continuation=True
while continuation==True:
	askingDifficultyLevel=True
	print("Hangman.Inc\n")
	print("Difficulty Levels:\nEasy\nMedium\nHard\n")
	randomWords=[]
	numberOfTries=0
	while askingDifficultyLevel==True:
		difficultyLevel=input("Please enter the difficulty level you want to play: ").lower()
		if difficultyLevel=="easy":
			randomWords=[["r","e","d"],["d","a","y"],["d","a","d"],["g","y","m"],["i","n","k"],["j","e","t"],["k","e","y"],["z","o","o"]]
			numberOfTries=20
			break
		elif difficultyLevel=="medium":
			randomWords=[["c","a","k","e"],["g","a","m","e"],["f","a","c","e"],["h","a","n","d"],["l","o","c","k"],["n","a","m","e"],["n","o","s","e"],["b","o","d","y"],["n","i","c","e"],["e","a","s","y"]]
			numberOfTries=20
			break
		elif difficultyLevel=="hard":
			randomWords=[["d","e","a","l","e","r"],["r","e","c","i","p","e"],["e","x","t","e","n","t"],["w","e","a","l","t","h"],["p","e","o","p","l","e"],["m","e","t","h","o","d"],["e","s","t","a","t","e"],["g","r","o","w","t","h"],["s","t","u","d","i","o"],["n","a","t","u","r","e"]]
			numberOfTries=24
			break	
		else:
			print("Please enter Easy, Medium or Hard only.\n")
	correctAnswer=random.choice(randomWords)
	lettersEnteredByUser=[]
	wrongLettersEnteredByUser=[]
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
						if numberOfCorrectLettersEntered<=len(correctAnswer):
							for i in range(0,len(correctAnswer)):
								if correctAnswer[i] in lettersEnteredByUser:
									print(correctAnswer[i],end=" ")
								else:
									print(" _ ",end =" ")
						print("\n")
						continue
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
							print("\n...You Loose...\n")
							print("The correct answer was:",end=" ")
							for i in correctAnswer:
								print(i,end="")
							print("\nBetter luck next time :)\n\n")
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
		
