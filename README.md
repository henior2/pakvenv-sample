# pakenv
A simple template for a Python program with a virtual environment (`venv`).

## Features
- Nice for low-end servers
- Lightweight
- Straightforward

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/henior2/pakenv.git --depth 1 PROJECT_NAME_HERE
   ```
2. Place your Python code in the `src` directory, with `main.py` as the entry point.
3. Edit `requirements.txt` to include the packages you need.
4. Write the code you want to execute during setup in `src/_setup.py`. You can access the `venv` packages from there.
5. Setup the virtual environment:
   ```sh
   python3 setup.py
   ```
6. Execute the program:
   ```sh
   python3 start.py
   ```