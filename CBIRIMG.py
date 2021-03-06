import random
import math
import functools
## UNCOMMENT THE TEXTURE TYPE YOU WNT:
#texture_type = ’random’ #(A1)
#texture_type = ’vertical’ #(A2)
#texture_type = ’horizontal’ #(A3)
#texture_type = ’checkerboard’ #(A4)
#texture_type = ’low_contrast’ #(A5)
#texture_type = None #(A6)
IMAGE_SIZE = 8 #(A7)
GRAY_LEVELS = 6 #(A8)
displacement = [1,1] #(A9)
#displacement = [1,0] #(A10)
#displacement = [0,1] #(A11)
image = [[0 for _ in range(IMAGE_SIZE)]
    for _ in range(IMAGE_SIZE)] #(B1)
if texture_type == ’random’: #(B2)
    image = [[random.randint(0,GRAY_LEVELS-1)
for _ in range(IMAGE_SIZE)] for _ in range(IMAGE_SIZE)] #(B3)
    elif texture_type == ’diagonal’: #(B4)
    image = [[GRAY_LEVELS - 1 if (i+j)%2 == 0 else 0
for i in range(IMAGE_SIZE)] for j in range(IMAGE_SIZE)] #(B5)
    elif texture_type == ’vertical’: #(B6)
    image = [[GRAY_LEVELS - 1 if i%2 == 0 else 0
for i in range(IMAGE_SIZE)] for _ in range(IMAGE_SIZE)] #(B7)
    elif texture_type == ’horizontal’: #(B8)
    image = [[GRAY_LEVELS - 1 if j%2 == 0 else 0
for i in range(IMAGE_SIZE)] for j in range(IMAGE_SIZE)] #(B9)
    elif texture_type == ’checkerboard’:                                 #(B10)
    image = [[GRAY_LEVELS - 1 if (i+j+1)%2 == 0 else 0
for i in range(IMAGE_SIZE)] for j in range(IMAGE_SIZE)]                 #(B11)
    elif texture_type == ’low_contrast’:                                #(B12)
    image[0] = [random.randint(0,GRAY_LEVELS-1) for _ in range(IMAGE_SIZE)] #(B13)
for i in range(1,IMAGE_SIZE):                                           #(B14)
    image[i][0] = random.randint(0,GRAY_LEVELS-1)                       #(B15)
for j in range(1,IMAGE_SIZE):                                           #(B16)

    Texture and Color An RVL Tutorial by Avi Kak
    image[i][j] = image[i-1][j-1]                                       #(B17)
else:                                                                   #(B18)
    image = [[2, 0, 1, 1],[0, 1, 2, 0],[1, 1, 1, 2],[0, 0, 1, 1]] #(B19)
    IMAGE_SIZE = 4 #(B20)
    GRAY_LEVELS = 3 #(B21)
# CALCULATE THE GLCM MATRIX:
    print("Texture type chosen: %s" % texture_type) #(C1)
    print("The image: ") #(C2)
for row in range(IMAGE_SIZE): print(image[row]) #(C3)
    glcm = [[0 for _ in range(GRAY_LEVELS)] for _ in range(GRAY_LEVELS)] #(C4)
    rowmax = IMAGE_SIZE - displacement[0] if displacement[0] else IMAGE_SIZE -1 #(C5)
    colmax = IMAGE_SIZE - displacement[1] if displacement[1] else IMAGE_SIZE -1 #(C6)
for i in range(rowmax): #(C7)
for j in range(colmax): #(C8)
    m, n = image[i][j], image[i + displacement[0]][j + displacement[1]] #(C9)
    glcm[m][n] += 1 #(C10)
    glcm[n][m] += 1 #(C11)
    print("\nGLCM: ") #(C12)
for row in range(GRAY_LEVELS): print(glcm[row]) #(C13)

# CALCULATE ATTRIBUTES OF THE GLCM MATRIX:
    entropy = energy = contrast = homogeneity = None #(D1)
    normalizer = functools.reduce(lambda x,y: x + sum(y), glcm, 0) #(D2)
for m in range(len(glcm)): #(D3)
for n in range(len(glcm[0])): #(D4)
    prob = (1.0 * glcm[m][n]) / normalizer #(D5)
if (prob >= 0.0001) and (prob <= 0.999): #(D6)
            log_prob = math.log(prob,2) #(D7)
if prob < 0.0001: #(D8)
    log_prob = 0 #(D9)
if prob > 0.999: #(D10)
    log_prob = 0 #(D11)
if entropy is None: #(D12)
    entropy = -1.0 * prob * log_prob #(D13)
continue #(D14)
    entropy += -1.0 * prob * log_prob #(D15)
if energy is None: #(D16)
        energy = prob ** 2 #(D17)
continue #(D18)
    energy += prob ** 2 #(D19)
if contrast is None: #(D20)
    contrast = ((m - n)**2 ) * prob #(D21)
continue #(D22)
    contrast += ((m - n)**2 ) * prob #(D23)
if homogeneity is None: #(D24)
    homogeneity = prob / ( ( 1 + abs(m - n) ) * 1.0 ) #(D25)
continue #(D26)
    homogeneity += prob / ( ( 1 + abs(m - n) ) * 1.0 ) #(D27)
                                                        #28
    Texture and Color An RVL Tutorial by Avi Kak
if abs(entropy) < 0.0000001: entropy = 0.0 #(D28)
    print("\nTexture attributes: ") #(D29)
    print(" entropy: %f" % entropy) #(D30)
    print(" contrast: %f" % contrast) #(D31)
    print(" homogeneity: %f" % homogeneity) #(D32)