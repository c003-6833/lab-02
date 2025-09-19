import re

pattern = r"\d+\.\d+\.\d+\.\d+"
with open("auth.log", "r") as f:
    text = f.read()

found_ips= re.findall(pattern, text)

ips = []     # creates an empty list called ips
for ip in found_ips:
        ips.append(ip) # Add each ip to our list

        
print(found_ips)