#include <iostream>
#include <string>
using namespace std;

int main() {
    
    struct student{
        int ID;
        bool isCool = false;
        bool isAnnoying = true;
        string discord;
    };

    student Noah;
    Noah.ID = 962276;
    Noah.isCool = true;
    Noah.isAnnoying = false;
    Noah.discord = "nerfminer1587";

    student Gus;
    Gus.ID = 774884;
    Gus.isCool = true;
    Gus.isAnnoying = false;
    Gus.discord = "thatgoblinking";

    cout << "Noah - ID:"<<Noah.ID<<", Cool:"<<Noah.isCool<<", Annoying:"<<Noah.isAnnoying<<", Discord:"<<Noah.discord << endl;
    cout << "Gus - ID:"<<Gus.ID<<", Cool:"<<Gus.isCool<<", Annoying:"<<Gus.isAnnoying<<", Discord:"<<Gus.discord << endl;
}