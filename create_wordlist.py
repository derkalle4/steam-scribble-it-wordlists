import sys
import glob

def concatenate_files(prefix):
    files = glob.glob(f"{prefix}_*.txt")
    if not files:
        print("No files found with the given prefix.")
        return

    file_contents = [open(file, encoding='utf-8').readlines() for file in files]
    max_lines = max(len(content) for content in file_contents)

    with open(f"output_{prefix}.txt", "w", encoding='utf-8') as output_file:
        for i in range(max_lines):
            line_parts = []
            for content in file_contents:
                if i < len(content):
                    line_parts.append(content[i].strip())
                else:
                    line_parts.append("")
            output_file.write("\t".join(line_parts) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_wordlist.py <prefix>")
    else:
        concatenate_files(sys.argv[1])