def convert_medical_units(unit_from, unit_to, value):
    # Conversion factors for medical units
    if unit_from == 'mg' and unit_to == 'mcg':
        return f'{value * 1000:.2f} mcg'
    elif unit_from == 'mcg' and unit_to == 'mg':
        return f'{value / 1000:.6f} mg'
    elif unit_from == 'mL' and unit_to == 'L':
        return f'{value / 1000:.4f} L'
    elif unit_from == 'L' and unit_to == 'mL':
        return f'{value * 1000:.2f} mL'
    else:
        return 'Unsupported medical unit conversion'

if __name__ == '__main__':
    print(convert_medical_units(input('From unit: ').lower(), input('To unit: ').lower(), float(input('Value: '))))