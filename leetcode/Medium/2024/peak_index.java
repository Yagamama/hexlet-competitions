class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = 0;
        int right = arr.length;
        int med = (right - left) / 2;
        while ((arr[med+1] >= arr[med]) | (arr[med-1] >= arr[med])){
            if (arr[med] <= arr[med-1])
                right = med;
            else if (arr[med] <= arr[med+1])
                left = med;
            med = (right - left) / 2 + left;
        }
        return med;
    }
}