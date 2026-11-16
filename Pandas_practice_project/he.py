def  counting_sort(num) :    

    n  = len (num)

    max_val  = max(num)
    count  = [0] * (max_val + 1)   

    #counting frequency  

    for  i  in num : 
        count[i]  +=  1    

    #counting prefix sum  

    for j  in range (1,max_val + 1) : 
        count[j] += count[j -1]

    ans  = [0] * n  

    for k  in range (n - 1 , -1 , -1) : 
        val  = num[k]
        ans[count[val] - 1]  = val  
        count[val] -= 1 

    print(ans)







num  =  [64, 34, 25, 5, 22, 11, 90, 12] 
counting_sort(num)