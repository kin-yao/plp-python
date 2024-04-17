# opening and reading a file

file_path = "pdrugs.txt"

with open(file_path, 'r') as file:
    data = file.read()
    print(data)

# writing to a file
file_path = "pdrugs.txt"
data_to_write = "SpecialK."

with open(file_path, 'w') as file:
    file.write(data_to_write)


# Appending 

file_path = "pdrugs.txt"
data_to_append = """Heroin
Cocaine
Methamphetamine (Meth)
Crack Cocaine
MDMA (Ecstasy/Molly)
LSD (Acid)
PCP (Angel Dust)"""

with open(file_path, 'a') as file:
    file.write(data_to_append)

# Chehcking for file existance
import os

file_path = "pdrugs.txt"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")



# renaming operations:import os

old_file_path = "old_file.txt"
new_file_path = "new_file.txt"

os.rename(old_file_path, new_file_path)

