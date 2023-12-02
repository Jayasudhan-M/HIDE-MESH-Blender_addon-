bl_info = {
    "name": "Hide Masked Area in Sculpting",
    "author": "OpenAI",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N Panel > Hide Masked",
    "description": "Hide masked area of the mesh in sculpt mode",
    "category": "Sculpting",
}

import bpy

class SCULPT_OT_hide_masked(bpy.types.Operator):
    bl_idname = "sculpt.hide_masked"
    bl_label = "Hide Masked"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.mode == 'SCULPT'

    def execute(self, context):
        bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
        return {'FINISHED'}


class SCULPT_OT_unhide_all(bpy.types.Operator):
    bl_idname = "sculpt.unhide_all"
    bl_label = "Unhide All"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.mode == 'SCULPT'

    def execute(self, context):
        bpy.ops.paint.hide_show(action='SHOW', area='ALL')
        return {'FINISHED'}


class SCULPT_PT_hide_masked_panel(bpy.types.Panel):
    bl_label = "Hide Masked"
    bl_idname = "SCULPT_PT_hide_masked_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        layout.operator("sculpt.hide_masked", text="Hide Masked")
        layout.operator("sculpt.unhide_all", text="Unhide All")


def register():
    bpy.utils.register_class(SCULPT_OT_hide_masked)
    bpy.utils.register_class(SCULPT_OT_unhide_all)
    bpy.utils.register_class(SCULPT_PT_hide_masked_panel)


def unregister():
    bpy.utils.unregister_class(SCULPT_PT_hide_masked_panel)
    bpy.utils.unregister_class(SCULPT_OT_unhide_all)
    bpy.utils.unregister_class(SCULPT_OT_hide_masked)


if __name__ == "__main__":
    register()
