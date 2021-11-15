def merge_sort(array):
	if len(array) > 1:
		mid = len(array)//2

		left_sub = array[:mid]
		right_sub = array[mid:]

		# Sorting the both halves recursively
		merge_sort(left_sub)
		merge_sort(right_sub)

		i = j = k = 0

        # Merge
		while i < len(left_sub) and j < len(right_sub):
			if left_sub[i] < right_sub[j]:
				array[k] = left_sub[i]
				i += 1
			else:
				array[k] = right_sub[j]
				j += 1
			k += 1

		# Defining two while loops to check if nay element was left in both the arrays respectively
        # Check any leftout element in left_sub array
		while i < len(left_sub):
			array[k] = left_sub[i]
			i += 1
			k += 1

        # Check any leftout element in right_sub array
		while j < len(right_sub):
			array[k] = right_sub[j]
			j += 1
			k += 1


# Display fucntion
def print_list(array):
	for i in range(len(array)):
		print(array[i], end=" ")
	print()


# Driver Code
str_arr=input("Enter the array to be sorted as comma separated numbers:\n")
array=[int(number) for number in str_arr.split(",")]
print("\nGiven array is: ")
print_list(array)

merge_sort(array)
print("\nCorrosponding sorted array is: ")
print_list(array)