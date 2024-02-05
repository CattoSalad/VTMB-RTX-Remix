import sys

def sort_texture_hashes(lines):
    processed_lines = []
    
    for line in lines:
        if '0x' in line:
            line_prefix, hash_values = line.split('=', 1)
            hash_values = hash_values.strip()

            unique_hashes = set(hash_values.split(', '))
            sorted_hashes = sorted(unique_hashes)
            processed_line = "{} = {}\n".format(line_prefix.strip(), ', '.join(sorted_hashes))
            processed_lines.append(processed_line)
        else:
            processed_lines.append(line)
    
    return processed_lines

def sort_lines(lines):
    sorted_lines = lines[:]
    sorted_lines.sort()

    return sorted_lines

def validate_unique_hashes(lines):
    all_hashes = set()

    for line in lines:
        if '0x' in line:
            _, hash_values = line.split('=', 1)
            hash_values = hash_values.strip()
            hashes_in_line = set(hash_values.split(', '))

            duplicates = all_hashes.intersection(hashes_in_line)
            if duplicates:
                return [False, f"Duplicate texture hashes found: {', '.join(duplicates)}"]

            all_hashes.update(hashes_in_line)
  
    return [True, "All texture hashes are unique"]


def validate_duplicated_keys(lines):
    seen_prefixes = set()
    for line in lines:
        if '=' not in line:
            continue

        prefix = line.split('=')[0].strip()
        if prefix in seen_prefixes:
            return [False, f"Duplicate key found: {prefix}"]
        seen_prefixes.add(prefix)

    return True, "All keys are unique"


def file_is_valid(lines):
    valid_texture_hashes, texture_message = validate_unique_hashes(lines)
    valid_keys, keys_message = validate_duplicated_keys(lines)

    if valid_texture_hashes and valid_keys:
        print(f"{texture_message}. {keys_message}.")
    else: 
        sys.exit(f"{texture_message}. {keys_message}.")

def sort_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sorted_lines = sort_lines(lines)
    sorted_lines_and_hashes = sort_texture_hashes(sorted_lines)

    file_is_valid(sorted_lines_and_hashes)

    with open(file_path, 'w') as file:
        file.writelines(sorted_lines_and_hashes)


if __name__ == "__main__":
    sort_file('./rtx.conf')
