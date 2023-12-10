import cv2
from pyzbar.pyzbar import decode
import webbrowser

def read_qr_code():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Display the camera feed
        cv2.imshow('QR Code Reader', frame)

        # Decode QR codes
        decoded_objects = decode(frame)
        if len(decoded_objects)>0:
            # Print the data contained in the QR code
            print("QR Code data:", decoded_objects[0].data.decode())
            
            # Open the interpreted link in Chrome
            webbrowser.open(decoded_objects[0].data.decode())
            break

        # Exit loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_qr_code()
