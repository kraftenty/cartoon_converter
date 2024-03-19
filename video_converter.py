import cv2

def convert(inputPath, outputPath):
    print('Converting video... Please Wait a moment.')
    cap = cv2.VideoCapture(inputPath)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 동영상 코덱 설정
    fps = cap.get(cv2.CAP_PROP_FPS)  # 원본 동영상의 FPS
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 프레임 너비
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
    out = cv2.VideoWriter(outputPath, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.medianBlur(img_gray, 7)
        edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
        ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

        sigma_color = 5
        sigma_space = 7
        size = 5
        for i in range(15):
            frame = cv2.bilateralFilter(frame, size, sigma_color, sigma_space)
        
        cartoon = cv2.bitwise_and(frame, frame, mask=mask)
        
        out.write(cartoon)

    cap.release()
    out.release()
    print('Conversion complete!')
