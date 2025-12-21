# Currency Converter Project

A simple, cross-platform currency and unit converter with a Tkinter GUI and modular backend converters.

This repository provides a desktop application that converts currency and many unit types (length, mass, temperature, time, volume, data units, binary, etc.). The app runs on Windows and Linux and uses Python 3 and Tkinter for the GUI.

**Project structure.**

- **`main.py`**: Primary entrypoint for launching the app.
- **`requirements.txt`**: Python dependency list.
- **`currency.json`**: Currency data used by the app.
- **`backend/`**: Backend API and converter implementations.
- **`frontend/`**: GUI frames, pages, and styles.

**Supported conversions**: currency, length, mass, temperature, time, volume, speed, area, data units, binary, numeral systems, discount calculations, and more.

**Compatibility**: Tested on Windows 10/11 and Ubuntu-based Linux. Should also work on other modern Linux distributions.

**Requirements.**

- **Python**: 3.8+ (Python 3.11 recommended).
- **Tkinter**: GUI toolkit (usually included with CPython, see Troubleshooting below).
- Install dependencies from `requirements.txt`.

**Installation (recommended: virtual environment).**

Linux / macOS (bash/zsh):

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows Command Prompt (cmd.exe):

```cmd
python -m venv venv
venv\\Scripts\\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you prefer not to use a virtual environment, you can install dependencies system-wide, but virtualenvs are recommended.

**Run the application.**

From the project root (virtualenv activated):

```bash
python main.py
```

This launches the Tkinter GUI. If you want to launch a particular module for development, you can run the GUI main directly:

```bash
python frontend/gui_main.py
```

**Headless / CLI usage.**

This project is primarily GUI-driven. If a CLI entrypoint exists (or you add one), run it similarly with `python <script>.py`.

**Development notes.**

- Code is split into `backend/` (conversion logic and API handler) and `frontend/` (UI frames and pages).
- Add new converters under `backend/converters/` and expose them through `backend/api_handler.py`.
- UI pages live under `frontend/pages/` and follow a consistent frame pattern.

**Troubleshooting.**

- Tkinter missing on Linux: install system package. On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3-tk
```

- Windows: Tkinter is included with standard CPython installers. If you get Tcl/Tk errors, ensure you installed the official Python installer from python.org and selected TCL/TK support.
- Permissions: On Linux, use `chmod +x` only for scripts you intend to execute directly. Running with `python main.py` avoids execute-bit issues.
- If `pip install -r requirements.txt` fails for packages with native extensions, install build tools first (e.g., `build-essential` on Debian/Ubuntu or Visual C++ Build Tools on Windows).

**Packaging (optional).**
To create a standalone executable, use `pyinstaller` (not included in requirements by default). Example:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

This creates a standalone binary in `dist/` suitable for distribution on the same OS. For cross-platform builds, build on each target OS.

**Contributing.**

- Fork the repo and open a pull request.
- Follow existing code style and add unit tests when possible.
- Update `README.md` and `docs/` with any API or behavior changes.

**License**
Specify your license here (e.g., MIT, Apache-2.0). If none, add one to the repository root in a `LICENSE` file.

**Contact / Further docs.**

- API and architecture docs are in the `docs/` folder (`docs/api_documentation.md`, `docs/architecture.md`).
- For questions or feature requests, open an issue in the repository.

---

If you'd like, I can also:

- add a short `CONTRIBUTING.md` template,
- create a simple CLI wrapper for headless conversions, or
- add packaging scripts for Windows and Linux.

Happy converting!
