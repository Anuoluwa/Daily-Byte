Given an array of integers, return whether or not two numbers sum to a given target, k. Note: you may not sum a number with itself

Ex: [1, 3, 8, 2], k = 10, return true (8 + 2)
Ex: [3, 9, 13, 7], k = 8, return false
Ex: [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

A simple solution to this problem might try picking two numbers and seeing if they sum to k. If they do we return true and if we iterate through all the numbers not being able to find such a pair, we return false.

public boolean twoSum(int[] nums, int target) {
    for (int i = 0; i 

While this approach works, it’s rather slow resulting from its O(N2) runtime. N2 coming from us comparing each of our N numbers to every other number in our array. By using a bit of space, we can knock down this runtime. Instead of doing a linear scan to find a number to complement our current number, we can introduce a hash map to remember what numbers we have seen. Now for each number, we can ask the question, “have we seen a number that when added to our current number will give us a sum of k?” If we have, we can return true, and if we haven’t can simply add our current number to our hash map to remember for the future. Following below is the solution described here

public boolean twoSum(int[] nums, int k) {
    HashMap map = new HashMap();
    for(int i = 0; i return false;

}
Big-O Analysis

Runtime: O(N) where N is the number of integers in our list.
Space complexity: O(N) because we use a hash map to store all N numbers in the worst case.