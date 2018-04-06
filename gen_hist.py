import numpy as np
import matplotlib.pyplot as plt

from pyemd import emd
from hausdorff import hausdorff
from scipy.stats import entropy, norm, uniform


# Number of samples
N = 100

# Dimension of samples
n = 1


# pdf1 = norm(10, 5)
pdf2 = norm(20, 5)
# pdf3 = norm(100, 5)

pdf1 = uniform(10,5)
# pdf2 = uniform(40,5)
pdf3 = uniform(100,5)

points1 = np.rint(pdf1.rvs(size=N))
points2 = np.rint(pdf2.rvs(size=N))
points3 = np.rint(pdf3.rvs(size=N))




# Assumes 1D histograms
def distanceMetric(points1, points2):
    distance = np.zeros((points1.shape[0], points2.shape[0]))
    for i in range(points1.shape[0]):
        for j in range(points2.shape[0]):
            distance[i, j] = np.abs(points1[i] - points2[j])
    return distance

dist12 = distanceMetric(points1, points2)
dist13 = distanceMetric(points1, points3)
dist23 = distanceMetric(points2, points3)

# EMD
emd12 = emd(points1, points2, dist12)
emd13 = emd(points1, points3, dist13)
emd23 = emd(points2, points3, dist23)

print(emd12, emd13, emd23)

# Hausdorff
haus12 = hausdorff(points1.reshape((points1.shape[0], 1)), points2.reshape((points2.shape[0], 1)))
haus13 = hausdorff(points1.reshape((points1.shape[0], 1)), points3.reshape((points3.shape[0], 1)))
haus23 = hausdorff(points2.reshape((points2.shape[0], 1)), points3.reshape((points3.shape[0], 1)))

print(haus12, haus13, haus23)



# KL Divergence
x = np.linspace(1, 150, 150)
kl12 = entropy(pdf1.pdf(x), pdf2.pdf(x))
kl13 = entropy(pdf1.pdf(x), pdf3.pdf(x))
kl23 = entropy(pdf2.pdf(x), pdf3.pdf(x))

print(kl12, kl13, kl23)

# L1 Norm
l112 = np.sum(np.abs(np.subtract(pdf1.pdf(x), pdf2.pdf(x))))
l113 = np.sum(np.abs(np.subtract(pdf1.pdf(x), pdf3.pdf(x))))
l123 = np.sum(np.abs(np.subtract(pdf2.pdf(x), pdf3.pdf(x))))


print(l112, l113, l123)

fig = plt.figure()
ax = fig.add_subplot(311)
ax.hist(points1, range=(1,150), bins=150, color='red')
ax.hist(points2, range=(1,150), bins=150, color='green')
ax.text(110,8, "EMD=%.1f\nHausdorff=%.1f\nKL=%.1f\nL1=%.1f" % (emd12, haus12, kl12, l112))
ax.axis([0, 150, 0, 25])

ax = fig.add_subplot(312)
ax.hist(points1, range=(1,150), bins=150, color='red')
ax.hist(points3, range=(1,150), bins=150, color='blue')
ax.text(110,8, "EMD=%.1f\nHausdorff=%.1f\nKL=%.1f\nL1=%.1f" % (emd13, haus13, kl13, l113))
ax.axis([0, 150, 0, 25])

ax = fig.add_subplot(313)
ax.hist(points2, range=(1,150), bins=150, color='green')
ax.hist(points3, range=(1,150), bins=150, color='blue')
ax.text(110,8, "EMD=%.1f\nHausdorff=%.1f\nKL=%.1f\nL1=%.1f" % (emd23, haus23, kl23, l123))
ax.axis([0, 150, 0, 25])

plt.show()
