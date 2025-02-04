import bpy

def rename_shapekeys(shapekey_mapping):
    for shapekey in bpy.data.shape_keys:
        for keyblock in shapekey.key_blocks:
            old_name = keyblock.name
            new_name = shapekey_mapping.get(old_name)
            
            if new_name:
                print(f"Now processing: {old_name}")
                keyblock.name = new_name
                print(f"Renamed to: {new_name}")
            else:
                print(f"Skipped: {old_name}")

shapekey_mapping = {
    "A01_Brow_Inner_Up": "browInnerUp",
    "A02_Brow_Down_Left": "browDownLeft",
    "A03_Brow_Down_Right": "browDownRight",
    "A04_Brow_Outer_Up_Left": "browOuterUpLeft",
    "A05_Brow_Outer_Up_Right": "browOuterUpRight",
    "A06_Eye_Look_Up_Left": "eyeLookUpLeft",
    "A07_Eye_Look_Up_Right": "eyeLookUpRight",
    "A08_Eye_Look_Down_Left": "eyeLookDownLeft",
    "A09_Eye_Look_Down_Right": "eyeLookDownRight",
    "A10_Eye_Look_Out_Left": "eyeLookOutLeft",
    "A11_Eye_Look_In_Left": "eyeLookInLeft",
    "A12_Eye_Look_In_Right": "eyeLookInRight",
    "A13_Eye_Look_Out_Right": "eyeLookOutRight",
    "A14_Eye_Blink_Left": "eyeBlinkLeft",
    "A15_Eye_Blink_Right": "eyeBlinkRight",
    "A16_Eye_Squint_Left": "eyeSquintLeft",
    "A17_Eye_Squint_Right": "eyeSquintRight",
    "A18_Eye_Wide_Left": "eyeWideLeft",
    "A19_Eye_Wide_Right": "eyeWideRight",
    "A20_Cheek_Puff": "cheekPuff",
    "A21_Cheek_Squint_Left": "cheekSquintLeft",
    "A22_Cheek_Squint_Right": "cheekSquintRight",
    "A23_Nose_Sneer_Left": "noseSneerLeft",
    "A24_Nose_Sneer_Right": "noseSneerRight",
    "A26_Jaw_Forward": "jawForward",
    "A27_Jaw_Left": "jawLeft",
    "A28_Jaw_Right": "jawRight",
    "A29_Mouth_Funnel": "mouthFunnel",
    "A30_Mouth_Pucker": "mouthPucker",
    "A31_Mouth_Left": "mouthLeft",
    "A32_Mouth_Right": "mouthRight",
    "A33_Mouth_Roll_Upper": "mouthRollUpper",
    "A34_Mouth_Roll_Lower": "mouthRollLower",
    "A35_Mouth_Shrug_Upper": "mouthShrugUpper",
    "A36_Mouth_Shrug_Lower": "mouthShrugLower",
    "A37_Mouth_Close": "mouthClose",
    "A38_Mouth_Smile_Left": "mouthSmileLeft",
    "A39_Mouth_Smile_Right": "mouthSmileRight",
    "A40_Mouth_Frown_Left": "mouthFrownLeft",
    "A41_MouthFrown_Right": "mouthFrownRight",
    "A42_Mouth_Dimple_Left": "mouthDimpleLeft",
    "A43_Mouth_Dimple_Right": "mouthDimpleRight",
    "A44_Mouth_Upper_Up_Left": "mouthUpperUpLeft",
    "A45_Mouth_Upper_Up_Right": "mouthUpperUpRight",
    "A46_Mouth_Lower_Down_Left": "mouthLowerDownLeft",
    "A47_Mouth_Lower_Down_Right": "mouthLowerDownRight",
    "A48_Mouth_Press_Left": "mouthPressLeft",
    "A49_Mouth_Press_Right": "mouthPressRight",
    "A50_Mouth_Stretch_Left": "mouthStretchLeft",
    "A51_Mouth_Stretch_Right": "mouthStretchRight",
    "A52_Tongue_Out": "tongueOut",
    "Merged_Open_Mouth": "jawOpen",
}

rename_shapekeys(shapekey_mapping)
