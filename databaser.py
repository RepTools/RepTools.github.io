import json
import os

def get_material_info():
    # Check if materials.json exists and load it
    if os.path.exists('materials.json'):
        with open('materials.json', 'r') as file:
            materials_db = json.load(file)
    else:
        materials_db = {}

    material = {}
    
    # Get material name and check if it exists
    while True:
        material['Material_Name'] = input("Enter material name: ") or "undefined"
        if material['Material_Name'] in materials_db:
            # Show existing material properties
            print("\nCurrent material properties:")
            for key, value in materials_db[material['Material_Name']].items():
                print(f"{key}: {value}")
            print()  # Empty line for better readability
            
            overwrite = input(f"Material '{material['Material_Name']}' already exists. Do you want to overwrite it? (y/n): ").lower()
            if overwrite == 'y':
                break
            print("Please enter a different material name.")
        else:
            break
    
    material['Elastic_Modulus'] = input("Enter Elastic Modulus (GPa): ") or "undefined"
    material['Yield_Strength'] = input("Enter Yield Strength (MPa): ") or "undefined"
    material['Tensile_Strength'] = input("Enter Tensile Strength (MPa): ") or "undefined"
    material['Density'] = input("Enter Density (g/cm³): ") or "undefined"
    material['Shear_Modulus'] = input("Enter Shear Modulus (GPa): ") or "undefined"
    material['Poisson_Ratio'] = input("Enter Poisson Ratio: ") or "undefined"
    material['Compressive_Strength'] = input("Enter Compressive Strength (MPa): ") or "undefined"
    material['Category'] = input("Enter Material Category: ") or "undefined"
    
    return material

def main():
    # Check if materials.json exists, if not create empty dict
    if os.path.exists('materials.json'):
        with open('materials.json', 'r') as file:
            materials_db = json.load(file)
    else:
        materials_db = {}
    
    while True:
        material_info = get_material_info()
        material_name = material_info.pop('Material_Name')
        
        # Check if material already exists
        if material_name in materials_db:
            # Show existing material properties
            print("\nCurrent material properties:")
            for key, value in materials_db[material_name].items():
                print(f"{key}: {value}")
            print()  # Empty line for better readability
            
            overwrite = input(f"Material '{material_name}' already exists. Do you want to overwrite it? (y/n): ").lower()
            if overwrite != 'y':
                print("Skipping this material.")
                continue
        
        materials_db[material_name] = material_info
        
        # Save to JSON file
        with open('materials.json', 'w') as file:
            json.dump(materials_db, file, indent=4)
        
        continue_input = input("\nWould you like to add another material? (y/n): ").lower()
        if continue_input != 'y':
            break

if __name__ == "__main__":
    main()