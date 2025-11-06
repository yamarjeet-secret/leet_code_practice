# # STEP 1  : Save your excel file as CSV

# ctr = 0
# excel_filename = "C:\\Users\\amarjeet\\Downloads\\Book1.csv"
# yaml_filename = excel_filename.replace('csv', 'yaml')
# users = {}

# with open(excel_filename, "r") as excel_csv:
#     for line in excel_csv:
#         if ctr == 0:
#             ctr+=1  # Skip the coumn header
#         else:
#             # save the csv as a dictionary
#             user,name,uid,shell = line.replace(' ','').strip().split(',')
#             users[user] = {'name': name, 'uid': uid, 'shell': shell}



# with open(yaml_filename, "w+") as yf :
#     yf.write("users: \n")
#     for u in users:
#         yf.write(f"  {u} : \n")
#         for k,v in users[u].items():
#             yf.write(f"    {k} : {v}\n")


# lst = [0x0, 0x1]
# cmd = [hex(i).replace('L', '') for i in lst]
# print(cmd)

cmd = ''
lst_cmd = ['ipmitool', '-H', '10.45.140.135', '-U', 'debuguser', '-P', '0penBmc1', '-I', 'lanplus', '-C', '17', 'raw', '0x0', '0x1']
# for st in lst_cmd:
#     cmd = cmd +" "+ st
    
cmd = [cmd + " " + st for st in lst_cmd]
    
print(cmd)