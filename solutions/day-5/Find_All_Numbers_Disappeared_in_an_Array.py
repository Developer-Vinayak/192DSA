class Solution{
  public List<Integers> findDisappearedNumbers (int[] nums){
    ArrayList<Integer> list = new Arraylist();
    int freq[] = new int[nums.length + 1];
    for(int i=0; i<nums.length; i++){
      freq[nums[i]]++;
    }
    for(int i=1; i<=nums.length; i++){
      if(freq[i]==0){
        list.add(i);
      }
    }
    return list;
  }
}
