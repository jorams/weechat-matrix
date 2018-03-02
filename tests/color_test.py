import webcolors
from hypothesis import given
from hypothesis.strategies import sampled_from

from matrix.colors import (Formatted, color_html_to_weechat,
                           color_weechat_to_html)

html_prism = ("<font color=maroon>T</font><font color=red>e</font><font "
              "color=olive>s</font><font color=yellow>t</font>")

weechat_prism = (
    u"\x1b[038;5;1mT\x1b[039m\x1b[038;5;9me\x1b[039m\x1b[038;5;3ms\x1b[039m\x1b[038;5;11mt\x1b[039m"
)

first_16_html_colors = list(webcolors.HTML4_HEX_TO_NAMES.values())


def test_prism():
    formatted = Formatted.from_html(html_prism)
    assert formatted.to_weechat() == weechat_prism


@given(sampled_from(first_16_html_colors))
def test_color_conversion(color_name):
    assert color_weechat_to_html(
        color_html_to_weechat(color_name)) == color_name
