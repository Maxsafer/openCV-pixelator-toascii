from os import listdir
import numpy as np
import cv2
import sys

def inputImg():
  files = []
  counter = 0
  inv = 0
  print(f'{counter}. Exit')
  for file in listdir('./images'):
    if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")) and file != 'output.jpg':
      counter += 1
      print(f'{counter}. {file}')
      files.append(file)
  chosen = input()
  if "inv" in chosen: inv = 1
  chosen = int(chosen.replace("inv",""))-1
  if chosen != -1: 
    inputName = f'{files[chosen]}'
    return [inputName, inv]
  else:
    sys.exit()

def generate_empty_image(bits, constant):
    return np.ones(shape=(bits * constant, bits * constant, 1), dtype=np.int16)

def toAscii(image, bits, w, h, inv):
  # 255/15 = 0 a 17, 17 a 34 etc. 15 rangos de intervalos de 17
  chars = ["@","#","%","&","8","0","U","L","l","!",";",",",":","."," "]
  #•
  if inv == False: chars.reverse()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  imascii = []

  constant = 15
  genimg = generate_empty_image(bits, constant)
  
  for row in range(0, bits):
    imascii.append([])
    for column in range(0, bits):
      color = image[row, column]
      if color <= 17: imascii[row].append(chars[0])
      elif color > 17 and color <= 34: imascii[row].append(chars[1])
      elif color > 34 and color <= 51: imascii[row].append(chars[2])
      elif color > 51 and color <= 68: imascii[row].append(chars[3])
      elif color > 68 and color <= 85: imascii[row].append(chars[4])
      elif color > 85 and color <= 102: imascii[row].append(chars[5])
      elif color > 102 and color <= 119: imascii[row].append(chars[6])
      elif color > 119 and color <= 136: imascii[row].append(chars[7])
      elif color > 136 and color <= 153: imascii[row].append(chars[8])
      elif color > 153 and color <= 170: imascii[row].append(chars[9])
      elif color > 170 and color <= 187: imascii[row].append(chars[10])
      elif color > 187 and color <= 204: imascii[row].append(chars[11])
      elif color > 204 and color <= 221: imascii[row].append(chars[12])
      elif color > 221 and color <= 238: imascii[row].append(chars[13])
      elif color > 238 and color <= 255: imascii[row].append(chars[14])
  
  for i in range(bits):
    print('')
    for j in range(bits):
      for times in range(0,round(w/h)):
        print(imascii[i][j], end = " ")
        cv2.putText(img=genimg, text=f'{imascii[i][j]}', org=(j * constant, (i * constant) + 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.5, color=(255),thickness=1)
  
  cv2.imwrite('output2.jpg', genimg)
  
def imageWriter(bits):
  selectImg = inputImg()
  input = cv2.imread(f'./images/{selectImg[0]}')
  
  # Get input size
  height, width = input.shape[:2]
  
  # Resize input to "pixelated"
  temp = cv2.resize(input, (bits, bits), interpolation=cv2.INTER_AREA)
  
  toAscii(temp, bits, width, height, selectImg[1])
  
  # Initialize output image
  output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
  
  cv2.imwrite('output.jpg', output)
  print('')
  print('__________________')
  
if __name__ == '__main__':
  while True:
    bits = 64
    imageWriter(bits)