import cv2

def convert(inputPath, outputPath):
    print('Converting image...')
    img = cv2.imread(inputPath)
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)
    
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    
    sigma_color = 5
    sigma_space = 7
    size = 5
    for i in range(15):
        img = cv2.bilateralFilter(img, size, sigma_color, sigma_space)
    
    cartoon = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imwrite(outputPath, cartoon)
    print('Conversion complete!')
