DEFAULT_THEME = 'blue_dark'
DEFAULT_FONT_FAMILY = 'Arial, Helvetica, sans-serif'
DEFAULT_FONT_SIZE = 'medium'
DEFAULT_TEXT_ALIGN = 'left'

class ThemeColors:
    def __init__(self, header_fg_color, header_bg_color, border, odd_bg_color, even_bg_color):
        self.header_fg_color = header_fg_color
        self.header_bg_color = header_bg_color
        self.border = border
        self.odd_bg_color = odd_bg_color
        self.even_bg_color = even_bg_color

THEME_COLORS = { # header_fg_color header_bg_color border odd_bg_color even_bg_color
    'blue_dark': ThemeColors('#FFFFFF', '#305496', '#305496', '#D9E1F2', '#FFFFFF'),
    'blue_light': ThemeColors('#305496', '#FFFFFF', '#305496', '#D9E1F2', '#FFFFFF'),
    'green_dark': ThemeColors('#FFFFFF', '#548235', '#548235', '#E2EFDA', '#FFFFFF'),
    'green_light': ThemeColors('#548235', '#FFFFFF', '#548235', '#E2EFDA', '#FFFFFF'),
    'grey_dark': ThemeColors('#FFFFFF', '#808080', '#808080', '#EDEDED', '#FFFFFF'),
    'grey_light': ThemeColors('#808080', '#FFFFFF', '#808080', '#EDEDED', '#FFFFFF'),
    'orange_dark': ThemeColors('#FFFFFF', '#C65911', '#C65911', '#FCE4D6', '#FFFFFF'),
    'orange_light': ThemeColors('#C65911', '#FFFFFF', '#C65911', '#FCE4D6', '#FFFFFF'),
    'red_dark': ThemeColors('#FFFFFF', '#823535', '#823535', '#efdada', '#FFFFFF'),
    'red_light': ThemeColors('#823535', '#FFFFFF', '#823535', '#efdada', '#FFFFFF'),
    'yellow_dark': ThemeColors('#FFFFFF', '#BF8F00', '#BF8F00', '#FFF2CC', '#FFFFFF'),
    'yellow_light': ThemeColors('#BF8F00', '#FFFFFF', '#BF8F00', '#FFF2CC', '#FFFFFF'),
}


def create_html_start():
    return '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" 
xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    '''

def create_css(theme, font_family, font_size, text_align):
    theme = theme.lower()
    if theme in THEME_COLORS:
        tc = THEME_COLORS[theme]
    else:
        raise ValueError(f"theme:{theme} is an invalid theme. It should be on of these themes:{THEME_COLORS.keys()}")

    return '''
<STYLE TYPE="text/css">
body {
   font-family: %s;
   font-size: %s;
}
table {
   border: 0px;
   border-collapse: collapse;
   
}

td, th {
   font-family: %s;
   font-size: %s;
   text-align: %s;
   padding: 0px 5px 0px 5px;
   white-space: nowrap;
}
th {   
   border-bottom: 2px solid %s;
}

thead, tfoot {
   color: %s;
   background: %s;
   font-weight: bold;
   text-align: center;
}

tr.odd  { background: %s; }
tr.even { background: %s; }
</STYLE>
</HEADER>
''' % (font_family, font_size, font_family, font_size, text_align, tc.border,
       tc.header_fg_color, tc.header_bg_color,
       tc.odd_bg_color, tc.even_bg_color)

def create_row(row_data, is_header, row_number=0):
    if is_header:
        element = 'TH'
        odd_or_even_class =''
    else:
        element = 'TD'
        odd_or_even = 'odd' if row_number % 2 else 'even'
        odd_or_even_class = f'CLASS="{odd_or_even}"'

    return f'<TR {odd_or_even_class}>' + " ".join(map(lambda v: f'<{element}>{v}</{element}>', row_data)) + "</TR>"

def create_table(data,
                 header=None, footer=None,
                 theme=DEFAULT_THEME,
                 font_family=DEFAULT_FONT_FAMILY, font_size=DEFAULT_FONT_SIZE,
                 text_align=DEFAULT_TEXT_ALIGN,
                 add_line_number=None
                 ):

    if type(data) is list and all(type(l) is list for l in data):
        if header:
            header_data = header
            body_data = data
        else:
            header_data = data[0]
            body_data = data[1:]
    elif type(data).__name__ == 'DataFrame':
        if header:
            header_data = header
        else:
            header_data = data.columns.to_list()
            body_data = data.values.tolist()
    else:
        raise Exception(f"data:{data} must either be a list of lists or a pandas.DataFrame")


    body = '<BODY><TABLE>'
    body = body + "<THEAD>" + create_row(header_data, True) + "</THEAD>"
    body = body + "<TBODY>"
    r = 1
    for row in body_data:
        body = body + create_row(row, False, r)
        r += 1
    body = body + "<TBODY>"
    body = body + "</TABLE>"

    html = create_html_start() + create_css(theme, font_family, font_size, text_align) + body

    return html





