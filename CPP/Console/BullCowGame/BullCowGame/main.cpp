/*
This is the console executable that makes use of the BullCow class.  It acts as the view in MVC Pattern 
and is responsible for all user interaction.  For game logic, see class.
*/

#include <iostream>
#include <string>
#include "FBullCowGame.h"
// #include "IsogramList.h"

using FText = std::string;
using int32 = int;

void PrintIntro();
void PrintAnswer();
void PlayGame();
void PrintResponse(FBullCowCount, FText);
FText GetValidGuess();
bool AskToPlayAgain();
FBullCowGame BCGame;


int32 main()
{
	PrintIntro();

	do
	{
		PlayGame();
	} while (AskToPlayAgain());

}
 
void PlayGame()
{
	BCGame.Reset();
	int32 guessLimit = BCGame.GetMaxTries();
	bool skipped = false;

	std::cout << "\nCan you guess the " << BCGame.GetHiddenWordLength() << " letter isogram I'm thinking of?\n\n";

	// Playing game
	for (int32 i = 0; i <= guessLimit; i++)
	{
		if (i != guessLimit) {
			if (!BCGame.isGameWon()) {

				FText Guess = GetValidGuess();

				if (Guess != "skip") {

					FBullCowCount BullCowCount = BCGame.SubmitGuess(Guess);

					PrintResponse(BullCowCount, Guess);

				}
				// Skipping
				else {
					
					i = guessLimit -1;
					BCGame.IncreaseSkips();
				}

			}
		}
		// Printing answer if failed
		else if (!BCGame.isGameWon()){
			PrintAnswer();
		}


	}
	// Increasing game counter
	BCGame.IncreaseGames();
	BCGame.PrintStats();
}

void PrintResponse(FBullCowCount BullCowCount, FText Guess)
{

	if (BullCowCount.Bulls == BCGame.GetHiddenWordLength())
	{
		std::cout << std::endl << Guess << " is the correct isogram.\nYou Win!\n\n";

		BCGame.SetGameWon();
	}
	else {
		std::cout << "\nBulls = " << BullCowCount.Bulls;
		std::cout << " Cows = " << BullCowCount.Cows << std::endl;
		std::cout << "(correct, wrong place)\n\n";
	}
}
// Loop until we get a valid guess
FText GetValidGuess() 
{

	bool ValidGuessNotGiven = true;
	do {

		// Player Input
		std::cout << "(#" << BCGame.GetCurrentTry() << ") Enter your guess: ";
		FText Guess = "";

		std::getline(std::cin, Guess);

		EGuessStatus Status = BCGame.CheckGuess(Guess);

		if (Guess == "skip") {
			std::cout << "Skipping...\n\n";
			return Guess;
		}
		else {

			switch (Status)
			{
			case EGuessStatus::Wrong_Length:
				std::cout << "\nINVALID INPUT: Please enter a word that is " << BCGame.GetHiddenWordLength() << " letters long.\n\n";
				break;
			case EGuessStatus::Not_Isogram:
				std::cout << "\nINVALID INPUT: Please enter an isogram (use letter only once).\n\n";
				break;
			default:
				ValidGuessNotGiven = false;
				return Guess;
			}
		}
	}
	while (ValidGuessNotGiven);
}

bool AskToPlayAgain()
{
	std::cout << "Do you want to play again? (y/n)";
	FText Response = "";
	std::getline(std::cin, Response);

	return (Response[0] == 'y') || (Response[0] == 'Y');
}

void PrintIntro() 
{
	// Intro
	std::cout << "Welcome to Bulls and Cows\n\n";

	return;
}

void PrintAnswer()
{
	std::cout << "The answer was " << BCGame.GetHiddenWord() << "\n\n";
	//BCGame.SetGameWon();
}

