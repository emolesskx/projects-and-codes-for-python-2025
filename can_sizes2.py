import math

class CanSize:
    def __init__(self, name, radius, height, cost):
        self.name = name
        self.radius = radius
        self.height = height
        self.cost = cost

def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2

def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area

def main():
    can_sizes = [
        CanSize("#1 Picnic", 6.83, 10.16, 0.28),
        CanSize("#1 Tall", 7.78, 11.91, 0.43),
        CanSize("#2", 8.73, 11.59, 0.45),
        CanSize("#2.5", 10.32, 11.91, 0.61),
        CanSize("#3 Cylinder", 10.79, 17.78, 0.86),
        CanSize("#5", 13.02, 14.29, 0.83),
        CanSize("#6Z", 5.40, 8.89, 0.22),
        CanSize("#8Z short", 6.83, 7.62, 0.26),
        CanSize("#10", 15.72, 17.78, 1.53),
        CanSize("#211", 6.83, 12.38, 0.34),
        CanSize("#300", 7.62, 11.27, 0.38),
        CanSize("#303", 8.10, 11.11, 0.42)
    ]

    for can in can_sizes:
        volume = compute_volume(can.radius, can.height)
        surface_area = compute_surface_area(can.radius, can.height)
        efficiency = compute_storage_efficiency(volume, surface_area)
        
        print(f"{can.name} {efficiency:.2f}")

if __name__ == "__main__":
    main()