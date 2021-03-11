#include <bits/stdc++.h> 
using namespace std; 
/* * * *   * * *   	* * * */ 
#define mp make_pair 
typedef long long ll; 
typedef pair<int, int> pii; 
/* * * *   * * *   	* * * */ 
/* * 
 * 
 * Too many mind, no mind. 
 * 
 * */ 
pii find(char c, vector<vector<char>> &key) { 
	for (int i = 0; i < 5; ++i) { 
		for (int j = 0; j < 5; ++j) { 
			if (key[i][j] == c) return {i, j}; 
		} 
	} 
	return {-1, -1}; 
} 
void decrypt(vector <char> &text, vector<vector<char>> &key) { 
	for (int i = 0; i + 1 < text.size(); i += 2) {
		char a = text[i], b = text[i + 1]; 
		if (a == 'J') a = 'I'; 
		if (b == 'J') b = 'I'; 
		pii x = find(a, key), y = find(b, key); 
		if (x.first == y.first) { //Same row 
			cout << key[x.first][(x.second - 1 + 5) % 5] << key[y.first][(y.second - 1 + 5) % 5]; 
		} else if (x.second == y.second) {//Same column 
			cout << key[(x.first - 1 + 5) % 5][x.second] << key[(y.first - 1 + 5) % 5][y.second]; 
		} else { 
			cout << key[x.first][y.second] << key[y.first][x.second];
		} 
		cout << ' ';
	} 
	cout << '\n'; 
} 
int main(){ 
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0); 
	//freopen("input.txt", "r", stdin); 
	//freopen("output.txt", "w", stdout); 
	cout << "Enter the key: " << endl;
	string s; getline(cin, s);
	vector <int> done(26, 0);
	vector <vector <char>> key (5, vector <char> (5));
	int pos = 0;
	for (int i = 0; i < s.size(); ++i) {//Buids the key matrix
		if (s[i] != ' ') {
			if (s[i] > 'Z') s[i] -= 'a' - 'A';//Capitalizes all characters
			if (s[i] == 'J') s[i] = 'I';
			if (!done[s[i] - 'A']) {
				key[pos / 5][pos % 5] = s[i];
				done[s[i] - 'A']++;
				pos++;
			}
		}
	}
	for (char c = 'A'; c <= 'Z'; ++c) {//Add remaining values
		if (c != 'J' && !done[c - 'A']) {
			key[pos / 5][pos % 5] = c;
			done[c - 'A'] = 1;
			pos++;
		}
	}
	cout << "Enter the text to encrypt: " << endl;
	getline(cin, s);
	vector <char> text;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == ' ') continue;//Elimnates spaces
		if (s[i] > 'Z') s[i] -= 'a' - 'A';//Capitalized all characters
		if (i && s[i - 1] == s[i]) text.push_back(s[i] == 'X' ? 'Y' : 'X');//Adds padding if needed
		text.push_back(s[i]);
	}
	if (text.size() & 1) text.push_back('X');//Adds padding if needed
	decrypt(text, key); 
	return 0; 
}

