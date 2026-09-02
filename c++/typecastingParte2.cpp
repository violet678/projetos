#include<iostream>
#include<string>
using namespace std;

main () {
    int number = 10;
    bool isValid = true;
    string text1 = to_string(number); //torna-se "789"
    string text2 = isValid ? "true" : "false"; //torna-se "true"

    return 0;
}