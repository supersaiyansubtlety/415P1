//
//  main.cpp
//  415P1
//
//  Created by Will Lucic on 2/21/19.
//  Copyright © 2019 LucicLangwell. All rights reserved.
//

#include <iostream>

int consecutiveGCD(const int& left, const int& right);
int avgConsecutiveGCD(const int& input);

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

int consecutiveGCD(const int& left, const int& right)
{
    int divisions = 0;
    int min = (left > right? left:right );
    for (int i = min; i > 0; i--)
    {
        if (left % min == 0)
        {
            divisions++;
            if (right % min ==0)
            {
                divisions++;
                return divisions;
            }
        }
    }
    return divisions;
}

int avgConsecutiveGCD(const int& input)
{
    int totalDivs = 0;
    for (int i = 1; i <= input; i++)
    {
        totalDivs += consecutiveGCD(input, i);
    }
    return totalDivs/input;
}
