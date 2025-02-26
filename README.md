# Regex-to-NFA-Validator
A Regular Expression validation engine that constructs Nondeterministic Finite Automata (NFA) from user-supplied Regular Expressions in postfix notation. Outputs the equivalent NFA for valid expressions and provides error messages for invalid ones.
README

1. Name and Email Address:
  - Name: Morgan Martin
  - Email: morgan.martin@wsu.edu

2. List of Files:
  - RE_to_NFA.py: Python script that converts a given regular expression in postfix notation to an NFA and prints the result.
  - README.txt: Documentation file containing information about the project, compile instructions, and run instructions.
  - test_input.txt: Test file with valid regular expressions on each line.
  - test_errors.txt: Test file containing BOTH valid regular expressions and errors.

3. Compiler/Interpreter Version:
  - Python 3.8 or higher

4. Compile Instructions:
  - Make sure Python 3.8 or higher is installed on the machine.
  - Make sure RE_to_NFA.py and input_file are in the same directory.

5. Run Instructions:
  - To run the program, use the following command:

     python3 RE_to_NFA.py <input_file>

     Replace <input_file> with the path to your input file containing postfix regular expressions, each on a new line.

  - Example(s):

     python3 RE_to_NFA.py test_input.txt
     python3 RE_to_NFA.py test_errors.txt
