class Solution:
    def mergeSort(self, arr, l, r):
        # Base case
        if l >= r:
            return

        # Find middle
        mid = (l + r) // 2

        # Sort left half
        self.mergeSort(arr, l, mid)

            # Sort right half
        self.mergeSort(arr, mid + 1, r)

            # Merge both halves
        self.merge(arr, l, mid, r)


    def merge(self, arr, l, mid, r):

        left = arr[l:mid + 1]
        right = arr[mid + 1:r + 1]

        i = 0
        j = 0
        k = l

        # Compare elements from left and right
        while i < len(left) and j < len(right):
    
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining elements in left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Remaining elements in right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1