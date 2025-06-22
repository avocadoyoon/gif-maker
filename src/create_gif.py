import imageio.v3 as iio
filenames = ['welcome1.jpeg', 'welcome2.jpeg', 'welcome3.jpeg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('hi.gif', images, duration =900, loop= 0)