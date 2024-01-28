#include<iostream>
#include<vector>
#include<unordered_map>
#include<bits/stdc++.h>
#include <chrono>
using namespace std::chrono;
using namespace std;

int main()
{
    auto start = high_resolution_clock::now();
        unordered_map<int,vector<int>> table;
    int rows = 30000;
    int cols = 10000000;
    for(int i=0;i<rows;i++)
    {
        vector<int> temp;
        for(int j=0;j<100;j++)
        {
            temp.push_back(rand()%cols);
        }
        table[rand()%100000] = temp;
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by function: "<< duration.count()/1000 << " milliseconds" << endl;
    return(0);
}