class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int small = i;
        for(int j = i; j < arr.length; j++){
            if(arr[small] > arr[j]) small = j;
        }
        return small;
	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    for(int i = 0; i< arr.length; i++){
	        int p = select(arr, i);
	        if(p != i){
	            arr[i] += arr[p];
	            arr[p] = arr[i] -  arr[p];
	            arr[i] = arr[i] - arr[p];
	        }
	    }
	}
}
