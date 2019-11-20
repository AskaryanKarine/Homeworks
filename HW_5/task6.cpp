#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <map> 
using namespace std;

multimap<int, char> counted_str(string message)
{
    string s, str;
    int x, y;
    map <char, int> a;
    multimap<int, char> sortedPaths;
    map <char,int> res;
    //getline(cin, str);
    if (message.size()==0){
      cout << "\n";
    }
    for (int i = 0; message[i]; i++)
    {
        if (isalpha(str[i]))
            s += tolower(message[i]);
    }
    sort(s.begin(), s.end());
    x = y = 0;
    for (int i = y; s[i]; i++)
    {
        if (s[i] == s[i+1])
        {
            x++;
        }
        else
        {
            y = x;
            x++;
             a.insert ( pair<char,int>(s[i],x) );
            //cout << s[i] << ": " << x << endl;
            x = 0;
        }
    }
    for(auto it = a.rbegin(); it != a.rend(); ++it)
    {
        int key = (*it).second;
        char val = (*it).first;
        sortedPaths.insert(pair<int, char>(key, val));
    }
    
    //for(auto it = sortedPaths.rbegin(); it != sortedPaths.rend(); //++it)
      //cout << " " << (*it).first << " : " << (*it).second << endl;

  return sortedPaths;
}