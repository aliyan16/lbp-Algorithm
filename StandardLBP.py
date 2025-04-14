import cv2 as cv
import numpy as np



def padding(img,pad):
    img[:pad,:]=0
    img[-pad:,:]=0
    img[:,:pad]=0
    img[:,-pad:]=0
    return img

def lbpAlgo(window):
    gc=window[1,1]
    arr=[]
    arr.append(window[0,0])
    arr.append(window[0,1])
    arr.append(window[0,2])
    arr.append(window[1,2])
    arr.append(window[2,2])
    arr.append(window[2,1])
    arr.append(window[2,0])
    arr.append(window[1,0])
    length=len(arr)
    binaryArray=[]
    for i in range(length):
        if arr[i] <= gc:
            binaryArray.append(0)
        else:
            binaryArray.append(1)
    weights = [1 << i for i in range(8)]
    return sum([binaryArray[i] * weights[i] for i in range(8)])


            


def lbp(img,filter):
    img2=img.copy()
    rows,cols=img.shape
    frows,fcols=filter.shape
    for i in range(rows- frows + 1):
        for j in range(cols- fcols + 1):
            window=img[i:i+frows,j:j+fcols]
            lbpValue=lbpAlgo(window)
            img2[i,j]=lbpValue
    return img2




if __name__=='__main__':
    # img=cv.imread('image3.png',cv.IMREAD_GRAYSCALE)
    # # vid=cv.VideoCapture()
    # padimg=padding(img,1)
    # cv.imshow('original img',padimg)
    # cv.waitKey(2000)
    # filter=np.zeros((3,3),dtype=np.uint8)
    # lbpImg=lbp(padimg,filter)
    # cv.imshow('lbp img',lbpImg)
    # cv.waitKey(0)
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not captured.")
            break

        img=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        padded=padding(img,1)
        filter=np.zeros((3,3),dtype=np.uint8)
        frame=lbp(padded,filter)
        cv.imshow('Original',img)
        cv.imshow('LBP Frame',frame)

        if cv.waitKey(1)&0xFF==ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
