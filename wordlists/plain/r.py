lines = []
with open('english wordlist.txt', 'r') as f:
    for line in f.readlines():
        if '!' not in line:
            lines.append(line)

with open('english wordlist.txt', 'w') as f:
    for l in lines:
        f.write(l)