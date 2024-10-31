
# Code Counter

A lightweight Python script that scans directories for source code files, counts lines of code (ignoring blank lines), and displays a comprehensive summary in the console. It also supports excluding files and directories, and can respect `.gitignore` rules for a streamlined counting process.

## Features
- **Counts lines of code** while ignoring blank lines.
- **Supports `.gitignore`** to exclude files and directories listed within it.
- **File type filtering** with customizable file extensions.
- **Exclusion options** for specific files and directories.
- **Debug mode** to track execution details in the console.
- **User-friendly console output** with color-coded messages and progress updates.

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/devnsko/CodeCounter.git
cd CodeCounter
```

### 2. Set Up a Virtual Environment
Navigate to the project directory and create a virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment:
- **Windows**: `.\.venv\Scripts\activate`
- **macOS/Linux**: `source .venv/bin/activate`

### 3. Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The basic usage format is as follows:
```bash
python main.py [directory] [-e EXTENSIONS] [-x EXCLUDE_FILES] [-X EXCLUDE_DIRS] [-g] [--debug]
```

### Example Commands
- **Basic Counting**:
  ```bash
  python main.py src
  ```
- **With Specific Extensions** (e.g., `.py` and `.js`):
  ```bash
  python main.py src -e .py .js
  ```
- **Using .gitignore Exclusions**:
  ```bash
  python main.py src -g
  ```
- **Enable Debug Mode**:
  ```bash
  python main.py src --debug
  ```

## Easy-to-Use Shortcuts for Windows, macOS, and Linux

### Windows Setup with `counter.bat`
1. Create a `counter.bat` file in the project directory:
   ```bat
   @echo off
   call .venv\Scripts\activate
   python %~dp0\main.py %*
   ```
2. Add the project directory to your system PATH:
   - Go to **System Properties > Environment Variables**.
   - Find the **Path** variable, click **Edit**, and add the path to your project directory.
3. Now, you can run the script from anywhere in the command prompt:
   ```bash
   counter C:\pat\to\your\directory -e .py .js -g --debug
   ```

### macOS and Linux Setup with `counter.sh`
1. Create a `counter.sh` file in the project directory:
   ```bash
   #!/bin/bash
   source .venv/bin/activate
   python "$(dirname "$0")/main.py" "$@"
   ```
2. Make the script executable:
   ```bash
   chmod +x counter.sh
   ```
3. Add the project directory to your PATH. Open `~/.bashrc` (or `~/.zshrc` for Zsh users) and add:
   ```bash
   export PATH="$PATH:/path/to/your/project"
   ```
4. Reload the terminal or source your shell configuration:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```
5. You can now run the script from any directory:
   ```bash
   counter.sh /path/to/your/directory -e .py .js -g --debug
   ```

## Arguments and Options

| Argument           | Description                                                                                       |
|--------------------|---------------------------------------------------------------------------------------------------|
| `directory`        | The directory to scan for code files. Defaults to the current directory (`.`).                    |
| `-e, --extensions` | List of file extensions to include (e.g., `.py`, `.java`). Defaults to common code file types.    |
| `-x, --exclude-files` | List of file names to exclude from counting.                                                   |
| `-X, --exclude-dirs` | List of directories to exclude from scanning.                                                   |
| `-g, --gitignore`  | Exclude files and directories listed in the `.gitignore` file of the directory being scanned.     |
| `--debug`          | Enable debug output to display skipped files and detailed processing information.                 |

## Example Output

Here’s an example of the script’s output in the console:
```
Starting scan in directory: src
File: app.py | Lines counted: 150
File: utils.py | Lines counted: 45
File: config.py | Lines counted: 20

--- Scan Complete ---
Total lines of code: 215
Files processed: 3
Files skipped: 1
```

## Contributing
Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest new features.

## License
This project is licensed under the MIT License.
