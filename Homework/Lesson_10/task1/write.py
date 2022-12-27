def write(filename, text):
    with open(filename, 'w', encoding="UTF-8") as file:
        file.writelines(text)


if __name__ == "__main__":
    write('myfile.txt', "Hello file world!\n")
