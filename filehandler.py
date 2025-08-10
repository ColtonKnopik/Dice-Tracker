
def save_to_file(results, filename):
    try:
        with open(filename, "w") as file:
            num_sides = len(results)
            total_rolls = sum(results)

            file.write(f"sides: {num_sides}\n")
            file.write(f"total_rolls: {total_rolls}\n")

            for i, count in enumerate(results, start=1):
                file.write(f"{i}: {count}\n")

        return True

    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def load_file(filename):
    try:
        with open(filename, "r") as file:
            # Read number of sides
            sides_line = file.readline().strip()
            if not sides_line.startswith("sides:"):
                raise ValueError("Missing 'sides' line.")
            sides = int(sides_line.split(":")[1].strip())

            # Read total rolls
            rolls_line = file.readline().strip()
            if not rolls_line.startswith("total_rolls:"):
                raise ValueError("Missing 'total_rolls' line.")
            total_rolls = int(rolls_line.split(":")[1].strip())

            # Read individual counts
            results = []
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    count = int(parts[1].strip())
                    results.append(count)

            # Sanity check: do we have the right number of sides?
            if len(results) != sides:
                raise ValueError("Mismatch between declared sides and result count.")

            return results, sides, total_rolls

    except FileNotFoundError:
        print(f"File: {filename} does not exist.")
        return [], 0, 0

    except ValueError as e:
        print(f"File format is incorrect: {e}")
        return [], 0, 0
