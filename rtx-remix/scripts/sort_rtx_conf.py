def sort_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines.sort()

    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    sort_file('./rtx.conf')
