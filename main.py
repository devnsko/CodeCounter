import os
import argparse
import pathspec
from colorama import Fore, Style, init

# Initialize colorama for color output in the console
init(autoreset=True)

def load_gitignore_patterns(gitignore_path, debug=False):
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            patterns = gitignore_file.read().splitlines()
        if debug:
            print(f"{Fore.CYAN}[DEBUG] Loaded patterns from .gitignore: {patterns}{Style.RESET_ALL}")
        return pathspec.PathSpec.from_lines('gitwildmatch', patterns)
    return None

def count_lines_of_code(directory, extensions, exclude_files=None, exclude_dirs=None, gitignore=None, debug=False):
    exclude_files = exclude_files or []
    exclude_dirs = exclude_dirs or []
    gitignore_spec = load_gitignore_patterns(gitignore, debug) if gitignore else None

    total_lines = 0
    file_count = 0
    skipped_files = 0

    print(f"{Fore.GREEN}Starting scan in directory: {directory}{Style.RESET_ALL}")

    for root, dirs, files in os.walk(directory):
        # Filtering directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs and
                   (not gitignore_spec or not gitignore_spec.match_file(os.path.join(root, d)))]

        for filename in files:
            filepath = os.path.join(root, filename)

            # Check exclusion criteria
            if filename in exclude_files or \
               (gitignore_spec and gitignore_spec.match_file(filepath)) or \
               not any(filename.endswith(ext) for ext in extensions):
                skipped_files += 1
                if debug:
                    print(f"{Fore.YELLOW}[DEBUG] Skipping file: {filename} (excluded or not matching extensions){Style.RESET_ALL}")
                continue

            # Count non-blank lines
            file_line_count = 0
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
                for line in infile:
                    if line.strip():  # Only count non-blank lines
                        total_lines += 1
                        file_line_count += 1

            # If file has code lines, include in count
            if file_line_count > 0:
                file_count += 1
                print(f"{Fore.BLUE}File: {filename} | Lines counted: {file_line_count}{Style.RESET_ALL}")

    # Print final summary
    print(f"\n{Fore.GREEN}--- Scan Complete ---{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total lines of code: {total_lines}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Files processed: {file_count}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Files skipped: {skipped_files}{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines of code in specified file types from a directory.")
    parser.add_argument('directory', nargs='?', default='.', help='The directory to scan. Defaults to the current directory.')
    parser.add_argument('-e', '--extensions', nargs='+', default=['.py', '.java', '.js', '.txt', '.md'], help='List of file extensions to include. Defaults to .py, .java, .js, .txt, and .md')
    parser.add_argument('-x', '--exclude-files', nargs='*', default=[], help='List of file names to exclude from counting.')
    parser.add_argument('-X', '--exclude-dirs', nargs='*', default=[], help='List of directory names to exclude from scanning.')
    parser.add_argument('-g', '--gitignore', action='store_true', help='Exclude files and directories listed in the .gitignore file.')
    parser.add_argument('--debug', action='store_true', help='Enable debug output to trace script execution.')

    args = parser.parse_args()

    exclude_dirs = [os.path.abspath(os.path.join(args.directory, d)) for d in args.exclude_dirs]
    scan_directory = os.path.abspath(args.directory)

    count_lines_of_code(
        scan_directory,
        args.extensions,
        args.exclude_files,
        exclude_dirs,
        gitignore=os.path.join(scan_directory, '.gitignore') if args.gitignore else None,
        debug=args.debug
    )
