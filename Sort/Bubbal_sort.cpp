#include<iostream>
using namespace std;

int main(){
	int arr[] = {20, 4, 3, 99, 44};
	int n = sizeof(arr)/sizeof(arr[0]);
	
	for(int i=0; i<n; i++){
		for(int j = i; j<n; j++){
			if(arr[j] > arr[j+1]){
				swap(arr[j], arr[j+1]);
			}
		}
	}
	
	for(int i =0; i<n; i++){
		cout<<arr[i]<<" ";
	}
}
