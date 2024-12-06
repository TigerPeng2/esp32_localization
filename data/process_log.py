if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        with open(f'{file_name.split(".")[0]}.csv', 'w') as output_file:
            lines = file.readlines()
            for line in lines:
                if "Tuple" in line:
                    output_file.write(line.split(":")[2].split("")[0] + "\n")
