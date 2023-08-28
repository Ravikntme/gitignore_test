# importing packages from package_imp.py
from Pricing-Module.package_imp import *
#import cv2 as cv
#import cv2

# vid = cv.VideoCapture(0)
# vid_width = int(vid.get(3))
# vid_height = int(vid.get(4))
# print("width,height", vid_height,vid_height)
# size = (vid_width,vid_height)
# fps = vid.get(cv.CAP_PROP_FPS)
# print("sssssssssssssssssss==========s===========",fps)
# result = cv.VideoWriter("myvideo1.avi",cv.VideoWriter_fourcc(*'MJPG'),fps,size)
# while(vid.isOpened()):
#     flag,frame = vid.read()
#     if flag == True:
#         result.write(frame)
#         # print("result===============",result)
#         cv.imshow("myvideo",frame)
#         if cv.waitKey(1) & 0xFF==ord('q'):
#             break
#     else:
#         break
# vid.release()
# result.release()
# cv.destroyAllWindows()
# print("video",vid.get(3))


  
   
# Create an object to read 
# from camera
video = cv2.VideoCapture(0)
fps = video.get(cv.CAP_PROP_FPS)
   
# We need to check if camera
# is opened previously or not
if (video.isOpened() == False): 
    print("Error reading video file")
  
# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)
   
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         fps, size)
    
while(True):
    ret, frame = video.read()
  
    if ret == True: 
  
        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)
  
        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)
  
        # Press S on keyboard 
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
  
    # Break the loop
    else:
        break
  
# When everything done, release 
# the video capture and video 
# write objects
video.release()
result.release()
    
# Closes all the frames
cv2.destroyAllWindows()
   
print("The video was successfully saved")
