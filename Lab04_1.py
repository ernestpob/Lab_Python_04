print "Ernest Pobee"

##                       QUESTION 1
# Given list
groceries = ['bananas','strawberries','apples','bread']

print groceries
## Appending champagne to the list
groceries.append('champagne')

print groceries

# Removing bread from list ...'cos john doesn't like it
groceries.remove('bread')

print groceries

## In order for John to find items he need easily we can sort the list
groceries.sort()
#for foodItem in groceries:
  #   print foodItem, 'is on isle', foodItem[0]

print groceries

print "\n\n"

##                       QUESTION 2
## 1 - Using a dictionary data structure, we could map each item in stock
##        to their prices. This will make a search request faster and easier

## Code to store information about items in stock and their prices

Stock_Items = {'Apples' : 7.3, 'Bananas' : 5.5, 'Bread' : 1.0, 'Carrots' : 10.0, 'Champagne' : 20.90, 'Strawberries' : 32.6}

print Stock_Items

## To modify price of Strawberries to 63.43,

Stock_Items['Strawberries'] = 63.43

print Stock_Items


## Adding an item Chicken with a price of 6.5

Stock_Items['Chicken'] = 6.5

print Stock_Items

##                  QUESTION 3

# # 3a - The best data structure that would fit this request by the C.E.O. would be a list.
# #          A list is an ordered collection of data Each element can be accessed by indexing

# 3b creating the collection of items that will be sent to the CEO.

in_stock = Stock_Items.keys()

print in_stock

## 3c - Converting the data structure in_stock to the immutable always_in_stock.

always_in_stock = tuple(in_stock)

print always_in_stock

## attemptin to modify always_in_stock[0] the 
# always_in_stock[0] = 'Vinegar'

# print always_in_stock


## 3d - Writing code that will print out the message
print "\n\n"
print "Welcome to shoprite! We always sell:"
for item in always_in_stock:
     print item


##                  QUESTION 4

## A viable data structure will be a dictionary with the items as keys and lists containing
##  the prices of the items at different stores as the values

## B      Design a function to inset another price in a given list of prices eg (e.g., $0.50, $1.25, $1.50)

     def binary_insert(new_float,price_list):
          #modifies the input list to include the new_float
          np = new_float
          pl = price_list
          j = 0
          for i in range(0,len(pl) + 1):
               if( pl[i] > np and j !=1):
                    pl.insert(i , np)
                    j += 1
          for i in pl:
               print i
          return 
# new list is created
gh = [0.50,1.0,1.25,100.50]
# binary_insert function is called with a float and a list (gh)
binary_insert(2.0,gh)

## Creating a function a function that returns the minimum amount of money that Steven and John will
#v have to spend on their grocery list.
print
print groceries
applelist = [1.20,1.3,1.25,1.4]
bananaslist = [2.20,2.10,2.50,2.13]
champagnelist = [6.20,6.50,5.30,7.20]
strawberrieslist = [4.10,4.20,4.45,4.60]     # 1.2 + 2.1 + 5.3 + 4.1 = 12.7

item_price_dict = { groceries[0]:applelist , groceries[1]:bananaslist , groceries[2]:champagnelist , groceries[3]:strawberrieslist }
#print item_price_dict
#print item_price_dict['apples']

def min_cost(grocery_list,item_to_price_list_dict):
     gl = grocery_list
     it_pl = item_to_price_list_dict
     total_cost = 0.0                                        #store the accumulated minimum cost
     for item in gl:                                            # pick an item from the list
          for litem in it_pl:                                   # pick an item from the dictionary
               min_list_price = 0.0              # variable to store the smallest value in extracted_list. By default, its very large
               if item == litem:                              # if a match is found
                    extracted_list = it_pl[litem]            #assign the prices of that item to a list
          for price in extracted_list:
               if (extracted_list.index(price) == 0):
                    min_list_price = price
               if(price < min_list_price):                  # if the current price is lesser than the min_list price assign its value to min list price
                    min_list_price = price
          total_cost +=min_list_price                  #After getting the least price, add it to overall cost
     print "The least amount they're gonna pay is",total_cost #print output message
     return

min_cost(groceries,item_price_dict)
