
#include <iostream>

#include <windows.h>
using namespace std;

int main(){
	
	HANDLE hconsole=GetStdHandle(STD_OUTPUT_HANDLE); 
SetConsoleTextAttribute(hconsole,0);

for(int i=0; i<=255; i++){
	
SetConsoleTextAttribute(hconsole,i);

cout<<"+-+-+-+-+-+-+-+-+-+-+"<<endl;
cout<<"TEXTO DEL COLOR # ";
cout<<i<<endl;
cout<<"+-+-+-+-+-+-+-+-+-+-+"<<endl;
}
SetConsoleTextAttribute(hconsole,15);
}
