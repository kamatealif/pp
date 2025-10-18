import os
import sys

# Count of .java files found while walking the tree
file_count = 0


def print_tree(path: str, prefix: str = '') -> None:
    """Recursively print a directory tree using box-drawing characters.

    Directories are printed with a trailing slash. Files are printed
    normally. Updates the global file_count for files ending with .java.
    """
    global file_count

    try:
        entries = sorted(os.listdir(path))
    except OSError as e:
        print(prefix + f"[error opening {path}: {e}]")
        return

    # Sort directories first, then files, case-insensitively
    entries = sorted(entries, key=lambda n: (not os.path.isdir(os.path.join(path, n)), n.lower()))

    for idx, name in enumerate(entries):
        full = os.path.join(path, name)
        is_dir = os.path.isdir(full)
        is_last = idx == len(entries) - 1
        connector = '└── ' if is_last else '├── '

        if is_dir:
            print(prefix + connector + name + '/')
            extension = '    ' if is_last else '│   '
            print_tree(full, prefix + extension)
        else:
            print(prefix + connector + name)
            if name.endswith('.java'):
                file_count += 1


def main() -> None:
    # Allow an optional path argument; default to the project source folder
    path = sys.argv[1] if len(sys.argv) > 1 else 'java-program-bcae/src'

    if not os.path.exists(path):
        print(f"Path not found: {path}")
        sys.exit(1)

    print(path.rstrip('/') + '/')
    print_tree(path)
    print()
    print(f'Total .java files: {file_count}')


if __name__ == '__main__':
    main()
