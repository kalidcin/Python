fh = open("mbox-short.txt", "r") # Ruta

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")