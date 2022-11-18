#MenuTitle: Fractal corners generator
# -*- coding: utf-8 -*-

__doc__="""
Generate fractals from corner components
"""

from copy import copy
from Foundation import NSPoint


################################################################################
#
# Input values

PREFIX = "_corner.fractal"
COUNT = 6 # CAUTION: save your work before increasing this!
SCALE = 0.9

#
################################################################################


def main():

	Glyphs.clearLog()

	# Get indexes of selected nodes to attach corners to
	nodes = [n.index for n in Glyphs.font.selectedLayers[0].selection]

	# Remove any previously generated corner glyphs, since we'll be regenerating them
	corners = [c for c in Glyphs.font.glyphs if c.name.startswith(PREFIX) and c.name != PREFIX+"0"]
	for c in corners:
		del Glyphs.font.glyphs[c.name]

	# Remove previously generated corner hints from the base corner glyph
	for layer in Glyphs.font.glyphs[PREFIX+"0"].layers:
		while len(layer.hints):
			del layer.hints[0]

	# Duplicate the corner and add it to the previous corner. Repeat n=count times.
	for i in range(1,COUNT):
		prevGlyph = Glyphs.font.glyphs[f"{PREFIX}{i-1}"]
		newGlyph = prevGlyph.copy()
		newGlyph.name = f"{PREFIX}{i}"
		Glyphs.font.glyphs.append(newGlyph)
		for layer in prevGlyph.layers:
			for n in nodes:
				newHint = GSHint()
				newHint.name = f"{PREFIX}{i}"
				newHint.type = CORNER
				newHint.originNode = layer.shapes[0].nodes[n]
				newHint.options = 2 # centred
				newHint.scale = NSPoint(SCALE**i,SCALE**i)
				layer.hints.append(newHint)

	# Refresh metrics
	for i in range(COUNT):
		for layer in Glyphs.font.glyphs[f"{PREFIX}{i}"].layers:
			layer.syncMetrics()

if __name__ == '__main__':
	main()