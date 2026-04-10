#MapPlot.py
#Name: Miguel Alvarado
#Date: 4/9/2026
#Assignment: Lab 10

import matplotlib.pyplot as plt

trials = []
reaction_times = []

file = open("reaction_time_data.csv", "r")

file.readline()

for line in file:
    line = line.strip()
    parts = line.split(",")

    trial = int(parts[0])
    reaction_time = int(parts[1])

    if reaction_time > 0:
        trials.append(trial)
        reaction_times.append(reaction_time)

file.close()

plt.plot(trials, reaction_times)
plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Time between trials")
plt.savefig("reaction_time_graph.png")



