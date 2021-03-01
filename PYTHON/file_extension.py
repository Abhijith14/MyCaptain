filename = input("Input the Filename:")
ext = filename[filename.find('.') + 1:]
ext_name = ""
if ext == "py":
    ext_name = "python"
elif ext == "txt":
    ext_name = "textfile"
else:
    ext_name = "NOT DEFINED !!"

print("The extension of the file is:'" + str(ext_name) + "'")
