# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ultrasound_app.py'],
    pathex=[],
    binaries=[('C:\\\\anaconda\\\\envs\\\\pytorch\\\\Lib\\\\site-packages\\\\cv2\\\\*.dll', 'cv2'), ('C:\\\\anaconda\\\\envs\\\\pytorch\\\\Lib\\\\site-packages\\\\PIL\\\\*.pyd', 'PIL')],
    datas=[('image', 'image')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='ultrasound_app',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
