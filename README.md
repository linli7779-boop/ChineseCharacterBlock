
## Setup

### Option 1: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r vibe/requirements.txt

# Run the game
python vibe/src/main.py
```

### Option 2: Using Conda

```bash
conda activate ChineseCharacterBlock
pip install -r vibe/requirements.txt
python vibe/src/main.py
```

## Building Executable

To create a standalone executable:

```bash
cd vibe
pip install pyinstaller
pyinstaller build.spec
```

The executable will be in `vibe/dist/ChineseCharacterBlock.exe`

## Requirements

- Python 3.7+
- pygame 2.5.2
- pyinstaller (for building executable)

See `vibe/requirements.txt` for details.
