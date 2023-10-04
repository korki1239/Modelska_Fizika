from RLS import raketa, analiza

m_gorivo = 4_000 #kg
m_raketa = 10_000 #kg
m_tovor = 1_000 #kg

FalconX = raketa.inicializacija_rakete(m_gorivo,m_raketa,m_tovor)


print("Nekaj dejstev o vzletu rakete:")
v1 = FalconX.prva_kozmična_hitrost(10_000)
v2 = FalconX.druga_kozmična_hitrost()
r_gso, v_gso = FalconX.geostacionarna_orbita()

print(f"    - Prva k.h. na višini 10 km: {v1/1000:.0f} km/s")
print(f"    - Druga k.h. {v2/1000:.0f} km/s")
print(f"    - Višina GSO je {r_gso/1000:.1f} km in ima hitrost {v_gso/1000:.1f} km/s")



for m_goriva in [1,2,4,8,16,32]:
    FalconX = raketa.inicializacija_rakete(m_goriva*1_000,m_raketa,m_tovor)
    #raketa = raketa.inicializacija_rakete(m_gorivo*1_000,m_raketa,m_tovor)
    enota = FalconX.enote
    df=FalconX.simuliraj(0.1)
    analiza.info_o_vzletu(df, ime = f"m_goriva_{m_goriva:02d}", show = False, save = False)
    analiza.narisi_graf(df,"Čas",["Višina","Hitrost","Pospešek","Masa goriva"],enota)