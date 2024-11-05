'''
import FWI

ffmc0 = 85.0
dmc0 = 6.0
dc0 = 15.0
mth = 4
temp = 17.0
rhum = 42.0
wind = 25.0
prcp = 0.0

fwisystem = FWI.FWICLASS(temp, rhum, wind, prcp)
ffmc = fwisystem.FFMCcalc(ffmc0)
dmc = fwisystem.DMCcalc(dmc0,mth)
dc = fwisystem.DCcalc(dc0,mth)
isi = fwisystem.ISIcalc(ffmc)
bui = fwisystem.BUIcalc(dmc,dc)
fwi = fwisystem.FWIcalc(isi,bui)

print(ffmc)
print(dmc)
print(dc)
print(isi)
print(bui)
print(fwi)
'''
import FWI  

#Function to calculate FWI using provided weather parameters
def calculate_fwi(temp, rhum, wind, prcp, ffmc0=85.0, dmc0=6.0, dc0=15.0, mth=4):
    
    fwisystem = FWI.FWICLASS(temp, rhum, wind, prcp)
    ffmc = fwisystem.FFMCcalc(ffmc0)
    dmc = fwisystem.DMCcalc(dmc0, mth)
    dc = fwisystem.DCcalc(dc0, mth)
    isi = fwisystem.ISIcalc(ffmc)
    bui = fwisystem.BUIcalc(dmc, dc)
    fwi = fwisystem.FWIcalc(isi, bui)
    
    return {
        'ffmc': ffmc,
        'dmc': dmc,
        'dc': dc,
        'isi': isi,
        'bui': bui,
        'fwi': fwi
    }
