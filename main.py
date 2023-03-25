#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(r"Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

with open(r"Input/Names/invited_names.txt") as file:
    invited_names = file.read().splitlines()

ready_to_sent_folder = r"Output/ReadyToSend"

for name in invited_names:
    personalized_letter = letter_template.replace("[name]", name)
    output_file = f"{ready_to_sent_folder}\\{name}_letter.txt"

    with open(output_file, mode="w") as file:
        file.write(personalized_letter)

