# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['./dev/mainfront.py'],
    pathex=[],
    binaries=[],
    datas=[
    ('dev/res/free-icon-add-button-8371340.png', 'res'),
    ('dev/res/free-icon-avatar-8370797.png', 'res'),
    ('dev/res/free-icon-hospital-signal-8371351.png', 'res'),
    ('dev/res/free-icon-search-8371297.png', 'res'),
    ('dev/res/icon.ico', 'res'),
    ('dev/res/icon.png', 'res'),
    ('dev/res/logo.jpg', 'res'),
    ('dev/res/logo.png', 'res'),
    ('dev/res/settings.png', 'res'),
    ('dev/docx/agreement.docx', 'docx'),

    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['dev\\res\\icon.ico'],
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Зерновой Трейдер',
)
