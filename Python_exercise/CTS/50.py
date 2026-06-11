files = {"file1.txt", "file2.txt"}

backup = set()

for file in files:
    if file not in backup:
        backup.add(file)
        print(file, "copied")