# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

# Get the directory where this spec file is located
spec_dir = os.path.dirname(os.path.abspath(SPEC))
# Get the project root (parent of vibe directory)
project_root = os.path.dirname(spec_dir)

# Collect all data files
datas = []

# Add all level JSON files (level1.json through level14.json)
for i in range(1, 15):
    level_file = os.path.join(project_root, f'level{i}.json')
    if os.path.exists(level_file):
        datas.append((level_file, '.'))

# Add all idiom level JSON files (idiom_level1.json through idiom_level6.json)
for i in range(1, 7):
    idiom_file = os.path.join(project_root, f'idiom_level{i}.json')
    if os.path.exists(idiom_file):
        datas.append((idiom_file, '.'))

# Include the font file
font_file = os.path.join(project_root, 'assets', 'simhei.ttf')
if os.path.exists(font_file):
    datas.append((font_file, 'assets'))

# Optionally include fireworks sound if it exists
fireworks1 = os.path.join(project_root, 'assets', 'fireworks.wav')
if os.path.exists(fireworks1):
    datas.append((fireworks1, 'assets'))

fireworks2 = os.path.join(project_root, 'vibe', 'assets', 'fireworks.wav')
if os.path.exists(fireworks2):
    datas.append((fireworks2, 'assets'))

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ChineseCharacterBlock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging, False for release
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you have one
)

