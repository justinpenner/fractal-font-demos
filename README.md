# Fractal Font Demos

Generating fractals using components in [Glyphs](https://glyphsapp.com/).

## How to use

1. Copy `Fractal corners generator.py` to your Glyphs scripts folder. You can find the scripts folder in Glyphs via *Script > Open Scripts Folder*. Instead of copying the script, you can hold Cmd+Opt while dragging it to create an alias, if you prefer.
2. Open `FractalCornersDemo1.glyphs` and edit the `_corner.fractal0` glyph. This is the base glyph for your fractal.
3. Select a couple of nodes in the base glyph to use as attachment points. The script will detect which nodes are selected.
4. Run `Fractal corners generator.py` (find it in the *Script* menu). The script will generate several copies of the base glyph and attach them to the previous copy.

Then, if you like, you can change the input values found near the top of `Fractal corners generator.py`. For example, `COUNT` is the number of copies, or in other words the number of times the fractal iterates. `SCALE` is useful if you want to rescale each iteration.

### ⚠️ CAUTION ⚠️

- Avoid too many overlaps in the branches of your fractal design. Your font might fail to export.
- Be careful adjusting the iteration `COUNT`! Each iteration doubles the complexity, so your app or your system might freeze or crash beyond 5–10 iterations.
