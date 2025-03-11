def total_euro(radni_sati,eura_h):
    ukupno=radni_sati*eura_h
    return ukupno

radni_sati=int(input("Radni sati: "))
eura_h=float(input("eura/h: "))
print("Ukupno iznos: ",total_euro(radni_sati,eura_h))

