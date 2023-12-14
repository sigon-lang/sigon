import matplotlib.pyplot as plt
# Plot the learning curves for loss


# without patience
# time = [round(17.8855438), round(34.82993748), round(15.84112307), round(20.2439233)]
# accs = [0.7570959577957789, 0.7902966290712357, 0.7487480094035467, 0.8185863643884659]

# with patience
# time = [25.15013253, 35.43919816, 14.21086239, 15,16063451]
# accs = [0.6734696750839552, 0.7540515065193176, 0.7734801123539606, 0.8236315349737803]

time = [6.032436538, 3.460548695, 1.724550847, 3.84118338]
accs = [0.9068255474170049, 0.8972180883089701, 0.7981593608856201, 0.9115890214840571]

plt.figure(figsize=(4, 4))
plt.plot("Only train", time[0], marker='o', linestyle='-', color='r')
plt.plot("Only fine tuning ", time[1], marker='x', linestyle='-', color='b')
plt.plot("Only feature extraction", time[2], marker='s', linestyle='-', color='y')
plt.plot("Sigon Agent", time[3], marker='+', linestyle='-', color='g')

# plt.title('Mean accuracy from the past 12 months')
plt.title('Time to retrain de CNN')
plt.xlabel('Approach')
plt.ylabel('Time (minutes)')


plt.grid(True)
plt.show()