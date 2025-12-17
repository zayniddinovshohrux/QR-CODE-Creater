import qrcode

url = input("Enter the URL to generate QR code: ")
img = qrcode.make(url)

img.save("qrcode.png")
print("QR code saved as qrcode.png")