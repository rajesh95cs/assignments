
#include <iostream>
#include <string>
using namespace std;
void reverse(char a[]);
int main()
{
    char a[50];
    cout << " Please enter a string " << endl;
    cin>>a;
    reverse(a);
    cout << " The reversed string is : " <<a<<endl;
    return 0;
}
void reverse(char a[])
{   
    int i;
    for(i=0; a[i]!='\0'; i++);
    int length = i;
    char temp;
    for(i=0; i < length/2; i++) {
       temp = a[i];
       a[i] = a[length-i-1];
       a[length-i-1] = temp;
    }
}
