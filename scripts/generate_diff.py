def parse_hashes(line):
    key, hashes = line.split('=', 1)
    return key.strip(), set(hashes.strip().split(', '))

def compare_hashes(old_hashes, new_hashes):
    added = new_hashes - old_hashes
    removed = old_hashes - new_hashes
    return added, removed

def process_file(file_path):
    with open(file_path, 'r') as file:
        return dict(parse_hashes(line) for line in file if '0x' in line)

def generate_diff(old_file, new_file):
    old_data = process_file(old_file)
    new_data = process_file(new_file)
    result = ""

    for key in new_data.keys():
        if key in old_data:
            added, removed = compare_hashes(old_data[key], new_data[key])
            if added or removed:
                result += (f"Changes in {key}: ")
                if added:
                    result += (f"  Added: {', '.join(added)}  ")
                if removed:
                    result += (f"  Removed: {', '.join(removed)}  ")
        else:
            print(f"New key in {new_file}: {key}  ")

    print(result)

if __name__ == "__main__":
    generate_diff('old_rtx.conf', 'rtx.conf')
