import cadquery as cq
result = (
    cq.Workplane("front")
    .ellipse(2, 4)
    .extrude(4)
    .faces(">Z")
    #.shell(-0.99999) # OK
    #.shell(-1.00000) # StdFail_NotDone: BRep_API: command not done
    #.shell(-1.00001)  # weird
    .shell(-1.7) # very odd
)
show_object(result)
