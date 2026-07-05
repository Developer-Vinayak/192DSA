class Solution{
  public int missingNumber(int[] nums){
    Arrays.sort(nums);
    int a=0;
    for(int i=0; i<=nums.length;i++){
      if(nums[i]!=i){
        a=i;
        break;
      }
      else{
        a=nums.length;
      }
    }
    return a;
  }
}
