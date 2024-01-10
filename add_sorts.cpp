#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;
void ShakerSort(vector<int>& values) {
  if (values.empty()) {
    return;
  }
  int left = 0;
  int right = values.size() - 1;
  while (left <= right) {
    for (int i = right; i > left; --i) {
      if (values[i - 1] > values[i]) {
        swap(values[i - 1], values[i]);
      }
    }
    ++left;
    for (int i = left; i < right; ++i) {
      if (values[i] > values[i + 1]) {
        swap(values[i], values[i + 1]);
      }
    }
    --right;
  }
}
float check_time(int n, int k){
    srand(time(0));
    vector<int> v;
    for (int i = 0; i < n; i++)
        {
            int num = rand() % k;
            v.push_back(num);
        }
    unsigned int start_time = clock();
    ShakerSort(v);
    int end_time = clock();
    // cout << v[0] << " " << v[1] << " " << v[2] << endl;
    return (float)(end_time - start_time) / CLOCKS_PER_SEC;
}
int main(){
    float t = check_time(100000, 200000);
    cout << t << endl;
}
