import cadquery as cq
result = (
    cq.Workplane("front")
    .ellipse(10, 20)
    .extrude(40)
    .faces(">Z")
    #.shell(-0.30) # OK
    #.shell(-4.99999) # OK
    #.shell(-5.00000) # StdFail_NotDone: BRep_API: command not done
    #.shell(-5.00001)  # weird
    .shell(-9) # very odd
)
show_object(result)

#import io
#tolerance=0.001
#f = io.open(f'shellellipse-direct-{tolerance}.stl', 'w+')
#cq.exporters.exportShape(result, cq.exporters.ExportTypes.STL, f, tolerance)
#f.close()
