from PIL import Image, ImageDraw
import argparse
import os 

def negative_filter():
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

def b_n_w_filter():
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))

def sepia_filter():
	depth = 50
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))


parser = argparse.ArgumentParser()
parser.add_argument('-im_n', '--image_name', type=str)
parser.add_argument('-f', '--filter', type=str, choices=["negative", "black_n_white", "sepia"])
args = parser.parse_args()

s='image/'+args.image_name
image = Image.open(s) 
draw = ImageDraw.Draw(image) 
width = image.size[0] 
height = image.size[1] 
pix = image.load()

if args.filter == 'negative':
	negative_filter()
elif args.filter == 'black_n_white':
	b_n_w_filter()
else:
	sepia_filter()

if not os.path.isdir('filtered_images'):
	os.mkdir('filtered_images')

save = 'filtered_images/'+args.image_name.split('.')[0]+'_'+args.filter+'.png'
image.save(save, "PNG")
