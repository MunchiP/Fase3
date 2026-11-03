
# Fase 3 - Compensandote

## Project Description

Desktop application developed in Python to manage affiliate
registrations for the family compensation fund "Compensandote".

The application implements object-oriented programming,
graphical user interfaces and three linear data structures:
Stack, Queue and List.

## Technologies

- Python 3
- Tkinter
- ttk.Treeview
- collections.deque
- list
- tkcalendar

## Project Structure

```text
Fase3PaulaAmaya/
|
|-- models/
|   |-- affiliate.py
|
|-- structures/
|   |-- affiliate_data_structure.py
|
|-- views/
|   |-- login_windows.py
|   |-- affiliate_window.py
|
|-- docs/
|   |-- abstraction_table.md
|
|-- main.py
|-- requirements.txt
|-- README.md
```

## Installation

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Create a virtual environment:

```powershell
py -m venv .venv
```

4. Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

## Execution

Run the following command:

```powershell
py main.py
```

## Login Credentials

Password: Caja

## Data Structures

### Stack

Uses collections.deque.

Operations:
- Push
- Pop

Report:
- Total membership fees.

### Queue

Uses collections.deque.

Operations:
- Enqueue
- Dequeue

Report:
- Number of affiliates.

### List

Uses Python list.

Operations:
- Add affiliate
- Search affiliate
- Remove affiliate

Report:
- Average current income.

## Storage

All affiliate information is stored in memory.
The application does not use databases or external
files to persist affiliate records.

## Author

Paula Amaya
