class State:
    def __init__(self, id):
        self.id = id
        self.transitions = []  # List of (symbol, target state)


class NFA:
    def __init__(self, start_state, accept_state):
        self.start_state = start_state
        self.accept_state = accept_state


def re_to_nfa(postfix_re):
    stack = []
    state_counter = [0]  # Use list to keep state counter mutable

    def create_state():
        state_counter[0] += 1
        return State(state_counter[0])

    for char in postfix_re:
        if char in "abcde":  # Symbols in the alphabet
            # Rule 1: Create an NFA for a single symbol
            start = create_state()
            accept = create_state()
            start.transitions.append((char, accept))
            stack.append(NFA(start, accept))
        elif char == 'E':  # Epsilon
            # Rule 1: Create an NFA for epsilon
            start = create_state()
            accept = create_state()
            start.transitions.append(('E', accept))
            stack.append(NFA(start, accept))
        elif char == '|':  # Union
            # Rule 2: Construct NFA for R1 | R2
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = create_state()
            accept = create_state()
            start.transitions.append(('E', nfa1.start_state))
            start.transitions.append(('E', nfa2.start_state))
            nfa1.accept_state.transitions.append(('E', accept))
            nfa2.accept_state.transitions.append(('E', accept))
            stack.append(NFA(start, accept))
        elif char == '&':  # Concatenation
            # Rule 3: Construct NFA for R1 & R2
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept_state.transitions.append(('E', nfa2.start_state))
            stack.append(NFA(nfa1.start_state, nfa2.accept_state))
        elif char == '*':  # Kleene star
            # Rule 4: Construct NFA for R*
            nfa = stack.pop()
            start = create_state()
            start.transitions.append(('E', nfa.start_state))
            nfa.accept_state.transitions.append(('E', start))
            stack.append(NFA(start, start))
        else:
            print(f"Error: Invalid character in postfix regular expression: {char}\n")
            return None

    if len(stack) != 1:
        print(f"Error: Invalid postfix regular expression.\n")
        return None

    return stack.pop()


def print_nfa(nfa):
    if nfa is None:
        return

    # Assign unique IDs to all states for easier printing
    state_id_map = {}

    def assign_state_ids(state):
        if state not in state_id_map:
            state_id_map[state] = f'q{state.id}'
            for _, next_state in state.transitions:
                assign_state_ids(next_state)

    assign_state_ids(nfa.start_state)

    # Print states
    print(f"Start: {state_id_map[nfa.start_state]}")
    print(f"Accept: {state_id_map[nfa.accept_state]}")

    # Collect transitions and print them
    visited = set()
    transitions = []
    stack = [nfa.start_state]

    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        for symbol, next_state in state.transitions:
            transitions.append((state_id_map[state], symbol, state_id_map[next_state]))
            stack.append(next_state)

    # Sorting function
    def transition_key(transition):
        start, symbol, end = transition
        return (int(start[1:]), symbol, int(end[1:]))

    transitions.sort(key=transition_key)
    for start, symbol, end in transitions:
        print(f"({start}, {symbol}) → {end}")
    print()  # Print a newline after each NFA


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 RE_to_NFA.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            print(f"RE: {line}")
            nfa = re_to_nfa(line)
            if nfa:
                print_nfa(nfa)