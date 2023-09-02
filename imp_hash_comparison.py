import os
import pefile
import sys

def calculate_imphash(file_path):
    try:
        pe = pefile.PE(file_path)
        return pe.get_imphash()
    except Exception as e:
        print("Error processing {0}: {1}".format(file_path, e))
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 compare_hashes.py MalwareFolderPath")
        sys.exit(1)

    malware_folder = sys.argv[1]
    
    if not os.path.exists(malware_folder):
        print("Error: The folder '{0}' does not exist.".format(0))
        sys.exit(1)

    hash_dict = {}

    for root, dirs, files in os.walk(malware_folder):
        for file in files:
            file_path = os.path.join(root, file)
            imphash = calculate_imphash(file_path)
            if imphash is not None:
                hash_dict[file] = imphash

    #Comparing the hashes
    for file1, hash1 in hash_dict.items():
        for file2, hash2 in hash_dict.items():
            if file1 != file2:
                if hash1 == hash2:
                    print("Hash Comparison: {0} and {1} have the same imphash {2}".format(file1, file2, hash1))

if __name__ == "__main__":
    main()
