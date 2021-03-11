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
void change(vector <char> &text, vector <char> &alph, int k, int par) {
	int add = par ? 1 : -1;
	for (char &c : text) cout << alph[((c - 'A') + add * k + 26) % 26];
	cout << endl;
}
int main(){
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//Builds the alphaet array, used to  ease things up
	vector <char> alph;
	for (char c = 'A'; c <= 'Z'; ++c) alph.push_back(c);
	cout << "Enter the text: " << endl;
	string s; getline(cin, s);
	cout << "Enter K parameter: " << endl;
	int k ; cin >> k;
	cout << "Enter 1 for encrypting or 0 for decrypting" << endl;
	int par; cin >> par;
	vector <char> text;
	for (char &c : s) if (c != ' ') //Deletes spaces
		text.push_back(c > 'Z' ? c - ('a' - 'A') : c);//Capitalizes all characters
	change(text, alph, k, par);
	return 0;
}

