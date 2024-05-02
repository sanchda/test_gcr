import sys

def parse_maps_file(pid):
    try:
        with open(f"/proc/{pid}/maps", "r") as file:
            memory_map = {}
            for line in file:
                parts = line.split()
                # Address range is in the first column, memory object (if present) is last
                if len(parts) > 5:
                    address_range = parts[0]
                    object_file = parts[-1]
                    # Skip anonymous maps
                    if object_file.startswith("["):
                        continue
                    # Calculate memory mapped for this range
                    start, end = address_range.split('-')
                    start, end = int(start, 16), int(end, 16)
                    size = end - start
                    if object_file in memory_map:
                        memory_map[object_file] += size
                    else:
                        memory_map[object_file] = size
            return memory_map
    except FileNotFoundError:
        print("Process ID does not exist or maps file is not accessible.")
        return {}

def print_memory_map(memory_map):
    for obj, size in sorted(memory_map.items(), key=lambda item: item[1], reverse=True):
        print(f"{size}    {obj}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mem_map.py [PID]")
        sys.exit(1)
    
    pid = sys.argv[1]
    memory_map = parse_maps_file(pid)
    print_memory_map(memory_map)
