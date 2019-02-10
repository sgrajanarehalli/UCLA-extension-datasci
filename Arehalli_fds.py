
# coding: utf-8



#The json module has functions that allow you to read json files into python data structures like lists and dicts
import json




#Use the json module to open the raw json data and convert it into a list of python dicts
jsonData = open('pizza_request_dataset.json', 'r')
pizza_data = json.load(jsonData)
jsonData.close()




#Create a subset of pizza_data by slicing the list
pizza_subset= pizza_data[:100]




#Export the sliced subset into its own json file. This can be opened again and parsed into a list of dicts using json.load
with open('pizza_request_subset.json', 'w') as pizza_request_subset:
    json.dump(pizza_subset, pizza_request_subset)
    pizza_request_subset.close()





#The scroll function pretty-prints the entry at the current index to the console, then prompts for user input. 
#If the user input is 'n', the index is increased by 1 and scroll is called again.
#If the user input is 'b', the index is decreased by 1 and scroll is called again.
#If the user input is 'q', they exit out of the program
#If user input is invalid, scroll is called again with no change to the index, so the same entry is displayed
#If the user reaches the last entry and scrolls to the next entry, they will be redirected to the first entry
#If the user reaches the first entry and scrolls backwards, they will be taken to entry #100
def scroll(index,data):
    print("\n\nDisplaying entry "+ str(index+1)+ " out of 100")
    print(json.dumps(data[index], indent=4))
    response=input("Press 'n' for next entry or 'b' for previous entry, or 'q' to exit, then press enter.")
    if response== 'q':
        return
    else:
        if index!=0 and index!=99:
            if response=='n':
                index+=1
                scroll(index,data)
            elif response=='b':
                index-=1
                scroll(index,data)
            else:
                print("Invalid Input")
                scroll(index,data)
        elif index==0:
            if response=='n':
                index+=1
                scroll(index,data)
            elif response=='b':
                index = 99
                scroll(index,data)
            else:
                print("Invalid Input")
                scroll(index,data)
        elif index==99:
            if response=='n':
                index=0
                scroll(index,data)
            elif response=='b':
                index-=1
                scroll(index,data)
            else:
                print("Invalid Input")
                scroll(index,data)




#The starting index is set to 0 before the scroll function is called.
index = 0
scroll(index, pizza_subset)
    
    

