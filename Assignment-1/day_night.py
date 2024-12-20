## take the video
import cv2
import numpy as np

vid_cap = cv2.VideoCapture("./cv_practice/WhatsApp Video 2024-12-06 at 8.36.21 PM.mp4")

while True :
    ret, frame = vid_cap.read()

    if not ret:
        print("unable to read frame")
        break

    ## converting in bgr to hsv
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    ## spliting hsv
    sat = hsv_img[:,:,1]
    hue = hsv_img[:,:,0]
    val = hsv_img[:,:,2]

    day_mask = (sat < 75) & (hue > 20) & (val > 178)
    night_mask = (sat > 38) & (hue > 38) & (val < 20)
    evening_mask = (sat > 127) & (hue < 19) & (val > 127)

    ##  percentage
    day_perc = np.sum(day_mask)/sat.size * 100
    night_perc = np.sum(night_mask)/sat.size * 100
    evening_perc = np.sum(evening_mask)/sat.size * 100


    text_1 = (f"DAY Percentage :{day_perc}")
    text_2 = (f"night percentage :{night_perc}")

    org_1 = (50, 50) # upper right corner of the text string in the image
    org_2 = (70,70)
    org_3 = (150,150)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.8
    fontScale_2 = 1.2
    color = (255, 0, 2) # blue color in rgb
    color_2 = (2,5,250)
    thickness = 1
    thickness_2 = 2

    if (day_perc >= night_perc) & (day_perc > evening_perc) :
        overall = "Day"
    if (night_perc > day_perc) & (night_perc > evening_perc) :
        overall = "Night"
    if (evening_perc > day_perc) & (evening_perc > night_perc) :
        overall = "Evening"

    # Add text to the image
    cv2.putText(frame, text_1, org_1, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(frame, text_2, org_2, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(frame, overall, org_3, font, fontScale_2, color_2, thickness_2, cv2.LINE_AA)

    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    frame_delay = int(1000 / fps)

    cv2.resize(frame,(8000,2000))

    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

    ##cv2.imwrite("./cv_practice/updated_video.mp4",frame)
    cv2.imshow("frame", frame)

vid_cap.release()
cv2.destroyAllWindows() 

