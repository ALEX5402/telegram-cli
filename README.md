# 🚀 Telegram CLI Tool

A simple and efficient command-line interface (CLI) tool for interacting with Telegram. This project is built using Python and packaged into a standalone executable using PyInstaller.

---

## 📋 Features

- 📤 Send text messages
- 📁 Send files with optional descriptions
- 🌐 Works with private chats, groups, and channels
- 🔒 Secure and lightweight executable

---

## 🛠️ Build Instructions

Follow these steps to build the project into a standalone executable:

### Prerequisites

1. 🐍 **Python 3.8+**
2. 📦 Required dependencies (install via `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```
3. 🛠️ **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

### Building the Executable

1. Clone the repository and navigate to the project directory.
2. Run the following command to build the executable:
   ```bash
   make
   ```

### Cleaning Up

To remove build artifacts and temporary files:
```bash
make clean
```

---

## 📦 Generated Executable

- The standalone executable will be located in the `dist` folder after the build process.
- Run the executable using:
  ```bash
  ./dist/telegram-cli
  ```

---

## 🔧 Usage

Here’s how to use the CLI tool:

### Sending a Text Message
```bash
./dist/telegram-cli -p <user_id> -t "Hello, this is a test message!"
```

### Sending a File with Description
```bash
./dist/telegram-cli -g <group_id> -F /path/to/file.txt -d "File description here."
```

### Available Options

| Option           | Description                       |
|------------------|-----------------------------------|
| `-p <user_id>`   | Send to a private user            |
| `-g <group_id>`  | Send to a group                  |
| `-c <channel_id>`| Send to a channel                |
| `-t <message>`   | Text message to send             |
| `-F <file>`      | File path to send                |
| `-d <description>`| Description for the file (optional)|

---

## 📂 File Structure

```plaintext
├── telegram-cli.py       # Main script
├── requirements.txt      # Dependencies
├── Makefile              # Build automation
├── dist/                 # Generated executables
└── README.md             # Project documentation
```

---

## 🌟 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests. 😊

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🤝 Acknowledgments

- Built with ❤️ using [Telethon](https://docs.telethon.dev/)
- Packaged with 🛠️ [PyInstaller](https://www.pyinstaller.org/)

---

## 🚀 Let's Build Together!

If you find this project helpful, please ⭐ it and share it with others! 💖
