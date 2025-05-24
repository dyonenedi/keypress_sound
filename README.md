# 🎹 Keyboard Sound FX 🎧

![GitHub stars](https://img.shields.io/github/stars/dyonenedi/keypress_sound?style=social) ![GitHub forks](https://img.shields.io/github/forks/dyonenedi/keypress_sound?style=social)

**Transform your typing into a sound experience! This Python project adds customizable auditory feedback to every keystroke on your computer.**

## ✨ Features

* 🔊 **Auditory Feedback:** Plays a WAV sound (`relax_key.wav`) with every keystroke.
* 🖥️ **Windows Integration:** Runs discreetly in the system tray with a custom icon.
* 핫키 **Exit Hotkey:** Press `Shift + Esc` to close the application.
* 🛠️ **Buildable:** Easy instructions to generate a standalone `.exe` executable.
* 🤫 **No Console Window:** Operates in the background without intrusive console windows.
* 🔔 **Sound Notifications:** Beeps on application start and exit.

## 🚀 Getting Started

Follow these instructions to get Keyboard Sound FX up and running on your local environment.

### 📋 Prerequisites

* Python 3.7 or higher (installed and configured in PATH)
* PIP (Python package manager)

### 🛠️ Installation and Setup

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/dyonenedi/keypress_sound.git](https://github.com/dyonenedi/keypress_sound.git)
    cd keypress_sound
    ```
    Alternatively, download the project ZIP and extract the `keyboard_sound.py` and `relax_key.wav` files to a folder.

2.  **Install the dependencies:**
    You can install the dependencies directly via pip:
    ```bash
    pip install pygame keyboard pystray Pillow pyinstaller
    ```
    Or, create a file named `requirements.txt` in the project root with the following content:
    ```txt
    pygame>=2.0.0
    keyboard>=0.13.0
    pystray>=0.19.0
    Pillow>=8.0.0
    pyinstaller>=5.0.0
    ```
    And then, install from the file:
    ```bash
    pip install -r requirements.txt
    ```

## 📦 Building the Executable

To compile `keyboard_sound.py` into a single executable file (`.exe`) for Windows:

1.  **Ensure the `relax_key.wav` sound file is in the same folder** as the `keyboard_sound.py` script.
2.  Open your terminal or command prompt in the folder where the files are located.
3.  Run the following PyInstaller command:

    ```bash
    pyinstaller --onefile --add-data "relax_key.wav;." --hidden-import pystray --hidden-import PIL.Image --hidden-import PIL.ImageDraw --noconsole keyboard_sound.py
    ```

    * `--onefile`: Creates a single executable file.
    * `--add-data "relax_key.wav;."`: Includes the sound file in the executable.
    * `--hidden-import ...`: Ensures `pystray` and `Pillow` modules are included.
    * `--noconsole`: Prevents the console window from appearing when running the program.

    > ℹ️ **Note on Building:**
    > * PyInstaller usually detects `pygame` and `keyboard` automatically. If you encounter issues in the executable related to 'module not found' for `pygame` or `keyboard`, try adding them as `--hidden-import pygame` or `--hidden-import keyboard` as well.
    > * The main script name in the command is `keyboard_sound.py`. If your file has a different name, adjust the command accordingly.

4.  After the process completes, you will find the `keyboard_sound.exe` file inside a folder named `dist`.

## ▶️ Running the Application

1.  Navigate to the `dist` folder created by PyInstaller.
2.  Run the `keyboard_sound.exe` file.
3.  The application will start running in the background, and you will hear a sound with each keystroke. A keyboard icon will appear in the system tray.
4.  To exit the application, right-click the tray icon and select "Exit", or press `Shift + Esc`.

## 🎨 Customization

* **Key Sounds:** To change the sound, replace the `relax_key.wav` file with another `.wav` file of your choice, keeping the same name. Ensure the new file is in the same folder as the script (or the `.exe` after compilation, if not included with `--add-data` during a new build).

## 🤝 Contributing

Contributions are welcome! Feel free to open Issues or Pull Requests.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
(Suggestion: Create a `LICENSE` file in your repository with the text of the MIT license or another of your choice).

## 🗂️ Auto Init on Windows
1. Pressione `Win + R` para abrir o **Executar**.
2. Digite:
    
    ```
    shell:startup
    ```
    
3. e pressione **Enter**.
4. Isso abrirá a **pasta de inicialização** do seu usuário.
5. Copie o seu arquivo `.exe` (ou um atalho dele) para essa pasta

---

<p align="center">Made with ❤️ by Dyon Enedi with AI</p>
