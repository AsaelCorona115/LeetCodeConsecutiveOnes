
#Array for testing
nums = [0,1];

#Some global variables, overall maximum number of consecutive ones
overall_max = 0; 
index = 0;

#Loop to go over the array
if(len(nums) > 1):
    for value in nums:
        
        #Starts at zero for every instance
        current_consecutive = 0; 
    
    #If the number is 1 and the number is not the last element in the array analysis begins
        if(value == 1 and index == (len(nums) - 1)   ):
            current_consecutive = 1
            
        if(value == 1 and index < (len(nums) - 1)   ):
            current_consecutive = 1
            current_position = index + 1;
            while(nums[current_position] == 1):
                current_consecutive+=1;
                if(current_position + 1 == len(nums)):
                    break;
                else:
                        current_position+=1;
        
        print("Element number " + str(index) + " has " + str(current_consecutive) + " consecutive ones")
        if(current_consecutive > overall_max):
            overall_max = current_consecutive;
    
        index+=1;

elif(len(nums) == 1):
    if(nums[0] == 1):
        overall_max = 1;

else:
    overall_max = 0; 
print("Max number of consecutive ones is " + str(overall_max))
