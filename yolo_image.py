def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            print(type(r_image))
            import cv2
            cv2.imwrite("out.jpg", np.asarray(r_image)[..., ::-1])
            r_image.show()
    yolo.close_session()



if __name__ == '__main__':
    detect_img(YOLO())