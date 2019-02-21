//
//  main.cpp
//  415P1
//
//  Created by Will Lucic on 2/21/19.
//  Copyright © 2019 LucicLangwell. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int consecutiveGCD(const int& left, const int& right);
double avgConsecutiveGCD(const int& input);

int main(int argc, const char * argv[]) {
    ofstream consecutiveGCDdat, euclidsGCDdat;
    consecutiveGCDdat.open("Consecutive GCD.dat");
    euclidsGCDdat.open("Euclid's GCD.dat");
    
    for (int i = 1; i <= 100; i += 3)
    {
        consecutiveGCDdat << i << '\t' << avgConsecutiveGCD(i) << endl;
    }
    
    consecutiveGCDdat.close();
    euclidsGCDdat.close();
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

double avgConsecutiveGCD(const int& input)
{
    int totalDivs = 0;
    for (int i = 1; i <= input; i++)
    {
        totalDivs += consecutiveGCD(input, i);
    }
    return totalDivs/input;
}
