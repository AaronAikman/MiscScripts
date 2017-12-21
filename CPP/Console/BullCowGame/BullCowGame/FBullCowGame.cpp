#include <iostream> //TEMP
#include <random>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include "FBullCowGame.h"
#include "IsogramList.h"

int32 FBullCowGame::GetMaxTries() const { return MyMaxTries; }
int32 FBullCowGame::GetCurrentTry() const { return MyCurrentTry; }
int32 FBullCowGame::GetHiddenWordLength() const { return MyHiddenWord.length(); }

int32 FBullCowGame::RandomInt(int32 maxLimit)
{

	rand();
	int random, max_value = maxLimit, min_value = 0;
	random = rand() % max_value + min_value;
	return random;

}


FBullCowGame::FBullCowGame()
{
	FBullCowGame::Reset();
	MyWins = 0;
	MyPoints = 0;
	MySkips = 0;
	MyGames = 0;
	MyDifficulty = 3;
}

void FBullCowGame::Reset()
{
	constexpr int32 MAX_TRIES = 50;
	const FString HIDDEN_WORD = GetHiddenWord();

	MyMaxTries = MAX_TRIES;

	MyCurrentTry = 1;

	MyHiddenWord = HIDDEN_WORD;


	MyGameIsWon = false;

}

void FBullCowGame::SetGameWon()
{
	MyGameIsWon = true;
	MyWins++;
	MyPoints += (GetHiddenWordLength() * (MyMaxTries - MyCurrentTry + 1));
	MyDifficulty++;
}

void FBullCowGame::IncreaseSkips()
{
	MySkips++;
}

void FBullCowGame::IncreaseGames()
{
	MyGames++;
}

void FBullCowGame::PrintStats()
{
	std::cout << "Wins: " << MyWins << "  Points: " << MyPoints << "  Games: " << MyGames << "  Skips: " << MySkips << std::endl;
}

FString FBullCowGame::GetHiddenWord()
{
	/*FString arr[] = Isograms[];
	int size = *(&arr + 1) - arr;
	int32 randomIndex = RandomInt(size);
	return Isograms[randomIndex];*/
	FString foundWord = "";
	srand(time(NULL)); //initialize the random seed
	do {


		int RandIndex = rand() % 1908; //generates a random number between 0 and 1907
		foundWord =  Isograms[RandIndex];
	} while (foundWord.length() != MyDifficulty);
	return foundWord;

}



bool FBullCowGame::isGameWon() const
{

	return MyGameIsWon;
}

// checks if string arg is an isogram
bool FBullCowGame::isIsogram(FString str)
{


	int len = str.length();

	// Convert the string in lower case letters
	for (int i = 0; i<len; i++)
		str[i] = tolower(str[i]);

	std::sort(str.begin(), str.end());


	for (int i = 0; i < len; i++)
	{
		if (str[i] == str[i + 1])
			
			return false;
	}
	return true;


}

bool FBullCowGame::CheckLength(FString Guess)
{
	return Guess.length() == FBullCowGame::GetHiddenWordLength();
}

EGuessStatus FBullCowGame::CheckGuess(FString Guess)
{
	// if wrong length
	if (!FBullCowGame::CheckLength(Guess)) {
		return EGuessStatus::Wrong_Length;
	// if not iso
	} else if (!FBullCowGame::isIsogram(Guess)) {
		return EGuessStatus::Not_Isogram;
	} else {
		return EGuessStatus::OK;
	}

}

FString FBullCowGame::MakeLower(FString str)
{
	for (int32 i = 0; i <= str.length(); i++)
	{
		if (str[i] >= 97 && str[i] <= 122)
		{
			str[i] = str[i] - 32;
		}
	}
	return str;
}

// receives a VALID guess, increments turn, and retuns count
FBullCowCount FBullCowGame::SubmitGuess(FString Guess)
{
	FString lowerGuess = FBullCowGame::MakeLower(Guess);

	// increment the turn
	MyCurrentTry++;

	// setup a  return var
	FBullCowCount BullCowCount;

	// loop all letters in guess
	int32 HiddenWordLength = MyHiddenWord.length();

	for (int32 i = 0; i < HiddenWordLength; i++) {
		//compare letters against a hidden word
		for (int32 j = 0; j < HiddenWordLength; j++) {
			// if they match
			if (Guess[i] == MyHiddenWord[j]){
				// if they're in the same place
				if (j == i){
					// increment bulls if they're in the same place
					BullCowCount.Bulls++;
				} else {
					// increment cows if not
					BullCowCount.Cows++;
				}
			}
		}
	}

	return BullCowCount;
}
