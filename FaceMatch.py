import face_recognition

image_of_Bgates = face_recognition.load_image_file('img/known/Bill Gates.jpg')
face_encodings_bill = face_recognition.face_encodings(image_of_Bgates)[0]


image_of_unkown = face_recognition.load_image_file('img/unknown/bill-gates-4.jpg')
face_encodings_unkwown = face_recognition.face_encodings(image_of_unkown)[0]

result = face_recognition.compare_faces([face_encodings_bill],face_encodings_unkwown)

if result[0]:
    print("Bill is here")
else:
    print("Try another image")
