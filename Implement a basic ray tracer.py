# Simple ray tracer (spheres only)
class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

def ray_tracer(ray_origin, ray_direction, spheres):
    for sphere in spheres:
        oc = ray_origin - sphere.center
        a = ray_direction.dot(ray_direction)
        b = 2.0 * oc.dot(ray_direction)
        c = oc.dot(oc) - sphere.radius * sphere.radius
        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            return sphere.color

    return None

# Usage
ray_origin = Vector3(0, 0, 0)
ray_direction = Vector3(0, 0, -1)
spheres = [Sphere(Vector3(0, 0, -5), 1, (255, 0, 0))]

result_color = ray_tracer(ray_origin, ray_direction, spheres)
print("Result from ray tracer:", result_color)