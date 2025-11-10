# Vibe: Chinese Character Block (Prototype)

This is a single-file Pygame prototype implementing the core gameplay for the
three subgames described in `PRD.txt`.

## Run (Desktop)

```bash
python -m venv .venv
# Windows PowerShell
. .venv\\Scripts\\Activate.ps1
pip install -r vibe/requirements.txt
python vibe/src/main.py
```

Run from the project root so the prototype can find `level*.json/txt` and
`idiom_level*.json/txt` at the root.

## Controls

- Left/Right: move falling block horizontally
- Down: accelerate fall
- Space: rotate 90° (认汉字 only)
- Type letters: pinyin input (认字写拼音)
- Mouse: click left column buttons to choose a subgame; click blocks (组成语)

## Notes

- The prototype uses your existing `level*.json/txt` and `idiom_level*.json/txt`
  datasets at the project root.
- Level-up triggers after ~10% of the items are answered correctly.
- Points: 5×level (认汉字/认字写拼音), 10 (组成语).
- Visuals and effects are simple placeholders; packaging scripts will be added
  in a later step.

### Optional sound

Place a `fireworks.wav` at `assets/fireworks.wav` to enable the firework sound.

## Build Executable (PyInstaller)

To package the game as a standalone executable:

```bash
cd vibe
pip install pyinstaller (if not already installed)
pyinstaller build.spec
```

The executable will be in the `dist` folder. The build includes:
- All level JSON files (level1.json through level14.json)
- All idiom level JSON files (idiom_level1.json through idiom_level6.json)
- The SimHei font file (assets/simhei.ttf)
- Optional fireworks sound file


