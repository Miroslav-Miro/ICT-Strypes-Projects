from PIL import Image

def make_white_parts_transparent(image_to_convert, new_file_name):
  image = image_to_convert.convert('RGBA')
  
  data = image.getdata()
  
  new_data = []
  
  for item in data:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
      new_data.append((255,255,255,0))
    else: 
      new_data.append(item)
  
  image.putdata(new_data)
  
  image.save(f'{new_file_name}.png')    

def decode_the_message(mask, matrix):
  
  w = matrix.width
  h = matrix.height
  resized_mask = mask.resize((w, h))

  make_white_parts_transparent(resized_mask, 'transparent_mask')

  transparent_mask_image = Image.open('transparent_mask.png')
  matrix.paste(im=transparent_mask_image, box=(0,0),mask=transparent_mask_image )

  matrix.show() 


mask = Image.open(r'C:\Users\miros\Desktop\ICT-Strypes-Projects\practice\section_16\images\mask.png')
matrix = Image.open(r'C:\Users\miros\Desktop\ICT-Strypes-Projects\practice\section_16\images\word_matrix.png')

decode_the_message(mask, matrix)
