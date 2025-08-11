try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def print_counts(results):
    for i, count in enumerate(results, start=1):
        print(f"{i}: {count}")

def print_percentages(results):
    total_rolls = sum(results)
    for i, count in enumerate(results, start=1):
        if total_rolls > 0:
            percent = (count / total_rolls) * 100
            print(f"{i}: {percent:.2f}%")
        else:
            print(f"{i}: 0.00%")

def get_percentage_graph(results):
    if not HAS_MATPLOTLIB:
        print("Matplotlib is not installed. Graphing is disabled.")
        return

    total_rolls = sum(results)
    if total_rolls == 0:
        print("No rolls to graph.")
        return
    percentages = [(count / total_rolls) * 100 for count in results]
    x = list(range(1, len(results) + 1))
    
    plt.bar(x, percentages, color='skyblue')  # <-- changed from plot() to bar()
    plt.title("Dice Roll Percentages")
    plt.xlabel("Die Value")
    plt.ylabel("Percentage (%)")
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

import numpy as np

def get_radar_chart(results):
    if not HAS_MATPLOTLIB:
        print("Matplotlib is not installed. Graphing is disabled.")
        return

    total_rolls = sum(results)
    if total_rolls == 0:
        print("No rolls to graph.")
        return

    percentages = [(count / total_rolls) * 100 for count in results]
    labels = [str(i + 1) for i in range(len(results))]

    values = percentages + [percentages[0]]
    angles = np.linspace(0, 2 * np.pi, len(percentages), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("Dice Roll Percentages (Radar Chart)", y=1.1)
    ax.set_yticklabels([])
    plt.show()

def display_help():
    print("----------+ Command List +----------")
    print("help                     Show this help menu")
    print("new <filename> <sides>  Create new dice file with given number of sides")
    print("save <filename>         Save current results to the given file")
    print("load <filename>         Load results from the given file")
    print("roll                    Begin submitting dice rolls")
    print("results                 Show all result info (counts, percentages, graphs)")
    print("results -c              Show raw roll counts")
    print("results -p              Show percentage breakdown")
    print("results -b              Show bar graph of results")
    print("results -r              Show radar chart of results")
    print("exit                    Exit the program")
    print("------------------------------------")

