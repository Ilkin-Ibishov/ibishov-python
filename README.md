# My Python UI App

This project is a simple interactive application built using Python and the Tkinter library for the user interface. The app allows users to:

- Enter a number: If the number is greater than 7, it prints "Hello".
- Enter a name: If the name is "John", it prints "Hello, John"; otherwise, it prints "There is no such name".
- Enter a list of numbers (space or comma separated): It prints all numbers that are multiples of 3.

## Requirements

- Python 3.7 or higher (Tkinter is included with standard Python distributions)

## Setup Instructions

1. Clone the repository:
   ```powershell
   git clone <repository-url>
   cd my-python-ui-app
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies (if any are listed in `requirements.txt`):
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

To start the application, run the following command from the project root:
```powershell
python src/main.py
```

This will open the main window. Enter your input in the field and click "Submit" to see the result below.

## Project Structure

```
my-python-ui-app/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── ui/
│   │   └── app_window.py
│   └── utils/
│       └── helpers.py
```

## Notes
- No additional dependencies are required for Tkinter.
- The UI is centered and minimal for ease of use.
- Only the number, name, and array logic is present


## My answer for the sequence question:
Given bracket sequence: [((())()(())]] 
Can this sequence be considered correct? 
If the answer to the previous question is “no”, then what needs to be changed in it to make it correct? 

My answers:
The given bracket sequence is not correct. It appears to be a sequence relates to First in Last out logic but the last out charachter must be the opposite (mirrored) of the First in character. For example:
First in --> "[ [ )"
Last out must be --> "( ] ]"
Full sequence --> "[ [ ) ( ] ]"

And for the given sequence: [((())()(())]]
The corrected sequence can be [[((())()(()))]] or [((())()(()))] or [(())()(())] or [[(())()(())]]# ibishov-python
