import matplotlib.pyplot as plt
import random
import numpy as np


def plot_embeddings(a, labels_new, epoch, config):
    hexadecimal_alphabets = '0123456789ABCDEF'
    number_of_colors = 32
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in
                            range(6)]) for i in range(number_of_colors)]

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')
    for i in range(len(labels_new)):
        ax.scatter(a[i][0], a[i][1], a[i][2], c=color[labels_new[i]])
        ax.text(a[i][0], a[i][1], a[i][2], labels_new[i])
    plt.savefig('/projects/plots/exp'+str(config) +
                '/embeddings_'+str(epoch)+'.png')
    # plt.show()
    plt.close()


def plot_embeddings_2d(a, labels_new, epoch, config):
    hexadecimal_alphabets = '0123456789ABCDEF'
    number_of_colors = 32
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in
                            range(6)]) for i in range(number_of_colors)]

    plt.figure()

    for i in range(len(labels_new)):
        # print(a[i][0],a[i][1],color[labels_new[i]])
        plt.scatter(a[i][0], a[i][1], c=color[labels_new[i]])

    plt.xlim((np.min(a[:, 0])-0.1, np.max(a[:, 0])+0.1))
    plt.ylim((np.min(a[:, 1])-0.1, np.max(a[:, 1])+0.1))
    plt.text(a[i][0], a[i][1], a[i][2], labels_new[i])
    plt.savefig('/projects/plots/exp'+str(config) +
                '/embeddings_'+str(epoch)+'.png')

    plt.show()
    plt.close()
