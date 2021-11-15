# Function to merge all the files with optimum cost
def optimal_merge(files):
    optimal_merge_cost=0
    
    while(len(files)>1):
        temp=0
        # Consider two minimum file sizes
        for i in range(2):
            min_index=files.index(min(files))
            temp+=files[min_index]
            files.pop(min_index)
        
        files.append(temp)
        optimal_merge_cost+=temp

    return optimal_merge_cost


# A list containing sizes of all the lists to be merged
feed=input("Enter the array to be sorted as comma separated numbers:\n")
file_size_list=[int(number) for number in feed.split(",")]
cost=optimal_merge(file_size_list)
print("Optimal merge cost for given set of files is:",cost)