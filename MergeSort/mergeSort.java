class MergeSort
{
	int[] mergeSort(int arr[]){
		mergeSort(arr, new int[arr.length], 0, arr.length-1);
	}
	void mergeSort(int arr[], int temp[], int low, int high){
		if(low<high){
			int middle = (low+high)/2;
			mergeSort(arr, temp, low, middle);
			mergeSort(arr, temp, middle+1, high);
			merge(array, temp, low, middle, high);
		}

	}
	void merge(int[] arr, int temp[], int leftStart, int middle, int rightEnd){
		int leftEnd = (leftStart+rightEnd)/2;
		int rightStart = leftEnd+1;
		int size = rightEnd - leftStart +1;

		int left = leftStart;
		int right = rightStart;
		int index = leftStart;

		while(left <= leftEnd && right<=rightEnd){
			if(arr[left]<=arr[right]){
				temp[index] = arr[left];
				left++;
			}else{
				temp[index] = arr[right];
				right++;
			}
			index++;
		}

		System.arraycopy(arr, left, temp, index, leftEnd-left+1);
		System.arraycopy(arr, right, temp, index, rightEnd-right+1);
		System.arraycopy(temp, leftStart, arr, leftStart, size);

	}





}