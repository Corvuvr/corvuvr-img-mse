from matplotlib.image import imread
png_res  = imread('res.png')
print(png_res)
png_ref  = imread('ref.png')
print(png_ref)

sum = 0
for j in range (len(png_ref[0])):
    for i in range (len(png_ref[0][0])):
        sum +=  pow((png_ref[i][j][0] - png_res[i][j][0]), 2) + \
                pow((png_ref[i][j][1] - png_res[i][j][1]), 2) + \
                pow((png_ref[i][j][2] - png_res[i][j][2]), 2)

MSE = sum / (3 * len(png_ref[0]) * len(png_ref[0][0]))

print(MSE)
