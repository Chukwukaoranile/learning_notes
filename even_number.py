def read_even_numbered_lines():
    even_lines = []
    try:
        with open('even_number.txt', 'r') as file:
            # Enumerate over the lines to keep track of the line numbers (starting from 1)
            for line_number, line in enumerate(file, 1):
                # Check if the line number is even (2, 4, 6, etc.)
                if line_number % 2 == 0:
                    even_lines.append(line.strip())

        print(even_lines)
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except Exception as e:
        print("Error occurred while reading the file:", e)
        return []

read_even_numbered_lines()
