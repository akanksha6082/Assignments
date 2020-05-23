hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
# taking input from user :
number = int(input("Enter the number of websites to be blocked!"))
website_list = []

for i in range(1, number + 1):
    website = input("Enter the site of url to block:")
    website_list.append(website)

# blocking of website:

with open(hosts_path, 'r+') as file:
    contents = file.read()
    for websites in website_list:
        if websites in contents:
            pass
            # Pass operation is the null operation where nothing runs or executes

        # if you want to add the website url to thew hosts file :
        else:
            file.write(redirect + " " + websites + "\n")

# unblocking code :
# while True:
#   with open(hosts_path,'r+') as file:
#      contents = file.readlines()
#        file.seek(0)
#        for line in contents:
#            if not any (websites in line for websites in website_list):
#                file.write(line)
#        file.truncate()
#
