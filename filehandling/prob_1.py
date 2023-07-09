file_paths = "G:\python\twinkle.txt"

f = open(file_paths, "rt")
content = f.read()
if "twinkle" in content:
    print("Twinkle is present")
else:
    print("Twinkle is not Present")
f.close()