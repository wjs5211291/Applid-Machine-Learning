from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

mat = np.array([[3.3, 0.9, 27.6, 0.9, 8.2, 19.1, 6.2, 26.6, 7.2],
                [9.2, 0.1, 21.8, 0.6, 8.3, 14.6, 6.5, 32.2, 7.1],
                [10.8, 0.8, 27.5, 0.9, 8.9, 16.8, 6.0, 22.6, 5.7],
                [6.7, 1.3, 35.8, 0.9, 7.3, 14.4, 5.0, 22.3, 6.1],
                [23.2, 1.0, 20.7, 1.3, 7.5, 16.8, 2.8, 20.8, 6.1],
                [15.9, 0.6, 27.6, 0.5, 10.0, 18.1, 1.6, 20.1, 5.7],
                [7.7, 3.1, 30.8, 0.8, 9.2, 18.5, 4.6, 19.2, 6.2],
                [6.3, 0.1, 22.5, 1.0, 9.9, 18.0, 6.8, 28.5, 6.8],
                [2.7, 1.4, 30.2, 1.4, 6.9, 16.9, 5.7, 28.3, 6.4],
                [12.7, 1.1, 30.2, 1.4, 9.0, 16.8, 4.9, 16.8, 7.0],
                [13.0, 0.4, 25.9, 1.3, 7.4, 14.7, 5.5, 24.3, 7.6],
                [41.4, 0.6, 17.6, 0.6, 8.1, 11.5, 2.4, 11.0, 6.7],
                [9.0, 0.5, 22.4, 0.8, 8.6, 16.9, 4.7, 27.6, 9.4],
                [27.8, 0.3, 24.5, 0.6, 8.4, 13.3, 2.7, 16.7, 5.7],
                [22.9, 0.8, 28.5, 0.7, 11.5, 9.7, 8.5, 11.8, 5.5],
                [6.1, 0.4, 25.9, 0.8, 7.2, 14.4, 6.0, 32.4, 6.8],
                [7.7, 0.2, 37.8, 0.8, 9.5, 17.5, 5.3, 15.4, 5.7],
                [66.8, 0.7, 7.9, 0.1, 2.8, 5.2, 1.1, 11.9, 3.2],
                [23.6, 1.9, 32.3, 0.6, 7.9, 8.0, 0.7, 18.2, 6.7],
                [16.5, 2.9, 35.5, 1.2, 8.7, 9.2, 0.9, 17.9, 7.0],
                [4.2, 2.9, 41.2, 1.3, 7.6, 11.2, 1.2, 22.1, 8.4],
                [21.7, 3.1, 29.6, 1.9, 8.2, 9.4, 0.9, 17.2, 8.0],
                [31.1, 2.5, 25.7, 0.9, 8.4, 7.5, 0.9, 16.1, 6.9],
                [34.7, 2.1, 30.1, 0.6, 8.7, 5.9, 1.3, 11.7, 5.0],
                [23.7, 1.4, 25.8, 0.6, 9.2, 6.1, 0.5, 23.6, 9.3],
                [48.7, 1.5, 16.8, 1.1, 4.9, 6.4, 11.3, 5.3, 4.0]])

plt.figure(1)
plt.plot()
plt.title("Agglomerative Clusterer Single")
dist_mat = mat
linkage_matrix_single = linkage(dist_mat,
                         "single")
print "linkage_single:"
print linkage_matrix_single
dendrogram(linkage_matrix_single,
           color_threshold=1,
           labels=['Belgium', 'Denmark', 'France', 'W. Germany', 'Ireland', 'Italy', 'Luxembourg', 'Netherlands',
                   'United Kingdom', 'Austria', 'Finland', 'Greece', 'Norway', 'Portugal'
               , 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Bulgaria', 'Czechoslovakia', 'E. Germany', 'Hungary',
                   'Poland', 'Rumania', 'USSR', 'Yugoslavia'],
           show_leaf_counts=True)


plt.figure(2)
plt.plot()
plt.title("Agglomerative Clusterer Complete")
dist_mat = mat
linkage_matrix_complete = linkage(dist_mat,
                         "complete")
print "linkage_complete:"
print linkage_matrix_complete
dendrogram(linkage_matrix_complete,
           color_threshold=1,
           labels=['Belgium', 'Denmark', 'France', 'W. Germany', 'Ireland', 'Italy', 'Luxembourg', 'Netherlands',
                   'United Kingdom', 'Austria', 'Finland', 'Greece', 'Norway', 'Portugal'
               , 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Bulgaria', 'Czechoslovakia', 'E. Germany', 'Hungary',
                   'Poland', 'Rumania', 'USSR', 'Yugoslavia'],
           show_leaf_counts=True)


plt.figure(3)
plt.plot()
plt.title("Agglomerative Clusterer Average")
dist_mat = mat
linkage_matrix_average = linkage(dist_mat,
                         "average")
print "linkage_average:"
print linkage_matrix_average
dendrogram(linkage_matrix_average,
           color_threshold=1,
           labels=['Belgium', 'Denmark', 'France', 'W. Germany', 'Ireland', 'Italy', 'Luxembourg', 'Netherlands',
                   'United Kingdom', 'Austria', 'Finland', 'Greece', 'Norway', 'Portugal'
               , 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Bulgaria', 'Czechoslovakia', 'E. Germany', 'Hungary',
                   'Poland', 'Rumania', 'USSR', 'Yugoslavia'],
           show_leaf_counts=True)

plt.show()