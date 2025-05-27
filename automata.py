class BinaryComplementFA:
    @staticmethod
    def ones_complement(binary: str) -> str:
        if not all(bit in '01' for bit in binary):
            raise ValueError("Input must contain only 0s and 1s")
            
        return ''.join(['1' if b == '0' else '0' for b in binary])

    @staticmethod
    def twos_complement(binary: str) -> str:
        if not all(bit in '01' for bit in binary):
            raise ValueError("Input must contain only 0s and 1s")
            
        result = []
        state = 'q0'  # Initial state
        
        for bit in reversed(binary):
            if state == 'q0':
                # State q0: Copy bits until first '1' is found
                result.append(bit)
                if bit == '1':
                    state = 'q1'  # Transition to flip state
            elif state == 'q1':
                # State q1: Flip all remaining bits
                result.append('1' if bit == '0' else '0')
        
        # Handle all zeros case (2's complement of 0 is 0)
        if state == 'q0':
            return binary
            
        return ''.join(reversed(result))

    @classmethod
    def visualize_automata(cls):
        print("\nFinite Automata Visualization:")
        print("1's Complement FA:")
        print("Single state automaton that flips each bit (0→1, 1→0)")
        
        print("\n2's Complement FA:")
        print("States:")
        print("q0: Haven't seen first '1' yet (copy bits)")
        print("q1: Seen first '1' (flip remaining bits)")
        print("\nTransitions:")
        print("q0 on 0 → q0, output 0")
        print("q0 on 1 → q1, output 1")
        print("q1 on 0 → q1, output 1")
        print("q1 on 1 → q1, output 0")

    @classmethod
    def interactive_demo(cls):
        print("Binary Complement Calculator")
        
        while True:
            print("\nChoice:")
            print("1. Calculate 1's complement")
            print("2. Calculate 2's complement")
            print("3. View automata diagrams")
            print("q. Quit")
            
            choice = input("\nEnter your choice (1-3/q): ").strip().lower()
            
            if choice == 'q':
                print("Exit")
                break
                
            if choice == '3':
                cls.visualize_automata()
                continue
                
            if choice not in ('1', '2'):
                print("Invalid choice. Please try again.")
                continue
                
            binary = input("Enter binary number: ").strip()
            
            try:
                if not all(bit in '01' for bit in binary):
                    raise ValueError("Input must contain only 0s and 1s")
                    
                print(f"\nOriginal: {binary}")
                
                if choice == '1':
                    print(f"1's complement: {cls.ones_complement(binary)}")
                elif choice == '2':
                    print(f"2's complement: {cls.twos_complement(binary)}")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    print("Running test cases...\n")
    
    test_cases = [
        ("1010", "0101", "0110"),
        ("1101", "0010", "0011"),
        ("0000", "1111", "0000"),
        ("1111", "0000", "0001"),
        ("1000", "0111", "1000")
    ]
    
    print("| Binary | 1's Comp | 2's Comp |")
    for binary, ones_expected, twos_expected in test_cases:
        ones_actual = BinaryComplementFA.ones_complement(binary)
        twos_actual = BinaryComplementFA.twos_complement(binary)
        print(f"| {binary:6} | {ones_actual:8} | {twos_actual:8} |")
        assert ones_actual == ones_expected
        assert twos_actual == twos_expected
    
    print("\nAll tests passed!")
    
    BinaryComplementFA.interactive_demo()