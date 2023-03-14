import cv2


def zkr():
    with open("v.txt", "r", encoding="utf8") as f:
        return f.readline()
    # with open("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\v.txt", "r", encoding="utf8") as f:
    #     return f.readline()


def tul():
    with open("tul.txt", "r", encoding="utf8") as f:
        return f.readline()
    # with open("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\tul.txt", "r", encoding="utf8") as f:
    #     return f.readline()


def spis(s):
    with open("write-offprc.txt", "a", encoding="utf8") as f:
        f.write(s)
    # with open("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\write-offprc.txt", "a", encoding="utf8") as f:
    #     f.write(s)


# clf = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
path_cs = "haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(path_cs)
cap = cv2.VideoCapture(0)

c = 0
c1 = 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if faces == ():
        c+=1

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if (x <= 130 or x >= 445) or (y <= 140 or y >= 340):
            c1 += 1

    cv2.imshow("came", frame)
    
    if cv2.waitKey(1) == ord('q') or zkr() == "true": 
        with open("v.txt", "w", encoding="utf8") as f:
            f.write("false")
        # with open("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\python\\v.txt", "w", encoding="utf8") as f:
        #     f.write("false")
        pr = 50
        if 10 <= c <= 40_000:
            pr += 15
        elif 40_001 <= c <= 85_000 and tul() == "true":
            pr += 10
        elif 40_001 <= c <= 85_000 and tul() == "":
            pr += 20
        elif c >= 85_001:
            pr += 10
        elif c1 >= 10_000:
            pr += 20
        spis(f"{pr}%")
        break

cap.release()
cv2.destroyAllWindows()