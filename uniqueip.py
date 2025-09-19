import re

pattern = r"\d+\.\d+\.\d+\.\d+"
with open("auth.log", "r") as f:
    text = f.read()

ips= re.findall(pattern, text)

# Convert to a set to remove duplicates
unique_ips = set(ips)

# Print each unique IP
print("Unique IPs:")
for ip in unique_ips:
    print(ip)

with open("unique_ips.txt", "w") as f:
    for ip in unique_ips:
        f.write(ip + "\n")

