/*
Program which allows the user to input a number from 2 to 30 and generates
a random string of N length. If string has characters of frequency > 1, will
display the count of said repeated character/s.

TODO - Find a way to ensure every character in the generated string has normalized
frequency
*/

#include "common_includes.h"
#include <unordered_map>

inline int genRandChar();
std::string createStr(int);
void checkInput(int&);
void determineOccurences(const std::string&);

constexpr int L_ALPHA_START{ 97 }, RANGE_END{ 26 }, MAX_ALLOWED{ 30 },
MIN_NEEDED{ 2 };

std::unordered_map<char, int> M;

int main() {

    srand(static_cast<unsigned>(time(0)));
    char goAgain;
    int num;


    do
    {
        std::cout << "Enter an integer and I will generate a random string\n"
            << "of 'N' letters => ";
        checkInput(num);
        std::string randStr = createStr(num);

        std::cout << "\nRandom string is: " << randStr << std::endl;
        if (!(M.empty())) {
            std::cout << "REPEATED OCCURRENCES OF LETTERS:\n";
            for (auto& k : M)
            {
                std::cout << "'" << k.first << "'" << " -> " << k.second
                    << std::endl;
            }
        }
        std::cout << "\nGenerate a new string? ['Y' 'N']? "; std::cin >> goAgain;
        system("cls"); // Clear console
    } while (tolower(goAgain) == 'y');

    return 0;
}


void checkInput(int& num) {

    while (!(std::cin >> num) || (num > MAX_ALLOWED || num < MIN_NEEDED))
    {
        std::cin.clear();
        ignoreExtraneous();
        std::cout << "ERROR! Please keep string between " << MIN_NEEDED <<
            " and " << MAX_ALLOWED << " characters.\n=> ";
    }
}


inline int genRandChar() {

    return L_ALPHA_START + (rand() % RANGE_END); // Offset 97 ('a'), range end
    // 1 + 'z'
}


std::string createStr(int N) {

    std::string str;

    for (int i = 0; i < N; i++)
    {
        char letter = static_cast<char>(genRandChar()); // Covert returned int
        str += letter;
    }

    std::sort(str.begin(), str.end());
    determineOccurences(str);
    return str;
}


void determineOccurences(const std::string& str) {

    M.clear(); // global, so need to reset each time the user re-runs prog

    for (int i = 0; i < str.length(); i++)
    {

        if (std::count(str.begin(), str.end(), str[i]) > 1) {

            M[str[i]]++; // Add count to map index of repeated letter
        }
    }

}
