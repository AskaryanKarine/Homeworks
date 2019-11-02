#include <iostream>
#include <locale.h>
#include <string>
#include <cstring>
using namespace std;
int main() {
  setlocale(LC_ALL, "Rus");
	int n,res1,res2,l;
	string s,s1;
  s="";
	res1=0; res2=0;
  cin >> n;
	for (int i=0; i<=n; i++){
	  getline(cin, s1);
    l=s1.size();
	  for (int j=0; j<l; j++){
	    s1[j]=tolower(s1[j]);
	    }

    for (int j=0; j<l; j++){
      if (isalpha(s1[j])){
        s=s+s1[j];
        }
      }
      l=s.size();
      for (int j=0; j<l/2; j++){
        if (s[j]!=s[l-j-1]){
          if (i%2==0 and res2==0){
            res1=1;
            break;
          }

          if (i%2==1 and res1==0){
            res2=1;
            break;
          }
        }
      }
    s="";
	}
	if (res1==1) {
    cout <<"Сослан на Плутон собеседник";
  }

  if (res2==1) {
    cout <<"Сослан на Плутон Юра";
  }

  if (res1==0 and res2==0){
    cout <<"Сослать обоих";
  }
	return 0;
}