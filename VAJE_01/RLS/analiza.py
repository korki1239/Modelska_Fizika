import pandas as pd
import matplotlib.pyplot as plt
from . import constante as const

micro = const.R_spk*288/const.Molska_masa_zraka


def info_o_vzletu(df:dict,ime:str, show = False, save = False):
    df_leta=pd.DataFrame(df)
    if show:
        print(df_leta.describe())
    m = df['Masa goriva'][0]/1000.0
    Hmax = max(df['Višina'])/1000
    print(f"Masa goriva: {m:.0f} ton\t",
          f"Najvišja lega: {Hmax:.1f} km\t",
          f"Tlak znaša: {micro*df['Gostota'][-1]/101300:.3f} bar")
    if save:
        df_leta.to_excel(f"df_{ime}.xlsx")
    
def narisi_graf(df:dict, x:str, y:list, enote:dict):
    plt.figure(figsize=(12,12))
    for iy,yy in enumerate(y):
        plt.subplot(int(f"22{iy+1}"))
        plt.plot(df[x],df[yy],label=yy)
        plt.xlabel(f"{x}({enote[x]})")
        plt.ylabel(f"{yy}({enote[yy]})")
    plt.show()