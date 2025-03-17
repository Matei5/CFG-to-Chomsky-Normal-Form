# CFG to CNF Converter

## Contents
- Overview
- Files
- How It Works
- Usage
- Example Execution
- Notes
- License

## Overview
This project converts a given **Context-Free Grammar (CFG)** into **Chomsky Normal Form (CNF)**. The implementation reads a grammar from an input file and processes it to ensure it adheres to CNF rules. The program is written in Python and automates the necessary transformations to achieve a valid CNF representation.

## Files
### 1. `CFG_to_CNF.py`
- Reads a CFG from `in.txt`.
- Processes the grammar to convert it into CNF.
- Outputs the transformed grammar to the console.

### 2. `in.txt`
- Contains the CFG rules in the format: `NonTerminal -> Production | Production`
- Example input:
  ```
  S -> ABCD
  ```

## How It Works
1. **Reads and Parses the CFG**
   - The program reads rules from `in.txt`, identifying terminals and non-terminals.
   - Splits productions into separate alternatives.

2. **Ensures CNF Compliance**
   - Introduces a new start symbol `S0` to avoid indirect recursion.
   - Converts terminals in mixed rules into separate non-terminals.
   - Reduces rules with more than two non-terminals.
   - Removes unnecessary rules and cycles.

3. **Outputs the CNF Grammar**
   - The transformed rules are printed to the console in CNF format.

## Usage
### Running the Program
To execute the conversion script, use:
```bash
python CFG_to_CNF.py
```

### Input Format
- Each production rule follows the format:
  ```
  A -> B C | a
  ```
- The program reads this format from `in.txt`.

### Example Execution
#### Input (`in.txt`):
```
S -> ABCD
```
#### Output:
```
S0 -> S
S -> A S1
S1 -> B S2
S2 -> C D
```

## Notes
- The script assumes a properly formatted CFG in `in.txt`.
- It does not handle ambiguous or inherently non-CNF grammars.
- Supports grammars with single terminals, multiple productions, and chained non-terminals.

## License
This project is free to use and modify for educational purposes.

