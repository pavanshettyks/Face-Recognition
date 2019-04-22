import face_recognition
image = face_recognition.load_image_file('img/groups/team1.jpg')
face_loactions = face_recognition.face_locations(image)

print(face_loactions)
print(f'There are {len(face_loactions)} people' )
