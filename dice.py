import display
import filehandler as fh
import shlex

roll_count = 0
dice_sides = 0
results = []

def make_dice_list():
    while True:
        try:
            dice_sides = int(input("Enter Dice Number: "))
            break
        except ValueError:
            print("Must enter integer value.")

    results = [0] * dice_sides
    return results

def roll_dice(results):
    global roll_count
    while True:
        print("Press q or quit to exit")
        user_input = input(f"Roll {roll_count}: ")

        if user_input.lower() in ("q", "quit"):
            set_results(results)
            break

        try:
            roll = int(user_input)
            if 1 <= roll <= len(results):
                results[roll - 1] += 1
                roll_count += 1
            else:
                print(f"Roll must be between 1 and {len(results)}.")
        except ValueError:
            print("Must enter integer value.")


def execute_command(command, args):
    global results, roll_count, dice_sides
    match command:
        case "help":
            display.display_help()

        case "new":
            if len(args) >= 2:
                filename = args[0]
                try:
                    sides = int(args[1])
                    results = [0] * sides  
                    fh.save_to_file(results, filename)
                    print(f"Created new dice file with {sides} sides: {filename}")
                except ValueError:
                    print("Dice sides must be an integer.")
            else:
                print("Usage: new <filename> <dice sides>")

        case "save":
            if args:
                filename = args[0]
                fh.save_to_file(get_results(), filename)
                print(f"Saved to {filename}")
            else:
                print("Usage: save <filename>")

        case "load":
            if args:
                filename = args[0]
                results, dice_sides, roll_count = fh.load_file(filename)
                print(f"Loaded from {filename}")
            else:
                print("Usage: load <filename>")

        case "roll":
            print("Rolling the dice...")
            roll_dice(get_results())

        case "exit":
            print("Goodbye!")
            exit()

        case "results":
            results = get_results()

            if not args:
                # No flags given: show everything
                display.print_counts(results)
                display.print_percentages(results)
                display.get_percentage_graph(results)
                display.get_radar_chart(results)
                return

            for flag in args:
                match flag:
                    case "-c":
                        display.print_counts(results)
                    case "-p":
                        display.print_percentages(results)
                    case "-b":
                        display.get_percentage_graph(results)
                    case "-r":
                        display.get_radar_chart(results)
                    case _:
                        print(f"Unknown flag: {flag}")


        case _:
            print("Unknown command.")


def listen_for_command():
    while True:
        user_input = input().strip()
        if not user_input:
            continue

        parts = shlex.split(user_input)  # allows quoted filenames too
        command = parts[0]
        args = parts[1:]

        execute_command(command, args)

def get_results():
    global results
    return results

def set_results(new_results):
    global results
    results = new_results


def main():
    print("Welcome to DicePy! (type 'help' for command list)")

    while True:
        listen_for_command()


if __name__ == "__main__":
    main()