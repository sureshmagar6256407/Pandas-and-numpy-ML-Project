num = [170, 45, 75, 90, 802, 24, 2, 66]

def counting_sort(num ,exp) : 
    n   = len(num)
    count  = [0] * 10  
    output  = [0] * n  

    #counting the frequency  

    for i  in range (0 , n) : 
        index = num[i] // exp 
        count[index % 10] += 1 

    for j  in range (1, 10) : 
        count[j] += count[j - 1]

    k  = n   - 1 

    while k >= 0 : 
        index     = num[k] // exp  
        output[count[index % 10] - 1]   = num[k]
        count[index % 10]  -= 1    
        k -= 1

    for l in range (0 , len(num)) : 
        num[l]  = output[l]  


def radix_sort(num) :   

    max_val  = max(num)
    exp  = 1  

    while max_val / exp  >= 1 : 
        counting_sort(num, exp)  
        exp *= 10  
    
radix_sort(num)  
print(num)