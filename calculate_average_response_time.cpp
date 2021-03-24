#include "iostream"
#include "map"
using namespace std;

#define time XTSS

string a;
double time;
int file_size;

map < int, int > file_counter;
map < int, double > M;

int main() {
	//freopen("RR", "r", stdin);

	while (cin >> a) {
		cin >> a;
		cin >> time >> file_size;

		//cout << time << " " << file_size << endl;

		M[file_size] += time;
		file_counter[file_size]++;
	}
    
	for (auto X : file_counter) {
		cout << X.first << " " << M[X.first]/(double)X.second << endl;
	}
	return 0;
}