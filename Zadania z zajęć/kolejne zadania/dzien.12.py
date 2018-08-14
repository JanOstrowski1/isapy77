import requests
import json
from PIL import Image, ImageDraw, ImageFont
import io

api_key = "cf0fb939ebb24c83a93536a0afb2df1b"
api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
adres_obrazka = 'https://ocdn.eu/pulscms-transforms/1/QtCktkqTURBXy9jNzEzOWQ2N2I5MzM1ZWVmYjVlZjg2NDkzZTViOTRhYy5qcGVnk5UDAADNBCvNAliTBc0DFM0BvJUH2TIvcHVsc2Ntcy9NREFfLzIzMzdjOWZkNmI5MzFlZTZjYjBkMjNkY2JhMjU4YTlkLnBuZwDCAA'


naglowki = {'Ocp-Apim-Subscription-Key': api_key}
parametry = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

dane = {'url': adres_obrazka}

wynik = requests.post(api_url, headers=naglowki, params=parametry, json=dane)
twarze = wynik.json()

obiekt_pil = Image.open(io.BytesIO(requests.get(adres_obrazka).content))
draw_pil = ImageDraw.Draw(obiekt_pil)
font = ImageFont.truetype(r"C:\Windows\Fonts\bahnschrift.ttf", 30)

for osoba in twarze:
    wiek = osoba['faceAttributes']['age']
    emocje = osoba['faceAttributes']["emotion"]
    glowna_emocja = max(emocje, key=emocje.get)
    ws_twarzy = osoba["faceRectangle"]
    x1 = ws_twarzy['left']
    y1 = ws_twarzy['top']
    x2 = x1 + ws_twarzy['width']
    y2 = y1 + ws_twarzy['height']

    draw_pil.rectangle(((x1,y1),(x2,y2)), outline=(128,128,255,255))
    draw_pil.text((x1,y2+20), glowna_emocja, fill=(128,128,255,255),font=font )
    draw_pil.text((x1,y2+80), "({}l.)".format(str(int(wiek))), font=font)

obiekt_pil.show()

text = wynik.text
for_dumps = json.loads(text)
#print(json.dumps(for_dumps, indent=4, sort_keys=True))