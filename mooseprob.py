a = 2.757 
b = 16.793

def moose_body_mass(latitude):
    mass = a * latitude + b
    return mass