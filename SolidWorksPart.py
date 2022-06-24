from dataclasses import dataclass
import pythoncom
import win32com.client


# a template class that all other solidworks parts classes will inherit
@dataclass
class SolidWorksPart:
    # variable to fix scaling issue with solidworks, this may need to be
    # altered in the future in the event this scaling issue is fixed
    conversion = 1/39.3701

    # how I dispatch to the solidworks appication (communicate with it)
    # solidworks must be launched before this can function currently
    sw = win32com.client.Dispatch('SldWorks.Application')

    def __init__(self):

        # create a new part
        self.sw.newpart

        # sets up parameters we use to communicate with SolidWorks
        model = self.sw.ActiveDoc
        self.model_extension = model.Extension
        self.selection_manager = model.SelectionManager
        self.feature_manager = model.FeatureManager
        self.sketch_manager = model.SketchManager
        self.equation_manager = model.GetEquationMgr
        self.ARG_NULL = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)
