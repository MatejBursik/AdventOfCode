#include <iostream>
#include <fstream>
#include <string>
#include <vector> //vector - dynamic array
#include <bits/stdc++.h> //sort

using namespace std;

int main(){
    //reading file 
    fstream file;
    file.open("C:\\Users\\matej\\Documents\\Projects\\AdventOfCode\\2022\\01\\input.txt", ios::in);
    
    if (file.is_open()){
        string line;
        vector<int> elves_calories;
        int total = 0;

        //getting the total callories per elf
        
        while (getline(file,line)){
            if (line != ""){
                total += (stoi(line));
            }else{
                elves_calories.push_back(total);
                total = 0;
            }
        }

        //sorting the total callories per elf
        sort(elves_calories.begin(), elves_calories.end(), greater<int>());
        int first = 0; int second = 0; int third = 0;
        
        //printing answers for part1 and part2
        cout << elves_calories[0] << endl;
        cout << elves_calories[0] + elves_calories[1] + elves_calories[2];

    //error testing for presious stupid mistakes
    }else if (!file.is_open()){
        cout << "Unable to open file";
    }
    file.close();

    return 0;
}
