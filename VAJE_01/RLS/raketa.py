from . import constante as const
import numpy as np

class inicializacija_rakete(object):
    def __init__(self,m_gorivo,m_raketa,m_tovor,h_start = const.R_earth, M = const.M_earth, rho = const.rho_0, Mol_mas = const.Molska_masa_zraka, R_spk = const.R_spk, T_ozracja = const.T_ozracja, R = const.R_earth):
        self.m_gorivo = m_gorivo
        self.m_raketa = m_raketa
        self.m_tovor = m_tovor
        self.M_planet = M
        self.R_planeta = R
        self.T_ozracja = T_ozracja
        self.rho_planet = rho
        self.G = const.G
        self.g = const.G * self.M_planet / const.R_earth**2
        self.h0 = (Mol_mas)/(const.R_spk * const.T_ozracja)
        self.h = h_start
        self.time = 0
        self.v = 0
        self.enote={}
        self.enote["Čas"] = " s"
        self.enote["Višina"] = " m"
        self.enote["Hitrost"] = " m/s"
        self.enote["Pospešek"] = " m/s2"
        self.enote["Skupna masa"] = " kg"
        self.enote["Masa goriva"] = " kg"
        self.enote["Gravitacijska sila"] = " N"
        self.enote["Zračni upor"] = " N"
        self.enote["Sila potiska"] = " N"
        self.enote["Rezultanta sil"] = " N"
        self.enote["Gostota"] = " kg/m3"
        
        self.df = {key:[] for key in self.enote}
    
    def gravitacijska_sila(self):
        return -const.G * self.M_planet * (self.m_raketa + self.m_tovor + self.m_gorivo) / (self.R_planeta + self.h)**2
    
    def Barometerska_enačba(self):
        return self.rho_planet * np.exp(-(self.h-self.R_planeta) * self.h0)
    
    def sila_upora(self):
        # Upoštevaj da je sila upora zmeraj usmerjena v nasprotno smer hitrosti. Torej
        # če se raketa premika gor je - če se premika dol pa je +
        rho = self.Barometerska_enačba()
        if self.v > 0:
            return -0.5 * rho * self.v**2 * const.C_d * const.S
        else:
            return 0.5 * rho * self.v**2 * const.C_d * const.S
    
    #Simuliraj let rakete in puporabi raketno enačbo
    def sila_potiska(self):
        if self.m_gorivo > 0:
            return const.F_potiska
        else:
            return 0
    
    def posodobi_maso_goriva(self,dt):
        if self.m_gorivo>0:
            return self.m_gorivo - const.burn_rate * dt
        else:
            return 0.0

    def Rezultanta_sil(self):
        #F_p - F_g - F_u
        return self.sila_potiska() + self.gravitacijska_sila() + self.sila_upora()
    
    def pospešek(self):
        m_skupaj = self.m_raketa + self.m_tovor + self.m_gorivo
        return self.Rezultanta_sil() / m_skupaj
    
    def enote(self):
        return self.enote 
    
    def simulacija_vzleta_rakete_2(self,dt = 0.1):
        """_summary_
        S to funkcijo izvedemo en integracijski korak simuliranja leta rakete
        Funkcija vrne slovar z vsemi podatki o stanju rakete po integracijskem koraku.
        """
        self.time = self.time + dt 
        self.h = self.h + self.v * dt
        self.v = self.v + self.pospešek() * dt
        self.m_gorivo = self.posodobi_maso_goriva(dt)
        result={}
        result["Čas"] = self.time
        result["Višina"] = self.h - self.R_planeta
        result["Hitrost"] = self.v
        result["Pospešek"] = self.pospešek()
        result["Skupna masa"] = self.m_raketa + self.m_tovor + self.m_gorivo
        result["Masa goriva"] = self.m_gorivo
        result["Gravitacijska sila"] = self.gravitacijska_sila()
        result["Zračni upor"] = self.sila_upora()
        result["Sila potiska"] = self.sila_potiska()
        result["Rezultanta sil"] = self.Rezultanta_sil()
        result["Gostota"] = self.Barometerska_enačba()
        return result
    
    def update_data(self,data):
        for key in data:
            self.df[key].append(data[key])
    
    def simuliraj(self,dt):
        stanje_rakete = self.simulacija_vzleta_rakete_2(dt)
        self.update_data(stanje_rakete)
        while stanje_rakete["Hitrost"] > 0 and stanje_rakete['Višina']<360_000_000:
            stanje_rakete = self.simulacija_vzleta_rakete_2(dt)
            self.update_data(stanje_rakete)
        return self.df
    
    def prva_kozmična_hitrost(self,h):
        return np.sqrt(const.G * self.M_planet / (self.R_planeta + self.h))
    
    def geostacionarna_orbita(self):
        micro = self.G*self.M_planet
        T = 24*60*60
        R_orbite = np.power(micro*T**2/(4*np.pi**2),1/3) - self.R_planeta
        v_orbite = 2*np.pi*R_orbite/T
        return R_orbite, v_orbite
    
    def druga_kozmična_hitrost(self):
        """
        Ubežna hitrost
        """
        return np.sqrt(2 * const.G * self.M_planet / (self.R_planeta))  
        
        