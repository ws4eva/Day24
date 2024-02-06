#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

template_path = "Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
name_list_path = "Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
ready_to_send_path = "Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/"

letter_list = []
with open(template_path) as file:
    contents = file.read()
#print(contents)


with open(name_list_path) as file:
    name_list = file.readlines()
#print(name_list)


for name in name_list:
    name = name.replace("\n", "")
    letter = contents.replace("[name]", name)
    letter_list.append(letter)
    
    new_file_name = f"Letter for {name}.txt"
    with open(ready_to_send_path + new_file_name, mode = "w") as file:
        file.write(letter)
#print(letter_list)
