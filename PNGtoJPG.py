import os
from PIL import Image

read = "<PUTANJA>" # folder sa .png slikama
write = "<PUTANJA>" # folder gde ce se cuvati .jpg slike

names = os.listdir(read)
brojac = 0 # brojac

for name in names:

    img = Image.open(read + name) # ucitavanje slika
    name = name.split(".") # splitovanje po tacki
    
    if name[-1] == "png":
        
        name[-1] = "jpg" # definisanje formata
        name = str.join(".", name) # konvertovanje u jpg, dodavanje sufiksa .jpg 
        save_path = write + name # putanja za cuvanje 
        
        img = img.convert('RGB') # konvertovanje u RGB
        img.save(save_path) # pilow funkcija za cuvanje
        
        brojac += 1 # inkrementovanje brojaca
        print(save_path, "------brojac：", brojac) # ispis povratnih informaacija u konzoli
    
    else:
 
        continue

