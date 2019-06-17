from PIL import Image

def read_line_of_ints(text):
    """Given a string with integers in it, return a list of those integers."""
    ints = []
    ints_as_strs = split_line(text)

#     # def get_elevations(elevation_small.txt):
#    with open('elevation_small.txt') as file:
#        elevation_array = [line.split() for line in file]
#        elevations = [[int(e) for e in row] for row in elevation_array]
#        print(elevations)

    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints


def split_line(line):
    return line.split()


def read_file_into_list(filename):
    """Given a file, return a list of each line in the file as a string."""
    with open(filename) as file:
        return file.readlines()


def read_file_into_ints(filename):
    """Given a filename, read that file and then convert it to a list
    of lists of ints. Example:

    We have a file with these contents:
    1 2
    3 4

    The return value would be [[1, 2], [3, 4]]
    """
    lines = read_file_into_list(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_line_of_ints(line))
    return list_of_lists


class ElevationMap:
    """
    ElevationMap is a class that takes a matrix (list of lists, 2D)
    of integers and can be used to generate an image of those elevations
    like a standard elevation map.
    """

    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y, min_elevation, max_elevation):
        """Given an x, y coordinate, return the
        intensity level (used for grayscale in image) of
        the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
        return (elevation - min_elevation) / (max_elevation - min_elevation) * 255


    def draw_grayscale_gradient(self, filename, width, height):
        image = Image.new(mode='L', size=(width, height))
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()

        for x in range(width):
            for y in range(height):
                intensity = int(self.intensity_at_coordinate(x, y, min_elevation, max_elevation))
                image.putpixel((x, y), (intensity))
        image.save(filename)


if __name__ == "__main__":
    
    elevations = read_file_into_ints('elevation_small.txt')

    e_map = ElevationMap(elevations)
    
    e_map.draw_grayscale_gradient('relief_map.png', 600, 600)









