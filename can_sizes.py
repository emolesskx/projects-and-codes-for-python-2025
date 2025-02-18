import math

def main():
    # Define can size data
    cans = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42},
    ]

    best_storage_efficiency = {"name": None, "efficiency": 0}
    best_cost_efficiency = {"name": None, "efficiency": 0}

    # Process each can
    for can in cans:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])

        # Print results for the can
        print(f"{can['name']}: Storage Efficiency = {storage_efficiency:.2f}, Cost Efficiency = {cost_efficiency:.2f}")

        # Update best storage efficiency
        if storage_efficiency > best_storage_efficiency["efficiency"]:
            best_storage_efficiency = {"name": can["name"], "efficiency": storage_efficiency}

        # Update best cost efficiency
        if cost_efficiency > best_cost_efficiency["efficiency"]:
            best_cost_efficiency = {"name": can["name"], "efficiency": cost_efficiency}

    # Print best efficiencies
    print(f"\nCan with highest storage efficiency: {best_storage_efficiency['name']} ({best_storage_efficiency['efficiency']:.2f})")
    print(f"Can with highest cost efficiency: {best_cost_efficiency['name']} ({best_cost_efficiency['efficiency']:.2f})")

def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    return volume / cost

if __name__ == "__main__":
    main()
