import qrcode as q
link = input("enter link : ")
img = q.make(link)

img.save("sandesh.png")
print("Sucessfully Created!!!")