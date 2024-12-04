if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        with open(f'{file_name.split(".")[0]}_list.csv', 'w') as output_file:
            lines = file.readlines()
            for line in lines:
                if "ftm_station" in line and "cm" in line:
                    output_file.write(line.split(", ")[1].split(" cm")[0] + ',\n')
