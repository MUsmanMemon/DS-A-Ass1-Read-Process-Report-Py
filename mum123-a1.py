"""
Created on Fri Aug  13 09:24:44 2021

@author: mum123 (Muhammad Usman Memon)
"""


#HashTable class defined, similar to python dictionaries to store unique words in file

class HashMap:  
    def __init__(self,maxy=1000):
        self.MAX = maxy
        self.arr = [[] for k in range(self.MAX)] #create an empty array at every node to accomodate collision
        
    def get_hash(self, key): #hashing to store values effectively
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def get(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def add(self, key, val):
        h = self.get_hash(key)
        # print(h)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
            
    def values(self):
        tlist = []
        for idx,val in enumerate(self.arr):
            if val:
                if len(val)>1:
                    for x,y in enumerate(val):
                        # print(val)
                        # print(x)
                        # print(y[1])  #[1] for value and [0] for key
                        tlist.append(y[1])
                
                else:
                    tlist.append(val[0][1])
        return tlist
    
    def keys(self):
        klist = []
        for idx,val in enumerate(self.arr):
            if val:
                if len(val)>1:
                    for x,y in enumerate(val):
                        #[1] for value and [0] for key
                        klist.append(y[0])
                
                else:
                    klist.append(val[0][0])
        return klist
    
    def items(self):
        ilist = []
        for idx,val in enumerate(self.arr):
            if val:
                if len(val)>1:
                    for x,y in enumerate(val):
                        #[1] for value and [0] for key
                        ilist.append(y)
                
                else:
                    ilist.append(val[0])
        return ilist
            

#---------------------------
# Ask User to input file name into the console.

filename = input("Please enter the file name with extension: ")
# filename = x + ".txt"
print("The filename you have entered is "+ filename +"\nThe results will be display below for this file \n")

# f = open(filename)

#dictionary to store the names and count its occurance
count_dict = HashMap(500)
testin = [] #an empty list to store the sorted list of words
#count = 0 #to count the number of words

# Python program to read
# file word by word
unwanted = [';', ':', '!', "_","*", '"' ,",",'”', '“',"\'","-",".","?","\'s"]
# opening the text file
with open(filename,'r', encoding="utf8") as file:
    # reading each line	
    for line in file:
        # reading each word		
        for word in line.split():
            # rt_word = word.lower()
            #count += 1
            #removing the unwanted characters in words
            rt_word = ''.join((filter(lambda i: i not in unwanted, word))).lower()
            
            #counting unique words using hash tables
            if rt_word in count_dict.keys():
                # count_dict[rt_word] += 1
                count_dict.add(rt_word, count_dict.get(rt_word)+1)
            #storing unique words using hash table
            else:
                count_dict.add(rt_word,1)
            	
            #print(rt_word)

# Sorting using merge sort function
def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:  #checking if the length of the list is 1 to know when to stop
      return unsorted_list
# Divide the list to sort into half from middle point
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]   #diving the list into 2
   right_list = unsorted_list[middle:]
   #recursively merge the list until it is merge_sort till 1 element
   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# mergin the small lists back into a new res list
def merge(left_half,right_half):
   res = [] #an empty list to store results
   while len(left_half) != 0 and len(right_half) != 0:
      # if diction[left_half[0]] > diction[right_half[0]]:
          #comparing string on their values, with first elemt of both lists
          #so if left elemt is smaller then it is appended first on the new list and removed from previous list
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
      
   return res

#Print out the total number of words in the file
print("The total number of words in the file are : "+ str(sum(count_dict.values())))

#Print the number of unique words in the file
print("\nThe number of unique words in the file are : "+ str(len(count_dict.keys())))

#counting through unique count values in the dictionary  

# uniquevalue = merge_sort(list(set(count_dict.values()))) 
#creating a list which stores the unique count numbers of words to sort according to count
uniquevalue = []
for po in count_dict.values():
    if po not in uniquevalue:
        uniquevalue.append(po)
        
uniquevalue = merge_sort(uniquevalue)

for i in range(len(uniquevalue)-1,-1,-1):
    # print(uniquevalue[i])  
    # tatti variable is used to create temporary list that hold filtered out data from the dictionary/hash table according to count
    tatti = list({key:value for (key,value) in count_dict.items() if value == uniquevalue[i]})
    testin += merge_sort(tatti)
       
print("\nThe first 15 words are :")
for i in testin[:15]:
    # print(testin +"  " + )
    # print("word "+str(i,count_dict.get(i))+" count")
    print(" Word : "+i + "  , Count : " +str(count_dict.get(i)))
    
print("\nThe Last 15 elements of the list are: ")
for x in testin[-15:]:
    # print("word "+str(x,count_dict.get(x))+" count")
    print(" Word : "+x + "  , Count : " +str(count_dict.get(x)))
    
# print("\n The length of the testin is "+ str(len(testin)))
# print("count variable "+ str(count))
  
        
    
        
    

