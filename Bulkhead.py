from dataclasses import dataclass

from SolidWorksPart import SolidWorksPart


@dataclass
class Bulkhead(SolidWorksPart):
    # required inputs when the class is created
    bulkhead_diameter: float
    u_bolt_holes: bool
    dowel_rod_holes: bool

    # optional inputs already have default values
    u_bolt_diameter: float = 0.0
    u_bolt_offset: float = 0.0

    dowel_diameter: float = 0.0
    dowel_offset: float = 0.0

    bulkhead_thickness = 0.125

    def __post_init__(self):
        super().__init__()
        # creates the actual bulkhead
        self._create_bulkhead_sketch()
        self._constrain_bulkhead()
        self._extrude_bulkhead()

        # adds U Bolt holes if needed
        if self.u_bolt_holes:
            self._create_u_bolt_holes()

        # adds Dowel Rod holes if needed
        if self.dowel_rod_holes:
            self._create_dowel_rod_holes()

    def _create_bulkhead_sketch(self):
        # selects the plane will will be working
        self.model_extension.SelectByID2(
            'Front Plane', 'PLANE', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        # inserts a new sketch
        self.sketch_manager.InsertSketch(True)
        # sketches the circle for the bulkhead
        bulkhead_radius = self.bulkhead_diameter*self.conversion/2
        self.sketch_manager.CreateCircleByRadius(0, 0, 0, bulkhead_radius)

    # dimnesionally constrains the bulkhead, divide by 50 for scaling issues
    def _constrain_bulkhead(self):
        self.model_extension.SelectByID2(
            'Line1', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.bulkhead_diameter/50, 0, 0)
        self.model_extension.SelectByID2(
            'Line2', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.bulkhead_diameter/50, 0, 0)

    # extrudes the bulkhead to designated thickness
    def _extrude_bulkhead(self):
        self.model_extension.SelectByID2(
            'Sketch1', 'SKETCH', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.feature_manager.FeatureExtrusion2(
            True, False, False, 0, 0, self.bulkhead_thickness*self.conversion,
            0.001, False, False, False, False, 0, 0, False, False, False,
            False, True, True, True, 0, 0, False)

    def _create_u_bolt_holes(self):
        # scaling and conversion corrections
        u_bolt_offset = self.u_bolt_offset*self.conversion/2
        u_bolt_radius = self.u_bolt_diameter*self.conversion/2

        # sketching and constraining u_bolts
        self._sketch_and_constrain_right_u_bolt(u_bolt_offset, u_bolt_radius)
        self._sketch_and_constrain_left_u_bolt(u_bolt_offset, u_bolt_radius)

        # extrudes the cut to make the holes
        self._extude_both_u_bolts()

    def _create_dowel_rod_holes(self):
        # scaling and conversion corrections
        dowel_offset = self.dowel_offset*self.conversion/2
        dowel_radius = self.dowel_diameter*self.conversion/2

        # makes top dowel rod holes
        self._sketch_and_constrain_top_dowel(dowel_offset, dowel_radius)
        # makes bottom dowel rod holes
        self._sketch_and_constrain_bottom_dowel(dowel_offset, dowel_radius)

        # extrudes the cuts for the dowel rod holes
        self._extrude_both_dowel_holes()

    def _sketch_and_constrain_right_u_bolt(self, u_bolt_offset, u_bolt_radius):
        # selects the front plane and creates a new sketch
        self.model_extension.SelectByID2(
            'Front Plane', 'PLANE', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.sketch_manager.InsertSketch(True)

        # creating the right circle for the U-bolt
        self.sketch_manager.CreateCircleByRadius(
            u_bolt_offset, 0, 0, u_bolt_radius)
        # constrains the right u-bolt hole
        self.model_extension.SelectByID2(
            'Line1', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.u_bolt_diameter/50, 0, 0)

    def _sketch_and_constrain_left_u_bolt(self, u_bolt_offset, u_bolt_radius):
        # creates the left circle for u-bolt
        self.sketch_manager.CreateCircleByRadius(
            -u_bolt_offset, 0, 0, u_bolt_radius)
        # constrains the left u-bolt hole
        self.model_extension.SelectByID2(
            'Line2', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.u_bolt_diameter/50, 0, 0)

    def _extude_both_u_bolts(self):
        self.model_extension.SelectByID2(
            'Sketch2', 'SKETCH', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.feature_manager.FeatureCut3(
            False, False, False, 1, 0, 100, 100, False, False, False, False, 0,
            0, False, False, False, False, False, True, True, False, False, 
            False, 0, 0, False)

    def _sketch_and_constrain_top_dowel(self, dowel_offset, dowel_radius):
        # creates new sketch
        self.model_extension.SelectByID2(
            'Front Plane', 'PLANE', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.sketch_manager.InsertSketch(True)
        # makes top dowel rod holes
        self.sketch_manager.CreateCircleByRadius(
            0, dowel_offset, 0, dowel_radius)
        self.model_extension.SelectByID2(
            'Line1', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.dowel_diameter/50, 0, 0)

    def _sketch_and_constrain_bottom_dowel(self, dowel_offset, dowel_radius):
        self.sketch_manager.CreateCircleByRadius(
            0, -dowel_offset, 0, dowel_radius)
        self.model_extension.SelectByID2(
            'Line2', 'SKETCHSEGMENT', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.model_extension.AddDimension(0, self.dowel_diameter/50, 0, 0)

    def _extrude_both_dowel_holes(self):
        # if no u-bolt sketch, the API will treat 'Sketch3' as 'Sketch2'
        self.model_extension.SelectByID2(
            'Sketch3', 'SKETCH', 0, 0, 0, False, 0, self.ARG_NULL, 0)
        self.feature_manager.FeatureCut3(
            False, False, False, 1, 0, 100, 100, False, False, False, False, 0,
            0, False, False, False, False, False, True, True, False, False,
            False, 0, 0, False)
