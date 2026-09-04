#include<iostream>
#include<string>
using namespace std;

int main() {
    double n1 = 789.0;
    string text1 = to_string(n1);
    //torna-se "789.000000"

    double n2 = 789.5;
    string text2 = to_string(n2);
    //torna-se "789.500000"

    double n3 = 789.123456;
    string text3 = to_string(n3);
    //torna-se "789.123456"

    //convertendo string para um tipo diferente
    string numberText = "123";
    int number = stoi(numberText); //torna-se 123

    //string para double
    string decimalText = "123.456";
    double decimalNumber = stod(decimalText); //torna-se 123.456

    string invalidStart = "abc";
    int number2 = stoi(invalidStart); //vai lançar um erro
    return 0;
}