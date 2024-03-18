# pakenv
A simple template for a Python program with a virtual environment (`venv`).

## Features
- Nice for low-end servers
- Lightweight
- Straightforward

## Usage
1. Clone the repository.
2. Place your Python code in the `src` directory, with `main.py` as the entry point.
3. Edit `requirements.txt` to include the packages you need.
4. Write the code you want to execute during setup in `src/_setup.py`. You can access the `venv` packages from there.
5. Run `python3 setup.py` to create the virtual environment and install the packages.
6. Run `python3 start.py` to execute your code.