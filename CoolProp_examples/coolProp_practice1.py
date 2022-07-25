import CoolProp.CoolProp as ct

fluid_name = 'water'

#conversion required
TC2TK = 273      #K
ton2Kg = 1000    #kg
bar2Pa = 100000  #Pa

# Given
m_flow = 300*tonToKg #ton/h
P1 = 100 * bar2Pa #
T1 = 500+TCtoTK #K

P2 = 20 * bar2Pa #
T2 = 320 + TCtoTK #K

#Finding Entalphy

H1 = ct.PropSI('H', 'P', P1, 'T', T1, fluid_name)
H1 = ct.PropSI('H', 'P', P2, 'T', T2, subsfluid_nametance)


W = m_flow * (H1-H2)

print (f'The entalpy of H1 is {H1:.3f} J/kg, or {H1/1000:.3f} kJ/kg.')
print (f'The entalpy of H2 is {H2:.3f} J/kg, or {H2/1000:.3f} kJ/kg.')
print (f'The work of W is {W:.3f} J, or {W/1000:.3f} kJ.')