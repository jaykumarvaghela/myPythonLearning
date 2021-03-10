list_Expense = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
print(list_Expense[1] - list_Expense[0])

# Find out your total expense in first quarter (first three months) of the year.
adds = 0
for i in range(3):
    adds += list_Expense[i]
print(adds)

# Find out if you spent exactly 2000 dollars in any month
print(True if 2000 in list_Expense else False)

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list4
list_Expense.append(1980)
print(list_Expense)

"""
You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

list_Expense.pop(3)
list_Expense.insert(3,2390)
print(list_Expense)