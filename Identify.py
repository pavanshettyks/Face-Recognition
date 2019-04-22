import face_recognition
from PIL import Image, ImageDraw

image_of_bill = face_recognition.load_image_file('img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

image_of_elon = face_recognition.load_image_file('img/known/Elon Musk.jpg')
elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

#  Array of encodings
known_face_encodings = [
  bill_face_encoding,
  steve_face_encoding,
  elon_face_encoding
]
#Array of names
known_face_names = [
  "Bill Gates",
  "Steve Jobs",
  "Elon Musk"
]

# Load test image
test_image = face_recognition.load_image_file('img/groups/bill-steve-elon.jpg')


# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)


# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"
  print(matches)
  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]

  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)

  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(25,255,0), outline=(255,55,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))











del draw
pil_image.show()
#pil_image.save('identify.jpg')
