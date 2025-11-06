import matplotlib.pyplot as plt
import random
def hiring_problem_simulation(n):
    candidates = list(range(1, n+1))
    random.shuffle(candidates)
    print("Interview Order (Ranks):", candidates)
    best_candidate = float('-inf')
    hires = 0
    hired_flags = []
    interview_steps = []
    for i, candidate in enumerate(candidates):
        step_info = f"Interviewing candidate {i+1} with rank: {candidate}"
        if candidate > best_candidate:
            best_candidate = candidate
            hires += 1
            hired_flags.append(1)
            step_info += " ---> Hired!"
        else:
            hired_flags.append(0)
        print(step_info)
        interview_steps.append(step_info)
    print(f"\nTotal number of hires: {hires}")
    return candidates, hired_flags, hires
def plot_hiring_simulation(candidates, hired_flags, total_hires):
    n = len(candidates)
    plt.figure(figsize=(12, 6))
    colors = ['green' if hire else 'blue' for hire in hired_flags]
    plt.bar(range(1, n+1), candidates, color=colors, alpha=0.7)
    for i, hire in enumerate(hired_flags):
        if hire:
            plt.text(i+1, candidates[i] + 0.5, 'Hired', ha='center')
    plt.title(f"Hiring Problem Simulation (Total Hires: {total_hires})")
    plt.xlabel("Interview Round")
    plt.ylabel("Candidate Rank (Higher is Better)")
    plt.xticks(range(1, n+1))
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
n = 20
candidates, hired_flags, total_hires = hiring_problem_simulation(n)
plot_hiring_simulation(candidates, hired_flags, total_hires)
