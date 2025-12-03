from typing import List
from Kernel import Kernel, init


def filter_function(image: List[List[int]], kernel: List[List[int]]):
    
    stride = (1,1)
    filtered = []
    
    lenY = len(image)
    lenX = len(image[0])
    
    top = len(kernel)//2
    left = len(kernel)//2
    
    for i in range (0, lenY, stride[0]):
        new_lin = []
        for j in range(0, lenX, stride[1]):
            s = 0
            sk = 0
            for ki in range(len(kernel)):
                for kj in range(len(kernel[ki])):
                    y = i - top + ki
                    x = j - left + kj
                    sk += kernel[ki][kj]
                    if y < 0 or y >= lenY or x < 0 or x >= lenY:
                        continue
                    s += image[y][x] * kernel[ki][kj]
            if sk != 0:
                s /= sk
            if s < 0:
                s = 0
            if s > 255:
                s = 255
                
            new_lin.append(s)
        filtered.append(new_lin)
                                
    return filtered[:]


Kernel = Kernel("cat.jpg", filter_function)

init()