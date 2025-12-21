#include<iostream>
using namespace std;

int linearSearch(int arr[], int n, int target){
	for(int i=0; i<n; i++){
		if(arr[i] == target){
			return i;
		}
	}
	return -1;
}

int main(){
	int arr[] = {50, 7, 91, 35, 33, 22};
	int n = sizeof(arr);
	int target = 35;
	
	int index = linearSearch(arr, n, target);
	if(index == -1){
		cout<<"Elemnt is not found";
	}
	else{
		cout << "Element is Found : "
     << "Value: " << arr[index]
     << " And it is found at index: " << index << "\n";
	}
	return 0;
}
