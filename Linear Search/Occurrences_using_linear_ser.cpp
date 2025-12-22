#include <iostream>
using namespace std;

int main(){
	int n;
	cout<<"Enter the size of array : ";
	cin>>n;
	
	int arr[n];
	cout<<"Enter the arr elements : ";
	for(int i =0; i<n; i++){
		cin>>arr[i];
	}
	
	int target;
	cout<<"Enter the targeted value : ";
	cin>>target;
	
	
	bool found = false;
	cout<<"Eelement found at index - ";
	for(int i = 0; i<n; i++){
		if(arr[i] == target){
			cout<<i<<" ";
			found = true;
		}
	}
	
	if(!found){
		cout<<"Not Found";
	}
	
	return 0;
}
