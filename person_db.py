from array import array
import os
from PIL import Image, ImageDraw
import sys
import time
from io import BytesIO
import requests
import cv2
import io
import numpy as np
import test3

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def isSugg():
    cap = cv2.VideoCapture('body.mp4')

    while True:
        ret, frame = cap.read()
        cv2.imwrite("b1.jpg", frame)

        subscription_key = "49476384fc2548968bfc09ab465229ca"
        endpoint = "https://seungjoolee.cognitiveservices.azure.com/"


        print("===== Detect objects =====")
        analyze_url = endpoint + "vision/v3.1/analyze"
        image_data = open("b1.jpg", "rb").read()
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'objects'}
        response = requests.post(
            analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()
        analysis = response.json()
        #print(analysis.get('objects'))
        #li = []
    # draw = ImageDraw.Draw(image_data)

        objects = analysis['objects']
        for obj in objects:
            if obj['object'] == 'person':
                rect = obj['rectangle']
                x = rect['x']
                y = rect['y']
                w = rect['w']
                h = rect['h']

                #cv2.imwrite("ad1.jpg", frame[y:y+h, x:x+w])
                ad, ra = test3.adult(frame[y:y+h, x:x+w])
                if(ad == True or ra == True):
                    face_region = frame[y:y+h, x:x+w]
                    M = face_region.shape[0]
                    N = face_region.shape[1]
                    face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
                    frame[y:y+h, x:x+w] = face_region

                #image_data = np.frombuffer(image_data, dtype=np.float64)

                
        os.remove("b1.jpg")
            #draw.rectangle(((x,y), (x+w, y+h)), outline='yellow')

        cv2.imshow("body", frame)
        if cv2.waitKey(1)==27:
            break

    cap.release()
    cv2.destroyAllWindows()
        #cv2.rectangle(image_data, (x,y), (x+h, y+h), (0, 0, 255), 2)

isSugg()
""" x=0
    y=0
    w=0
    h=0
    for i in range(len(analysis.get('objects'))):
        if analysis.get('objects')[i].get('object') == 'person':
            li.append(analysis.get('objects')[i].get('rectangle'))
            for name, positon in li[i]:
                if name == "x":
                    x = li[name]
                elif name == "y":
                    y =li[name]
                elif name == "w":
                    y =li[name]
                elif name == "h":
                    y =li[name]
            roi = image_data[y:y+h, x:x+w]
            cv2.imwrite("n" + str(i) + ".png", roi)
            
    return li"""