from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filtered = []
    
    lenX = len(image)
    lenY = len(image[0])

    for linha in range(0, lenX, stride[0]):
        new_line = []
        for coluna in range(0, lenY , stride[1]):
            totalWeight = 0
            finalPixel = 0

            for xPixel, xKernel in zip(range(-1, 2, 1), range(0, len(kernel), 1)):
                for yPixel, yKernel in zip(range(-1, 2, 1), range(0, len(kernel), 1)):
                    
                    if(linha + xPixel > lenX - 1 or coluna + yPixel > lenX - 1):
                        pixelOG = 0
                    else:
                        pixelOG = image[linha + xPixel][coluna + yPixel]
                    
                    finalPixel += pixelOG * kernel[xKernel][yKernel]
                    totalWeight += kernel[xKernel][yKernel]
            
            if totalWeight < 1:
                totalWeight = 1
            finalPixel = finalPixel / totalWeight

            if finalPixel > 255:
                finalPixel = 255
            if finalPixel < 0:
                finalPixel = 0
            
            new_line.append(finalPixel)
        filtered.append(new_line)

    return filtered

Kernel = Kernel("minion.png", filter_function)

init()