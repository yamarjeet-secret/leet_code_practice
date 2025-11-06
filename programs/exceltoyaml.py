# import pandas as pd
# import yaml

# # Step 1: Read the Excel file using pandas
# excel_file = "C:\\Users\\amarjeet\\Downloads\\Book1.csv"
# df = pd.read_excel(excel_file)

# # Step 2: Convert the data column-wise to a dictionary
# data_dict = {}
# for column in df.columns:
#     data_dict[column] = df[column].tolist()

# # Step 3: Convert the dictionary to YAML
# yaml_data = yaml.dump(data_dict)

# # Step 4: Save the YAML data to a file or print it
# with open("data.yaml", "w") as yaml_file:
#     yaml_file.write(yaml_data)
#     print("Data has been converted to YAML and saved as data.yaml")
    
    
    
    
import re
import yaml

# Sample input data
data = """
-
   Identifier: 1_var1_1_var1
   BIOS Knobs: dfxRankMaskEn:0x1,dfxRankMask_0:0x00,dfxRankMask_1:0x00,dfxRankMask_3:0x0F,dfxRankMask_4:0x00,dfxRankMask_6:0x00,dfxRankMask_7:0x00,dfxRankMask_9:0x00,dfxRankMask_10:0x00,dfxRankMask_12:0x00,dfxRankMask_13:0x00,dfxRankMask_15:0x0F,dfxRankMask_16:0x00,dfxRankMask_18:0x00,dfxRankMask_19:0x00,dfxRankMask_21:0x00,dfxRankMask_22:0x00
   Register check: 
"""

# Split the data into individual entries
entries = re.split(r'-\s+', data.strip())[1:]

# Initialize an empty result dictionary
result = {}

# Process each entry
for entry in entries:
    lines = entry.strip().split('\n')
    identifier = lines[0].strip().split(": ")[1]
    bios_knobs = lines[1].strip().split(": ")[1].split(',')
    
    bios_knobs_dict = {}
    for knob in bios_knobs:
        knob_name, knob_value = knob.split(':')
        bios_knobs_dict[knob_name.strip()] = knob_value.strip()
    
    register_check = lines[2].strip()
    
    result[identifier] = {
        "bios_knobs": bios_knobs_dict,
        "register_check": {
            "sv.sockets.uncore.cha.cha0.ms2idi0.snc_config": register_check
        }
    }

# Convert the result dictionary to YAML
yaml_data = yaml.dump(result, default_flow_style=False)

# Print the YAML data
print(yaml_data)

