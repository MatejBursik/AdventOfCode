#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    //reading file 
    fstream file;
    file.open("C:\\Users\\matej\\Documents\\Projects\\AdventOfCode\\2022\\02\\input.txt", ios::in);
    int points_1 = 0;
    int points_2 = 0;

    if (file.is_open()){
        string line, elf, you;
        
        while (getline(file,line)){
            elf = line[0];
            you = line[2];
            
            //part1
            if (elf == "A" && you == "Y"){
                points_1 += (2 + 6);
            }else if (elf == "A" && you == "Z"){
                points_1 += (3 + 0);
            }else if (elf == "A" && you == "X"){
                points_1 += (1 + 3);
            }else if (elf == "B" && you == "Y"){
                points_1 += (2 + 3);
            }else if (elf == "B" && you == "Z"){
                points_1 += (3 + 6);
            }else if (elf == "B" && you == "X"){
                points_1 += (1 + 0);
            }else if (elf == "C" && you == "Y"){
                points_1 += (2 + 0);
            }else if (elf == "C" && you == "Z"){
                points_1 += (3 + 3);
            }else if (elf == "C" && you == "X"){
                points_1 += (1 + 6);
            }

            //part2
            if (elf == "A" && you == "Y"){
                points_2 += (1 + 3);
            }else if (elf == "A" && you == "Z"){
                points_2 += (2 + 6);
            }else if (elf == "A" && you == "X"){
                points_2 += (3 + 0);
            }else if (elf == "B" && you == "Y"){
                points_2 += (2 + 3);
            }else if (elf == "B" && you == "Z"){
                points_2 += (3 + 6);
            }else if (elf == "B" && you == "X"){
                points_2 += (1 + 0);
            }else if (elf == "C" && you == "Y"){
                points_2 += (3 + 3);
            }else if (elf == "C" && you == "Z"){
                points_2 += (1 + 6);
            }else if (elf == "C" && you == "X"){
                points_2 += (2 + 0);
            }
        }
    }
    file.close();

    cout << points_1 << endl;
    cout << points_2 << endl;

    return 0;
}
