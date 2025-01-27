#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

//Global vars
const int MAX_INCORRECT = 6; //wrong guesses
char incorrect[MAX_INCORRECT];
int numIncorrect = 0;
int misses = 0;

void displayHangman() {
    cout << "\n";
    switch (misses) {
        case 0:
            cout << "  +---+\n";
            cout << "  |   |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "==========\n";
            break;
        case 1:
            cout << "  +---+\n";
            cout << "  |   |\n";
            cout << "  O   |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "==========\n";
        case 2:
            cout << "  +---+\n";
            cout << "  |   |\n";
            cout << "  O   |\n";
            cout << "  |   |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "==========\n";
        case 3:
            cout << "  +---+\n";
            cout << "  |   |\n";
            cout << "  O   |\n";
            cout << "  |]  |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "==========\n";
        case 4:
            cout << "  +---+\n";
            cout << "  |   |\n";
            cout << "  O   |\n";
            cout << " /|]  |\n";
            cout << "      |\n";
            cout << "      |\n";
            cout << "==========\n";
    }
}

void display(string guessedWord) {
    cout << "\n Word: ";
    for (int i = 0; i < guessedWord.length(); i++){
        cout << guessedWord[i] << ' ';
    }
    cout << "\n Incorrect guesses: ";
    for (int i = 0; i < MAX_INCORRECT; i++){
        cout << incorrect[i] << ' ';
    }
    cout << "\n Misses left : " << MAX_INCORRECT - misses << "\n";
    displayHangman();
}

string processGuess(char guess, string word, string guessedWord) {
    bool isCorrect = false;
    char potato;
    cout<<"word length is"<<word.length()<<endl;
    cin>>potato;
    for (int i = 0; 1 < word.length(); i++) {
        cout<<word[i]<<endl<<guess<<endl<<guessedWord[i]<<endl;
        if (word[i] == guess && guessedWord[i] == '_') { //segfault here
            guessedWord[i] = guess;
            isCorrect = true; 
        }
    }

    if (!isCorrect) {
        bool alreadyGuessed = false;

        for (int i = 0; i < numIncorrect; i++) {
            if (incorrect[i] == guess) {
                alreadyGuessed = true;
                break;
            }
        }

        if (!alreadyGuessed) {
            incorrect[numIncorrect++] = guess;
            misses++;
        }
    }
    return guessedWord;
}

int main() {
    //string wordList[] = { "windowkill", "minecraft", "stardew", "valley", "programming", "game", "developer" };
    string wordList[] = {  "snuffalupagus"};
    srand(time(0));
    string word = wordList[rand() % 5];
    string guessedWord(word.length(), '_');

    cout << "Welcome to Hangman\n";

    while (misses < MAX_INCORRECT && guessedWord != word) {
        display(guessedWord);
        cout << "Enter guess: ";
        char guess;
        cin >> guess;

        string oldGuessedWord = guessedWord;
        guessedWord = processGuess(guess, word, guessedWord);

        if (guessedWord == oldGuessedWord) {
            cout << "nah\n";
        } else {
            cout << "yea\n";
        }
    }

    if (guessedWord == word) {
        cout << "yorue did it!!1!!11one!!11\n it was: " << word << "\n";
    } else {
        cout << "nah you kinda suck, it was\n" << word << "\n";
    }
    return 0;
}