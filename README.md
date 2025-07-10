# Tree generator

The goal is to make a generator that generates trees procedurally in a terminal.

---

**IMPORTANT:**

This project needs the [`textual`](https://github.com/Textualize/textual) library.

Run it inside a Python virtual environment where `textual` is installed. (See below for a quick setup guide if needed)

---

### Quick `textual` virtual environment setup

#### 1. Clone the repo & create a virtual environment

On **Linux/macOS**:
```bash
python -m venv venv
source venv/bin/activate
pip install textual
```

On **Windows**:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install textual
```

#### 2. Each time before running the code, activate the venv

On **Linux/macOS**:
```bash
source venv/bin/activate
```

On **Windows**:
```bash
.\venv\Scripts\activate
```

#### 3. Run the code!

(Make sure your virtual environment is activated, see step 2.)

```bash
python tree-generator.py
```

---

Similar projects that I found inspiration from or took notes in how to make my own implementation:
- [Procedurally generating trees with space colonization algorithm](http://www.jgallant.com/procedurally-generating-trees-with-space-colonization-algorithm-in-xna/)
- [cbonsai](https://gitlab.com/jallbrit/cbonsai)
- [PyBonsai](https://github.com/Ben-Edwards44/PyBonsai)
