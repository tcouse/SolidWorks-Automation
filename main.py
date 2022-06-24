from Bulkhead import Bulkhead

# edit these variables in order to change the dimensions of the bulkheads
bulkhead_diameter = 10
u_bolt_holes = True
dowel_rod_holes = True
u_bolt_diameter = .75
u_bolt_offset = 5
dowel_diameter = .3
dowel_offset = 7


def create_part(bulkhead_diameter, u_bolt_holes, dowel_rod_holes,
                u_bolt_diameter, u_bolt_offset, dowel_diameter, dowel_offset):
    print('Be sure to launch SolidWorks before you continue.')
    Bulkhead(bulkhead_diameter, u_bolt_holes, dowel_rod_holes, u_bolt_diameter,
             u_bolt_offset, dowel_diameter, dowel_offset)
    print('Part Complete')


if __name__ == '__main__':
    create_part(bulkhead_diameter, u_bolt_holes, dowel_rod_holes,
                u_bolt_diameter, u_bolt_offset, dowel_diameter, dowel_offset)
