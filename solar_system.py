import cv2

img = cv2.imread("solar-system.jpg")



cv2.putText(img,  
           "SUN",
           (50, 100),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )

cv2.putText(img,  
           "MERCURY",
           (80, 260),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )           

cv2.putText(img,  
           "VENUS",
           (180, 170),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )       

cv2.putText(img,  
           "EARTH",
           (280, 270),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )            

cv2.putText(img,  
           "MARS",
           (380, 170),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )   

cv2.putText(img,  
           "JUPITER",
           (550, 390),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )   
cv2.putText(img,  
           "SATURN",
           (800, 130),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           )   
cv2.putText(img,  
           "URANUS",
           (950, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           ) 
cv2.putText(img,  
           "NEPTUNE",
           (1100, 140),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.8,  
           (255,255,255)
           ) 

cv2.putText(img,  
           "{SOLAR  SYSTEM}",
           (460, 40),  
           cv2.FONT_HERSHEY_COMPLEX,
           1,  
           (255,191,0)
           )   
cv2.imshow("SOLAR SYSTEM IMAGE",img)
cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)