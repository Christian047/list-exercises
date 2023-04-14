# write a Python function that removes duplicates from an amount in a list
#  and also sum up all the items and remove 7% VAT from that amount. And print the amount

def amount():
 List_a =[ 2, 3,4,5,5,6,2,5,88,90,12] #This is a list 

# We used set function to remove duplicates in List_a
 List_b =  list(set(List_a)) 
#We summed up List_b and gave it a variable of Listc
 List_c = sum(List_b)

#We defined Vat as 7%

 Vat=0.07
#  calculated vat

 Vat_remove= List_c*Vat

# We removed 7% VAT from list_c

 Total_amount = List_c - Vat_remove

 print("the amount after VAT is removed is ", "#",Total_amount)

amount()