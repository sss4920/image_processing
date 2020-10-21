from PIL import ImageGrab

snapshot = ImageGrab.grab()
save_path = "MySnapshot.jpg"
snapshot.save(save_path)