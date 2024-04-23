def convert_to_dd(campos):
    gms1 = campos[0]
    gms2 = campos[1]
    gms1 = gms1.replace('°',' ').replace('\'',' ').replace('Â','').replace('"','').replace('O','').replace('S','').split()
    gms2 = gms2.replace('°',' ').replace('\'',' ').replace('Â','').replace('"','').replace('O','').replace('S','').split()

    dd1 = (int(gms1[0]) + (int(gms1[1])/60) + int(gms1[2])/3600)
    dd2 = (int(gms2[0]) + (int(gms2[1])/60) + int(gms2[2])/3600)
    campos[0] = dd1
    campos[1] = dd2
    return campos