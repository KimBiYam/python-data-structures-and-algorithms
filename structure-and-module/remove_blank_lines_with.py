
import sys


def read_data(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            if line.strip():
                lines.append(line)
    return lines


def write_data(lines, filename):
    file = None
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)


def remove_blank_lines():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [file ...]")

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == "__main__":
    remove_blank_lines()
