try:
    def createFile(name, content):
        with open(name+".txt", "w") as f:
            f.write(content)
except Exception as e:
    print("Error creating file, exception:", e)
