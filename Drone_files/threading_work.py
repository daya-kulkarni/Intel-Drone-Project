import threading
import cv2

def task1():
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    print("I'm running task 1")

def task2():
    print("I'm running task 2")
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)




# creating threads
t1 = threading.Thread(target=task1, name='')
t2 = threading.Thread(target=task2, name='')

# starting threads
t1.start()
t2.start()

# wait until all threads finish
t1.join()
t2.join()
