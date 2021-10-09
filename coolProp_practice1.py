import CoolProp.CoolProp as ct

fluid_name = 'water'

# Given
m_flow = 300 #
P1 = 100 #
T1 = 500+273 #K

P2 = 20 #
T2 = 320#

#Finding Entalphy

H1 = ct.PropSI('H', 'P', P1, 'T', T1, fluid_name)
H1 = ct.PropSI('H', 'P', P2, 'T', T2, subsfluid_nametance)


W = m_flow * (H1-H2)