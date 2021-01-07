def render_tlay(tlay):
	result = [" "*77]*18

	def set_text(line, column, text):
		length = len(text)
		before = result[line][:column]
		after = result[line][column + length:]
		result[line] = before + text + after

	set_text(4, 1, "DATUM")
	set_text(5, 1, "DATE")

	set_text(4, 7, "ZEIT")
	set_text(5, 7, "TIME")

	set_text(4, 14, "VON/DE/FROM")
	set_text(4, 31, "->")
	set_text(4, 35, "NACH/A/TO")
	set_text(4, 52, "DATUM")
	set_text(5, 52, "DATE")
	set_text(4, 58, "ZEIT")
	set_text(5, 58, "TIME")
	set_text(4, 66, " KL.")
	set_text(5, 66, " CL.")

	for b in tlay.blocks:
		line = int(b.line)
		column = int(b.column)
		length = int(b.length)

		for part in b.text.split("\n"):
			set_text(line, column, part)
			line += 1

	return "\n".join(result)