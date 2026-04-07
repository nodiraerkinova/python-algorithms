N = input().strip() 
 
even_sum, odd_sum = 0, 0 
 
 
for index in range(len(N)): 
    digit = int(N[index]) 
    odd_sum += digit if index % 2 == 0 else 0 
 
even_sum += digit    
diff = even_sum - odd_sum 
 
print("Yes") if diff == 0 or diff % 11 == 0 else print("No")