#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <map> 
using namespace std;

map<string, int> counted_str(string& message)
{
  string s, str;
  int x, y;
  map <string, int> a;
  multimap<int, string> sortedPaths;
  map <string, int> res;
  getline(cin, str);
  if (str.size()==0)
    cout << "\n";
  for (int i = 0; str[i]; i++) {
    if (isalpha(str[i]))
      s += tolower(str[i]);
  }
  sort(s.begin(), s.end());    
  x = y = 0;
  for (int i = y; s[i]; i++) {
    if (s[i] == s[i+1]) {
      x++;
    }
    else {
      y = x;
      x++;
      a.insert ( pair<string,int>(string(1, s[i]),x) );
      //cout << s[i] << ": " << x << endl;
      x = 0;
      }
    }
  for(auto it = a.rbegin(); it != a.rend(); ++it) {
        int key = (*it).second;
        string val = (*it).first;
        sortedPaths.insert(pair<int, string>(key, val));
    }
    
  for(auto it = sortedPaths.rbegin(); it!=sortedPaths.rend(); ++it){
    cout << " " << (*it).second << " : " << (*it).first << endl;
    res.insert(pair<string, int>((*it).second, (*it).first));
  }
  return res;
}