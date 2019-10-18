#include <iostream>
#include <math.h>
using namespace std;
int main() {
	int a, b, c, d;
	float x1, x2;
	cin >> a >> b >> c;
	if ((a!=0) and (b!=0)) {
	    d=b*b-4*a*c;
	    if (d>0){
	        x1=(-1*b+sqrt(d))/(2*a);
	        x2=(-1*b-sqrt(d))/(2*a);
	        cout << "X1:" << x1 <<" X2:" <<x2;
	    }
	    if (d==0){
	        x1=(-1*b+sqrt(d))/(2*a);
	        cout << "X1:" << x1;
	    }
	    
	    if (d<0){
	        cout << "";
	    }
	}
	
	if ((a==0) and (b!=0)){
	    x1=(-1*c)/b;
	    cout << "X1:" << x1;
	}
	
	if ((a==0) and (b==0)){
	    cout << "";
	}
	return 0;
}
