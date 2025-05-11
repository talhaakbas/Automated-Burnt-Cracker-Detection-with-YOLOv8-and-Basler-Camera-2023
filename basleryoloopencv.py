from pypylon import pylon
from ultralytics import YOLO
from supervision.video.source import get_video_frames_generator
import cv2
import time

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
converter = pylon.ImageFormatConverter()

#camera.ExposureTime = 105000

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

model = YOLO('C:/Users/talha/forcuda.pt')  # load a pretrained model

starting_time = time.time()
kare_id = 0
font = cv2.FONT_HERSHEY_PLAIN

while camera.IsGrabbing():
    kare_id += 1
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)

        sonuc = model(img)[0]
        koordinatlar = sonuc.boxes.xyxy
        koord = koordinatlar.tolist()
        if len(koord) > 0:

            (x1, y1, x2, y2) = koord[0]
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            print("x1 koordinatı:  ", x1)
            print("y1 koordinatı:  ", y1)
            print("x2 koordinatı:  ", x2)
            print("y2 koordinatı:  ", y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        elapsed_time = time.time() - starting_time
        fps = kare_id / elapsed_time
        cv2.putText(img, "FPS: " + str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)

        cv2.imshow('title', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()

# Releasing the resource
camera.StopGrabbing()

cv2.destroyAllWindows()