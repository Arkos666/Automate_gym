import re
from datetime import timedelta, date


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    substring = "SALSA CARDIO \\\\&quot;AL L&#205;MIT\\\\&quot;"
    txt_hora = '18:15'

    f = open("html.txt", "r")
    txt_html = f.read()
    f.close()

    EndDate = date.today() + timedelta(days=1)

    txt_button = "button"
    txt_data_hora = '{}-{:02d}-{:02d}T' + txt_hora + ':00'.format(EndDate.year, EndDate.month, EndDate.day)
    # print("SEARCH " + substring + " at " + txt_data_hora)

    txt_start = 'data-json="{&quot;Id&quot;:[0-9]{5},&quot;Nombre&quot;:&quot;'
    txt_end = '&quot;,&quot;HoraInicio&quot;:&quot;' \
              '[0-9]{4}-[0-9]{2}-[0-9]{2}T' + txt_hora + ':00'

    print("SEARCH " + txt_start + substring + txt_end)

    txt = re.search(txt_start + substring + txt_end, txt_html)

    print(txt.group())

    btn_id = re.search('[0-9]{5}', txt.group()).group()
    print("Button ID: " + btn_id)
    txt_time = txt.group()[-5:]

    print(txt_time)
