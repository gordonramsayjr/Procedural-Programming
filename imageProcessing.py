import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import scipy.ndimage as gf

def loadImage(filename):
    imageData = img.imread(filename)

    if type(imageData[0, 0, 0]) == np.float32:
        imageData *= 255
    (rows, cols, colourChannels) = imageData.shape
    if colourChannels == 4:
        imageData = imageData[:, :, 0:3]
    imageData = np.float64(imageData)
    return imageData


def saveImage(imageData, filename, scale=False, format="RGB"):
    if format == "HSL":
        hsl2rgb(imageData)

    if not scale:
        imageData[imageData > 255] = 255
        imageData[imageData < 0] = 0
    if scale:
        imageData -= np.min(imageData)
        imageData = imageData / np.max(imageData)
        imageData *= 255
    imageData = np.uint8(imageData)
    plt.imsave(filename, imageData)


def rgb2hsl(imageData):
    (rows, cols, colourLength) = imageData.shape

    for row in range(0, rows):
        for col in range(0, cols):
            (R, G, B) = imageData[row, col, :]
            R2 = R / 255
            G2 = G / 255
            B2 = B / 255
            cmax = np.max((R2, G2, B2))
            cmin = np.min((R2, G2, B2))
            D = cmax - cmin

            if D == 0:
                H = 0
            elif cmax == R2:
                H = 60 * np.mod((G2 - B2) / D, 6)
            elif cmax == G2:
                H = 60 * (((B2 - R2) / D) + 2)
            elif cmax == B2:
                H = 60 * (((R2 - G2) / D) + 4)

            L = (cmax + cmin) / 2

            if D == 0:
                S = 0
            else:
                S = (D / (1 - np.abs(2 * L - 1)))
            imageData[row,col,:] = (H,S,L)
    return imageData

def hsl2rgb(imageData):
    (rows, cols, colourLength) = imageData.shape
    for row in range(0,rows,):
        for col in range(0,cols):
            (H,S,L) = imageData[row,col,:]
            C = (1-np.abs(2*L-1))*S
            X = C * (1-np.abs(np.mod(H/60,2)-1))
            m = L - (C/2)

            if 0 <= H < 60:
                (R2,G2,B2) = (C,X,0)
            elif 60 <= H < 120:
                (R2, G2, B2) = (X,C,0)
            elif 120 <= H < 180:
                (R2, G2, B2) = (0,C,X)
            elif 180 <= H < 240:
                (R2, G2, B2) = (0,X,C)
            elif 240 <= H < 300:
                (R2, G2, B2) = (X,0,C)
            elif 300 <= H < 360:
                (R2, G2, B2) = (C,0,X)
            (R, G, B) = ((R2 + m)*255), ((G2+m)*255), ((B2+m)*255)
            imageData[row,col,:] = (R,G,B)
    return imageData

def showImage(imageData):
    tmp = imageData.copy()
    tmp[tmp > 255] = 255
    tmp[tmp < 0] = 0
    tmp.round()
    tmp = np.uint8(tmp)
    plt.imshow(tmp)
    plt.axis('off')


def brightness(imageData, b, changeType="absolute"):
    if changeType == "absolute":
        imageData += b
    elif changeType == "relative":
        imageData *= b
    else:
        return imageData
    return imageData

def contrast(imageData, c):
    imageData = c*(imageData-127.5) + 127.5
    return imageData

def saturation(imageData, amount):
    imageData[:,:,1] *= amount
    return imageData

def toneMap(imageData, H, S):
    imageData[:,:,0] = H
    imageData[:,:,1] = S
    return imageData

def crop(imageData, top, bottom, left, right):
    [rows,cols,num] = imageData.shape
    if top < 0 or top >= bottom:
        print("ERROR: top is outside of the range")
        return imageData
    elif bottom >= cols:
        print("ERROR: bottom is outsode of the range")
        return imageData
    elif left <= 0 or left >= right:
        print("ERROR: left is outside of the range")
        return imageData
    elif right >= rows:
        print("ERROR: Right is outside of the range")
        return imageData

    return imageData[top:bottom, left:right]

def saturated(imageData, type="white", format="RGB"):
    PC = np.size(imageData)
    L = imageData[:,:,2]

    if format == "RGB":
        if type == "white":
            p = imageData[imageData >= 254.5]
            return np.size(p) / PC * 100
        if type == "black":
            p = imageData[imageData <= 0.5]
            return np.size(p) / PC * 100
    if format == "HSL":
        if type == "white":
            p = L[L >= 0.99]
            return np.size(p) / (PC/3) * 100
        if type == "black":
            p = L[L <= 0.01]
            return np.size(p) / (PC / 3) * 100


def histogram(imageData, scale="linear", channel="L", bins=255, format="RGB"):
    R = imageData[:,:,0]
    G = imageData[:,:,1]
    B = imageData[:,:,2]
    L = imageData[:,:,2]

    if scale == "linear":
        if format == "RGB":
            if channel == "L":
                rgb2hsl(imageData)
                plt.hist(L.reshape(-1), bins)
            elif channel == "R":
                plt.hist(R.reshape(-1), bins)
            elif channel == "G":
                plt.hist(G.reshape(-1), bins)
            elif channel == "B":
                plt.hist(B.reshape(-1), bins)
        if format == "HSL":
            if channel == "L":
                plt.hist(L.reshape(-1), bins)
            elif channel == "R":
                hsl2rgb(imageData)
                plt.hist(R.reshape(-1), bins)
            elif channel == "G":
                hsl2rgb(imageData)
                plt.hist(G.reshape(-1), bins)
            elif channel == "B":
                hsl2rgb(imageData)
                plt.hist(B.reshape(-1), bins)
    if scale == "log":
        if format == "RGB":
            if channel == "L":
                rgb2hsl(imageData)
                plt.hist(L.reshape(-1), bins,log=True)
            elif channel == "R":
                plt.hist(R.reshape(-1), bins,log=True)
            elif channel == "G":
                plt.hist(G.reshape(-1), bins,log=True)
            elif channel == "B":
                plt.hist(B.reshape(-1), bins,log=True)
        if format == "HSL":
            if channel == "L":
                plt.hist(L.reshape(-1), bins,log=True)
            elif channel == "R":
                hsl2rgb(imageData)
                plt.hist(R.reshape(-1), bins,log=True)
            elif channel == "G":
                hsl2rgb(imageData)
                plt.hist(G.reshape(-1), bins,log=True)
            elif channel == "B":
                hsl2rgb(imageData)
                plt.hist(B.reshape(-1), bins,log=True)

def unsharpMask(imageData, radius=5, amount=2, format="RGB"):
    if format == "HSL":
        hsl2rgb(imageData)
    sigma = radius/3
    RB = gf.gaussian_filter(imageData[:,:,0], sigma)
    GB = gf.gaussian_filter(imageData[:, :, 1], sigma)
    BB = gf.gaussian_filter(imageData[:, :, 2], sigma)

    RS = imageData[:,:,0] + (imageData[:,:,0] - RB) * amount
    GS = imageData[:,:,1] + (imageData[:,:,1] - GB) * amount
    BS = imageData[:,:,2] + (imageData[:,:,2] - BB) * amount

    imageData[:,:,0] = RS
    imageData[:,:,1] = GS
    imageData[:,:,2] = BS

    return imageData
