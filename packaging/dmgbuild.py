import os

# dmgbuild settings for FlashDraft. The EULA resource makes macOS show a
# license dialog before the image can be mounted.
app = os.path.abspath("FlashDraft.app")
files = [app]
symlinks = {"Applications": "/Applications"}
license = os.path.abspath("packaging/EULA.rtf")
volume_name = "FlashDraft"
format = "UDZO"
icon = os.path.abspath("assets/flashdraft.icns")
window_rect = ((100, 100), (660, 400))
icon_locations = {
    "FlashDraft.app": (150, 180),
    "Applications": (500, 180),
}
