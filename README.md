# Assignment 2 - Formal Languages

## Names
Isabel Acevedo Acosta
Sara Castrillón Sánchez    

## Class
SI2002-2 (7309) – Wednesday class

## Environment

- **Operating System:** Intel Core i7 (Windows 11)
- **Programming Language:** Python 3.x
- **Tools Used:**
  - Visual Studio Code
  - Python 3 interpreter

---

## Project Structure

### Algorithm 1 – Generate Valid and Invalid Strings

**Purpose:**  
Generate at least 2 valid strings and 2 invalid strings using the alphabet `{a, b}`.

- **Valid strings** follow the grammar rule (e.g., `ab`, `aabb`, `aaabbb`).
- **Invalid strings** use the same letters but break the structure (e.g., `aab`, `bab`).

**What it does:**  
- Creates a `.txt` file (`ALGORITHM_1_LFCO_2025_IAA_SC.txt`) with the generated strings.
- Includes a mutation function to create variations of valid and invalid strings.

---

### Algorithm 2 – PDA Simulator

**Purpose:**  
Implement a Push Down Automaton (PDA) that recognizes the language defined by the grammar.

**What it does:**
- Reads the strings from the `.txt` file created in Algorithm 1.
- Simulates the behavior of a PDA:
  - Pushes a symbol for each `'a'`
  - Pops for each `'b'`
  - Accepts the string if the stack is empty at the end
- Prints whether each string is accepted or rejected.

---

### Algorithm 3 – Leftmost Derivation Tree

**Purpose:**  
Build the **leftmost derivation tree** for strings that are **accepted by the PDA**.

**What it does:**
- Uses only strings accepted by Algorithm 2.
- Applies the grammar rules step by step:
  - `S → aSb` (repeated)
  - `S → ε` (final step)
- Prints each derivation step to reconstruct the original string.


##  How to Execute the Code

> Make sure Python 3 is installed and you're working in the project folder.

### 1. Run Algorithm 1

Generates the strings and saves them in a text file.

python ALGORITHM_1_LFCO_2025_IAA_SC.py
You will get a file named:
ALGORITHM_1_LFCO_2025_IAA_SC.txt

### 2. Run Algorithm 2
Reads the strings from the file and simulates the PDA.
python ALGORITHM_2_LFCO_2025_IAA_SC.py
 Example output:
 aabb → Accepted by PDA
aab → Rejected by PDA

### Run Algorithm 3
Prints the leftmost derivation steps for valid strings.
python ALGORITHM_3_LFCO_2025_IAA_SC.py
Example output:
String: aaabbb
  → S
  → aSb
  → aaSbb
  → aaaSbbb
  → aaabbb

### Notes:
All three algorithms use the same grammar: S → aSb | ε

The .txt file from Algorithm 1 is required for Algorithms 2 and 3.

No external libraries are needed.

### References: 
Kozen, Dexter C. (1997). Automata and Computability. 1st ed.