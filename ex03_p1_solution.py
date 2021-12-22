import numpy as np

class Q11:
    
    global c 
    global Q
    c = 299792458                # m/s
    Q = 1.602E-19                # C

    
    def __init__(self, A, CS, T):
        self.A  = A              # Atomic number
        self.CS = CS             # Charge State
        self.T  = T              # Kinetic energy (MeV)
        
    def get_T(self):
        global T_tot
        T_tot = self.A*self.T*1.60205E-13
        
    def get_Mass(self):
        global m
        m = self.A*1.6605402E-27
    
    def get_RestE(self):
        global E_r
        E_r = m*c**2
    
    def get_TotE(self):
        global E_t
        E_t = T_tot+E_r
        
    def get_p(self):
        global p
        p = np.sqrt( (E_t**2-E_r**2)/c**2)
    
    def get_rigidity(self):
        pB = p/(Q*self. CS)
        print('\nThe magnetic rigidity for is: ' "{:.2E}".format(pB), 'T m\n')
   
    def get_all(self):
        self.get_T()
        self.get_Mass()
        self.get_RestE()
        self.get_TotE()
        self.get_p()
        self.get_rigidity()
        
Q3 = Q11(238,28,90)
Q4 = Q11(197,77,330)
Q5 = Q11(1,1,7000000)
Q6 = Q11(0,1,10000)

Q3.get_all()    
    
    
# spent 4 hours trying to get np.vectorize to work with classes but with no luck
