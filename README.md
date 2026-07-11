# GeezTranslit

A Python package for converting **Latin phonetic input** to **Ethiopic (Ge'ez/Fidel) characters** and converting Ethiopic characters back to Latin.

GeezTranslit provides an easy way to type Amharic and other Ethiopic languages using a Latin keyboard.

---

## Features

✅ Latin → Ge'ez transliteration  
✅ Ge'ez → Latin transliteration  
✅ Traditional 8 Fidel order support  
✅ Support for related Ethiopic characters  
✅ Python package support  
✅ Simple integration into other applications  

---

## Fidel Order System

GeezTranslit follows the traditional Ethiopic Fidel order:

| Order | Name | Input | Example |
|---|---|---|---|
| 1st | Ge'ez (ግዕዝ) | `e` | `le` → ለ |
| 2nd | Ka'eb (ካእብ) | `u` | `lu` → ሉ |
| 3rd | Sals (ሳልስ) | `i` | `li` → ሊ |
| 4th | Ra'eb (ራዕብ) | `a` | `la` → ላ |
| 5th | Hams (ሀምስ) | `ie` | `lie` → ሌ |
| 6th | Sadis (ሳድስ) | consonant | `l` → ል |
| 7th | Sabe (ሳብዕ) | `o` | `lo` → ሎ |
| 8th | Dika'la (ዲቃላ) | `ua` | `lua` → ሏ |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/innovatorsemir/GeezTranslit.git
```

Move into the project:

```bash
cd GeezTranslit
```

Install:

```bash
pip install .
```

---

## Usage

Import the package:

```python
from geeztranslit import latin_to_geez, geez_to_latin
```

---

## Latin to Ge'ez

Example:

```python
print(latin_to_geez("selam"))
```

Output:

```
ሰላም
```

---

## Ge'ez to Latin

Example:

```python
print(geez_to_latin("ሰላም"))
```

Output:

```
selam
```

---

## Examples

### Basic Fidel

```
le    → ለ
lu    → ሉ
li    → ሊ
la    → ላ
lie   → ሌ
l     → ል
lo    → ሎ
lua   → ሏ
```

---

## Project Structure

```
GeezTranslit/
│
├── geeztranslit/
│   ├── __init__.py
│   └── transliterator.py
│
├── main.py
├── pyproject.toml
└── README.md
```

---

## Requirements

- Python 3.8+

Install dependencies:

```bash
pip install symspellpy
```

---

## Run Example

```bash
python main.py
```

Example:

```
Input:
selam

Output:
ሰላም
```

---

## License

Licensed under the GNU General Public License v3.0.

---

## Author

**innovatorsemir**

GitHub:

https://github.com/innovatorsemir/geeztranslit
