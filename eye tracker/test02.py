import matplotlib.pyplot as plt
import matplotlib.image as mping

image = mping.imread('demo.jpg')
implot = plt.imshow(image)
plt.show()