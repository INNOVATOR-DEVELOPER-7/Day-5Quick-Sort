# Day-5-Quick-Sort
Here Python Program for Quick Sort. Day 5 of Day 365.
- Initial Setup: Choose a 'pivot' element from the array. Commonly, the last element is chosen as the pivot.
- Partitioning: Rearrange the array so that elements smaller than the pivot come before it, and elements greater than the pivot come after it.
- Placing the Pivot: The pivot element is now in its correct sorted position.
- Recursive Sorting: Recursively apply the same process to the sub-arrays of elements with smaller and greater values.

Here's a visual representation using the example array [10, 80, 30, 90, 40, 50, 70]:

1. Initial Array: [10, 80, 30, 90, 40, 50, 70]
2. Choose Pivot: 70
3. Partitioning: Move elements smaller than 70 to the left, and larger to the right
   - Result: [10, 30, 40, 50, 70, 90, 80] 
4. Pivot in Correct Position: 70
5. Sub-array Before Pivot: [10, 30, 40, 50]
   - Choose Pivot: 50
   - Result: [10, 30, 40, 50]
6. Sub-array After Pivot: [90, 80]
   - Choose Pivot: 80
   - Result: [70, 80, 90]

This process continues recursively for the sub-arrays until the entire array is sorted.
