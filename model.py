import bpy

animList = []
addedList = []

for i in bpy.data.actions:
    print(i)
#     if not i.name.startswith('bone_root'):
#         continue

#     newName = i.name.split('|')[1].replace('Student_Name_', '')
    
#     if newName in addedList:
#         continue

#     i.name = newName
    
#     animList.append(i)
#     addedList.append(newName)

# for obj in bpy.context.scene.objects:
#     if obj.parent is None:
#         obj.scale = (1, 1, 1)

# obj = bpy.context.object

# for i in animList:
#     print(i)
#     nla_track = obj.animation_data.nla_tracks.new()
#     nla_track.strips.new(i.name, 0, i)
     
# for material in bpy.data.materials:
#     material.blend_method = 'OPAQUE'
#     if not material.use_nodes:
#         material.metallic = 0
#         continue
#     for n in material.node_tree.nodes:
#         if n.type == 'BSDF_PRINCIPLED':
#             n.inputs["Metallic"].default_value = 0