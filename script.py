import cv2
import numpy as np
#from gui import show2



def blur(img_path):
    img = cv2.imread(img_path)
    rows, cols = img.shape[:2]
    kernel_5x5 = np.ones((5, 5), np.float32) / 25.0

    output = cv2.filter2D(img, -1, kernel_5x5)

    cv2.imwrite('01.jpg',output)

def edge_detection(img_path):
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape

    canny = cv2.Canny(img, 50, 240)

    cv2.imwrite('01.jpg', canny)

def motion_blur(img_path):
    img = cv2.imread(img_path)

    size = 15  # generating the kernel

    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size

    # applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_motion_blur)

    cv2.imwrite('01.jpg', output)

def sharp(img_path):
    img = cv2.imread(img_path)

    # generating the kernels
    kernel_sharpen = np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 8, 2, -1], [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0

    # applying different kernels to the input image
    output = cv2.filter2D(img, -1, kernel_sharpen)
    cv2.imwrite('01.jpg', output)

def Enhance(img_path):
    import cv2
    import numpy as np
    img = cv2.imread(img_path)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    # convert the YUV image back to RGB format
    output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    cv2.imwrite('01.jpg', output)

