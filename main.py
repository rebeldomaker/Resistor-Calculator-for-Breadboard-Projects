 
import readline

# Color code dictionaries
color_codes = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9,
    "gold": -1, "silver": -2  # Use -1 and -2 to represent non-numeric multipliers
}

multiplier = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000, "gray": 100000000,
    "white": 1000000000, "gold": 0.1, "silver": 0.01
}

tolerances = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1,
    "gray": 0.05, "gold": 5, "silver": 10, "none": 20
}

# Function to complete input colors using readline
def complete_colors(text, state):
    options = [color for color in color_codes if color.startswith(text)]
    return options[state] if state < len(options) else None

# Setup readline to use the completion function
def setup_readline():
    readline.set_completer(complete_colors)
    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims(' \t\n;')

# Function to format the resistance value more readably
def format_resistance(value):
    if value >= 1_000_000:
        return f"{value // 1_000_000}M"
    elif value >= 1000:
        return f"{value // 1000}k"
    else:
        return f"{value} ohms"

# Calculate the resistance based on color bands
def calculate_resistance(colors):
    if len(colors) not in [3, 4]:  # Handling 3 or 4 bands only for simplicity
        return "Error: Incorrect number of color bands."
    value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * multiplier[colors[2]]
    formatted_value = format_resistance(value)
    if len(colors) == 4:
        tolerance = tolerances[colors[3]]
        formatted_tolerance = f"±{tolerance}%"
    else:
        tolerance = 20  # Default tolerance when no tolerance band is given
        formatted_tolerance = "±20%"
    return f"{formatted_value} {formatted_tolerance}"

def main():
    setup_readline()
    while True:
        input_colors = input("Enter the resistor colors separated by spaces (or type 'exit' to quit): ").lower().strip()
        if input_colors == 'exit':
            break
        colors = input_colors.split()
        result = calculate_resistance(colors)
        print(result)

if __name__ == "__main__":
    main()
