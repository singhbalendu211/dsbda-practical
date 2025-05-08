#Implement Greedy search algorithm for any of the following application:
#I. Selection Sort


'''
n = int(input("Enter number of jobs: "))
jobs = []
print("Enter Id deadline and profit respectively for each job:")
for i in range(n):
    job = input("Job " + str(i+1) + ": ").split()
    jobs.append(job)

sorter = lambda job: int(job[2]) 
jobs = sorted(jobs, key=sorter, reverse=True)

scheduled = []
time = 0

for i in jobs:
    if time <= int(i[1]):
        scheduled.append(i[0])
        time += 1

print("Jobs are scheduled as: ")
print(scheduled)

'''
def selection_sort(arr):
    """
    Implementation of Selection Sort using a greedy approach.
    At each step, it selects the smallest remaining element and swaps it into place.
    """
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6],
        []
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"Test case {i+1}:")
        print(f"Original array: {test_case}")
        sorted_arr = selection_sort(test_case.copy())
        print(f"Sorted array:   {sorted_arr}")
        print('\n')
