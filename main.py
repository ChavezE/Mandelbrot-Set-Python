# The Mandelbrot-Set is the fractal created in the complex plane
# with the recursive formula: Zn = (Zn-1)^2 + C

# a^2 - b^2		real axis
# 2ab			imaginary axis

# libs
import cv2
import numpy as np

max_iterations = 100
infinity_thres = 16

# main window properties
height = 500
width = 500

# Create main window 8 bit resolution
main_img  = np.zeros((height,width,3), np.uint8)


def updateTrack():
	pass


def main():

	# Create trackbars for the resolution of the window
	# cv2.namedWindow('resolution')
	# cv2.createTrackbar('real-axis','resolution', 0, 2, updateTrack)
	# cv2.createTrackbar('imag-axis','resolution', 0, 2, updateTrack)

	print ("Calculating...")
	# Iteration loop for the window
	for x in range(0,width):
		for y in range (0, height):
			print (x,'/',width)
			# mapping the complex plane to 'a' and 'b' numbers to a trackbar
			# This will give us dynbamic resolution or zoom
			a_norm = np.interp(x, [0, width], [-2, 2])
			b_norm = np.interp(y, [0, height], [-2, 2])
			# print (a_norm,b_norm)
			
			new_a = float(a_norm)
			new_b = float(b_norm)

			# track the number of iterations before number Z goes to infinity

			n = 0
			while (n < max_iterations):
				p = new_a
				new_a = float(new_a*new_a - new_b*new_b) + a_norm
				new_b = float(2.0*p*new_b) + b_norm

				# print (new_a + new_b)
				# verify if num goes to infinity
				if (new_a*new_a + new_b*new_b > infinity_thres):
					break

				# update n
				n = n + 1

			if (n == max_iterations):
				main_img[y,x] = 0
			else:
				light_intensity = np.interp(n,[0,max_iterations], [0, 255])
				# light_intensity = 255
				main_img[y,x] = light_intensity


	cv2.imshow('Mandelbrot-Set', cv2.resize(main_img,(1000,1000)))
	# cv2.imshow('Mandelbrot-Set', main_img)

	# show it for half minute or until key pressed
	cv2.waitKey(30000)

if __name__ == '__main__':
	main()