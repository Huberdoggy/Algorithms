/*

*/

#include "common_includes.h"


inline int genRandChar();
std::pair<std::string, int> createStr(std::string&, int);
void checkInput(int&);
int determineOccurences(const std::string&);

constexpr int L_ALPHA_START{ 97 }, RANGE_END{ 26 }, MAX_ALLOWED{ 30 },
MIN_NEEDED{ 2 };


int main() {

    srand(static_cast<unsigned>(time(0)));
    char goAgain;
    int num;
    std::string randStr;
    std::pair<std::string, int> p;

    do
    {
        std::cout << "Enter an integer and I will generate a random string\n"
            << "of 'N' letters => ";
        checkInput(num);
        p = createStr(randStr, num);

        std::cout << "Random string is: " << p.first << std::endl;
        if (p.second)
            std::cout << "REPEATING CHARACTERS: " << p.second << std::endl;
        randStr = "";
        std::cout << "Generate a new string? ['Y' 'N']? "; std::cin >> goAgain;
        std::cout << "\n\n";
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

    return L_ALPHA_START + (rand() % RANGE_END);
}


std::pair<std::string, int> createStr(std::string& str, int N) {

    std::pair<std::string, int> p;

    for (int i = 0; i < N; i++)
    {
        char letter = static_cast<char>(genRandChar());
        str += letter;
    }

    p.first = str;
    p.second = determineOccurences(str);
    return p;
}


int determineOccurences(const std::string& str) {

    int occurences{ 0 };

    for (int i = 0; i < (str.size() - 1); i++)
    {

        if (std::count(str.begin(), str.end(), str[i]) > 1) {

            occurences++;
        }
    }

    return (occurences > 0 ? occurences : 0);
}
