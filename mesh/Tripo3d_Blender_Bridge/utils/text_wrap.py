"""Text wrapping helpers for the sidebar panel.

Blender clips label text that does not fit the region instead of wrapping it,
which hides most of a status line in a default-width sidebar. These helpers
estimate how many characters fit and split the text into several labels.

The module deliberately avoids importing ``bpy`` so the wrapping logic stays
testable outside Blender; only ``draw_wrapped_label`` touches a UILayout, and it
does so through the layout object it is given.
"""
import unicodedata

# Average glyph advance of the Blender UI font at ui_scale 1.0, in pixels. This
# slightly overestimates a lowercase latin glyph so the estimate errs towards
# wrapping one word early rather than clipping it.
CHAR_WIDTH_PX = 6.8

# Horizontal space a label icon takes, including its gap, at ui_scale 1.0.
ICON_WIDTH_PX = 20.0


def char_units(ch):
    """Return the display width of *ch* in units of one narrow glyph."""
    if unicodedata.combining(ch):
        return 0
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1


def display_units(text):
    """Return the display width of *text* in units of one narrow glyph."""
    return sum(char_units(ch) for ch in text)


def units_for_width(width_px, ui_scale=1.0):
    """Return how many narrow glyphs fit into *width_px*."""
    return max(1, int(width_px / (CHAR_WIDTH_PX * ui_scale)))


def _split_units(text, max_units):
    """Split *text* so the first part is at most *max_units* wide."""
    used = 0
    for index, ch in enumerate(text):
        width = char_units(ch)
        if used + width > max_units and index:
            return text[:index], text[index:]
        used += width
    return text, ""


def _tokenize(text):
    """Break *text* into atomic pieces greedy wrapping may place on a line.

    Runs of narrow non-space characters stay together so latin words are not
    split, wide characters become individual tokens because CJK text carries no
    spaces to break on, and spaces are emitted as their own separators.
    """
    tokens = []
    word = ""
    for ch in text:
        if ch.isspace():
            if word:
                tokens.append(word)
                word = ""
            tokens.append(" ")
        elif char_units(ch) == 2:
            if word:
                tokens.append(word)
                word = ""
            tokens.append(ch)
        else:
            word += ch
    if word:
        tokens.append(word)
    return tokens


def _wrap_paragraph(text, max_units):
    lines = []
    current = ""
    for token in _tokenize(text):
        if token == " ":
            # A trailing space is only worth keeping when the next token can
            # still follow it on this line.
            if current and display_units(current) + 1 <= max_units:
                current += " "
            elif current:
                lines.append(current)
                current = ""
            continue

        if display_units(current) + display_units(token) <= max_units:
            current += token
            continue

        if current:
            lines.append(current.rstrip())
            current = ""
        while display_units(token) > max_units:
            head, token = _split_units(token, max_units)
            lines.append(head)
        current = token

    if current:
        lines.append(current.rstrip())
    return lines or [""]


def wrap_text(text, max_units):
    """Wrap *text* to lines at most *max_units* narrow glyphs wide."""
    lines = []
    for paragraph in text.split("\n"):
        lines.extend(_wrap_paragraph(paragraph, max_units))
    return lines


def draw_wrapped_label(layout, text, width_px, ui_scale=1.0, icon='NONE'):
    """Draw *text* as one label per line, wrapped to *width_px*.

    Continuation lines of an icon label are indented with a blank icon so the
    text keeps a single left edge.
    """
    available_px = width_px
    if icon != 'NONE':
        available_px -= ICON_WIDTH_PX * ui_scale

    column = layout.column(align=True)
    for index, line in enumerate(wrap_text(text, units_for_width(available_px, ui_scale))):
        if icon == 'NONE':
            column.label(text=line)
        else:
            column.label(text=line, icon=icon if index == 0 else 'BLANK1')
    return column
