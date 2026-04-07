## **Problem 2: Contains Duplicate (Arrays)**

While Two Sum focused on finding a *pair*, this problem focuses on **membership testing**—a core skill for almost every high-level algorithm.

### **1. The Challenge**
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.
* **Constraints:** $1 \leq nums.length \leq 10^5$.
* **Example:** `nums = [1, 2, 3, 1]` $\rightarrow$ `True`

### **2. The Pattern Trigger**
* **Trigger:** "Frequency," "Unique," or "Duplicate."
* **Pattern:** **Hash Set.** A Set is the most efficient way to track "seen" items because lookups and insertions are $O(1)$.



### **3. Conceptual Approach**
There are three ways to solve this, but we will focus on the most "Interview-Correct" one:
1.  **Brute Force ($O(N^2)$):** Compare every element with every other element. (Too slow).
2.  **Sorting ($O(N \log N)$):** Sort the array and check if adjacent elements are the same. (Good, but not optimal).
3.  **Hash Set ($O(N)$):** Iterate once. If a number is already in our `seen` set, we found a duplicate.

### **4. Complexity Target**
* **Time Complexity:** $O(N)$ — One pass through the array.
* **Space Complexity:** $O(N)$ — In the worst case (all unique), we store every element in the set.

### **5. The Skeleton**
```python
def contains_duplicate(nums: list[int]) -> bool:
    # 1. Initialize an empty set
    
    # 2. Iterate through each number
    
    # 3. Check if number is in set
    
    # 4. If not, add to set; if yes, return True
    
    # 5. Return False if loop completes
    pass
```

---

### **6. Pythonic Solution**
In an interview, you should explain the manual set iteration first, but then show the "One-Liner" to demonstrate language expertise.

**Option A: The Manual Way (Best for explaining logic)**
```python
#Start code
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
#End code
```

**Option B: The Pythonic Pro-Trick (Minimum code)**
```python
#Start code
def contains_duplicate(nums: list[int]) -> bool:
    # A set only stores unique values. 
    # If the length changes, there were duplicates.
    return len(nums) != len(set(nums))
#End code
```

### **7. Test Bench**
* **Case 1 (Duplicate exists):** `nums = [1, 2, 3, 1]` $\rightarrow$ Expected: `True`
* **Case 2 (All unique):** `nums = [1, 2, 3, 4]` $\rightarrow$ Expected: `False`
* **Case 3 (Large duplicates):** `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` $\rightarrow$ Expected: `True`

---

**Efficiency Check:** Why is `len(nums) != len(set(nums))` often preferred? Because `set(nums)` is implemented in C-level code in Python, making it incredibly fast for large datasets.
