#pragma once
#include <string>

using FString = std::string;
using int32 = int;

// All are initialized to 0
struct FBullCowCount
{
	int32 Bulls = 0;
	int32 Cows = 0;
};

enum EGuessStatus {
	OK,
	Not_Isogram,
	Wrong_Length
};


class FBullCowGame {
public:
	FBullCowGame(); // Construction
	void Reset();  // Set return val
	void SetGameWon();
	void IncreaseSkips();
	void IncreaseGames();
	void PrintStats();
	FString GetHiddenWord();
	int32 GetMaxTries() const;
	int32 GetCurrentTry() const;
	int32 GetHiddenWordLength() const;
	int32 RandomInt(int32);
	

	bool isGameWon() const;
	bool isIsogram(FString);
	bool CheckLength(FString);
	EGuessStatus CheckGuess(FString);

	FString MakeLower(FString);
	FBullCowCount SubmitGuess(FString);

private:
	int32 MyMaxTries;
	int32 MyCurrentTry;
	FString MyHiddenWord;
	int32 MyWins;
	int32 MySkips;
	int32 MyGames;
	int32 MyPoints;
	bool MyGameIsWon;
	int32 MyDifficulty;


};