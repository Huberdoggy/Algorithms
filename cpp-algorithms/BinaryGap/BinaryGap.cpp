/*
A binary gap within a positive integer N is any maximal sequence of consecutive
zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap
of length 2. The number 529 has binary representation 1000010001 and contains
two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

int solution(int N);

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
*/

#include "common_includes.h"

void checkInput(int&, int);
void decToBin(int, std::string&);
int findLongestGap(const std::string&);


void decToBin(int N, std::string& bin_num) {

    for (int i = 31; i >= 0; i--) // corresponding to 32 bit int
    {
        int b = N >> i; // bitwise
        (b & 1) ? bin_num += "1" : bin_num += "0";
    }
    // Trim leading zeroes
    bin_num.erase(0, bin_num.find_first_not_of('0'));
}


void checkInput(int& num, int min) {

    while (!(std::cin >> num) || (num < min || num > INT_MAX))
    {
        std::cin.clear();
        ignoreExtraneous();
        std::cout << "ERROR! Please ensure input is greater than or equal to "
            << min << ",\nand less than or equal to " << INT_MAX << "\n=> ";
    }
}


int findLongestGap(const std::string& bin_num) {

    int count{ 0 };
    std::string offset = bin_num.substr(1, bin_num.length() - 1);

    for (size_t i = 0; i < bin_num.length(); i++)
    {
        if (!(std::count(offset.begin(), offset.end(), '1'))) {
            break; // No bits turned on
        }
        else if (!(std::count(offset.begin(), offset.end(), '0'))) {
            break; // All bits turned on
        }
        else if (i > 0 && offset[i] == '1')
        {
            break; // We found a gap
        }
        
        count++;
    }
    
    return count;
}


int main() {

    int min{ 1 }, num;
    std::string bin_num;

    // Get user input
    std::cout << "Enter an integer between " << min << " and "
        << INT_MAX << "=> ";

    checkInput(num, min);
    decToBin(num, bin_num);

    std::cout << "The binary representation of " << num << " is " << bin_num
        << '\n';

    int count = findLongestGap(bin_num);
    (!count) ? printf("\n%s does NOT have a binary gap\n", bin_num.c_str())
        : printf("\nLongest binary gap for %s: %d\n", bin_num.c_str(), count);

    return 0;
}

