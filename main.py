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

