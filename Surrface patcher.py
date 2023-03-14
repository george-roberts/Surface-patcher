#Author-George Roberts
#Description-Select a face and patch all holes.

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        selectFace = ui.selectEntity('Select BREP face', 'Faces')
        selectedFace = selectFace.entity
        doc = app.activeDocument
        des = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
        features = des.rootComponent.features
        patchFeatures = features.patchFeatures
        loops = None
        loops = selectedFace.loops
        for loop in loops:
            if not loop.isOuter:
                collection = adsk.core.ObjectCollection.create()
                for edge in loop.edges: collection.add(edge)
                patchInput = patchFeatures.createInput(collection, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                patchFeatures.add(patchInput)

        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
