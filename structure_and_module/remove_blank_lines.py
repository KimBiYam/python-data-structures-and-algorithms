import sys


def read_data(filename):
    lines = []
    file = None
    try:
        file = open(filename)
        for line in file:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if file is not None:
            file.close()
    return lines


def write_data(lines, filename):
    file = None
    try:
        file = open(filename, "w")
        for line in lines:
            file.write(line)
    except (EnvironmentError) as err:
        print(err)
    finally:
        if file is not None:
            file.close()


def remove_blank_lines():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [file ...]")

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == "__main__":
    remove_blank_lines()
