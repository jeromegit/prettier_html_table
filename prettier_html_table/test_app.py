from prettier_html_table import create_table

data = [[1,2,3,4],
        [11,22,33,44],
        [111,222,333,444]
        ]
header = ['header 1', 'header 2', 'header 3', 'header 4']

html_table = create_table(data, theme='yellow_dark', header=header, font_size='small', text_align='right')
print(html_table)