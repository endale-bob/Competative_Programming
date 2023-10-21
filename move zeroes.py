class Solution {
    public void moveZeroes(int[] nums) {
        int pointer1 = 0;
        int pointer2 = 0;
        int n = nums.length;

        while(pointer1 < n && pointer2 < n ){
            if(nums[pointer1] != 0) pointer1 ++;
            else if( nums[pointer2] == 0) pointer2 ++;
            else if(pointer2 < pointer1) pointer2 = pointer1;
            else{
                int temp = nums[pointer1];
                nums[pointer1] = nums[pointer2];
                nums[pointer2] = temp;
                pointer1 ++;
                pointer2 ++;
            }
        }

    }
}
