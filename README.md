
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

## Easy-to-Use Shortcuts for Windows, macOS, and Linux

For quick access to the script from any location, you can set up a shortcut.

#### Windows

1. Create a `counter.bat` file in the root directory with the following contents:

   ```bat
   @echo off
   call C:\Path\To\CodeCounter\.venv\Scripts\activate  # Update this path
   python C:\Path\To\CodeCounter\main.py %*  # Update this path
   deactivate
   ```

2. Add the directory containing `counter.bat` to your system PATH:
   - Go to **Control Panel** > **System and Security** > **System** > **Advanced system settings** > **Environment Variables**.
   - Under **System variables**, find the **Path** variable, and add the path to the directory containing `counter.bat`.

You can now use the script from any directory with the command:
```bash
counter [options]
```

#### Linux / macOS

1. Create a shortcut script `counter` in `/usr/local/bin` or another directory in your PATH:

   ```bash
   #!/bin/bash
   source /path/to/CodeCounter/.venv/bin/activate  # Update this path
   python /path/to/CodeCounter/main.py "$@"  # Update this path
   deactivate
   ```

2. Make the script executable and ensure it’s in your PATH:

   ```bash
   chmod +x /usr/local/bin/counter
   ```

You can now use the command in the terminal:
```bash
counter [options]
```

## Usage

The basic usage format is as follows:
```bash
counter [directory] [-e EXTENSIONS] [-x EXCLUDE_FILES] [-X EXCLUDE_DIRS] [-g] [--debug]
```

### Example Commands
- **Basic Counting**:
  ```bash
  counter src
  ```
- **With Specific Extensions** (e.g., `.py` and `.js`):
  ```bash
  counter src -e .py .js
  ```
- **Using .gitignore Exclusions**:
  ```bash
  counter src -g
  ```
- **Enable Debug Mode**:
  ```bash
  counter src --debug
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
