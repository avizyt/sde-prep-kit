Excellent choice. Starting with the fundamentals is the only way to ensure the advanced patterns (like DP or Graphs) don't feel like "magic" later on.

We are starting with **Module 1: Linear Data Structures**.
## **Problem 1: Two Sum (Arrays)**

This is the quintessential "intro to hashing" problem. It moves you from a naive $O(N^2)$ brute-force mindset to an optimized $O(N)$ lookup mindset.

### **1. The Challenge**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
* **Constraints:** Each input has exactly one solution. You may not use the same element twice.
* **Example:** `nums = [2, 7, 11, 15], target = 9` $\rightarrow$ `[0, 1]`

### **2. The Pattern Trigger**
* **Trigger:** "Find a pair that sums to X" in an **unsorted** array.
* **Pattern:** **Hash Map (One-Pass).** Since we need to find a "complement" ($target - current$), a Hash Map allows us to check if that complement was seen previously in $O(1)$ time.

### **3. Conceptual Approach**
1.  Initialize an empty dictionary `prev_map` where `key = value` and `value = index`.
2.  Iterate through the array using `enumerate` to get both the index (`i`) and the value (`n`).
3.  Calculate the `diff = target - n`.
4.  Check if `diff` exists in `prev_map`.
    * If yes: You found the pair! Return `[prev_map[diff], i]`.
    * If no: Add the current number and its index to `prev_map` and keep moving.



### **4. Complexity Target**
* **Time Complexity:** $O(N)$ — We traverse the list only once.
* **Space Complexity:** $O(N)$ — In the worst case, we store $N$ elements in the dictionary.

### **5. The Skeleton (Try thinking through this first)**
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    # 1. Create a map to store value -> index
    
    # 2. Loop through nums with index
    
    # 3. Find complement
    
    # 4. Return result or update map
    pass
```

---

### **6. Pythonic Solution**
```python********
#Start code
import collections

def twoSum(nums: list[int], target: int) -> list[int]:
    # We use a standard dict for O(1) average lookups
    prev_map = {} 

    for i, n in enumerate(nums):
        diff = target - n
        
        if diff in prev_map:
            # If the complement exists, return the stored index and current index
            return [prev_map[diff], i]
        
        # Otherwise, store the current number's index
        prev_map[n] = i
    
    return [] # Should not be reached based on constraints
#End code
```

### **7. Test Bench**
* **Case 1 (Standard):** `nums = [2, 7, 11, 15], target = 9` $\rightarrow$ Expected: `[0, 1]`
* **Case 2 (Unordered):** `nums = [3, 2, 4], target = 6` $\rightarrow$ Expected: `[1, 2]`
* **Case 3 (Same Values):** `nums = [3, 3], target = 6` $\rightarrow$ Expected: `[0, 1]`

---

