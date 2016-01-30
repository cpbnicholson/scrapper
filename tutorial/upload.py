from oauth2client.client import SignedJwtAssertionCredentials
import json
import gspread

def main():
    json_key = json.load(open('/Users/cnicholson/PycharmProjects/Scrapper/scrapper/tutorial/House Prices-1588e3b20535.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    wks = gc.open("HousePrices").sheet1

    file = open("items.json", "r")
    stuff = json.loads(file.read())

    cells = wks.range("A1:H40")

    cells[0].value = 'price'
    cells[1].value = 'size'
    cells[2].value = 'price/m2'
    cells[3].value = 'beds'
    cells[4].value = 'description'
    cells[5].value = 'ber'
    cells[6].value = 'address'
    cells[7].value = 'url'

    i = 1
    for each in stuff:

        add_cell(1, i, each.get('price'), cells)
        add_cell(2, i, each.get('size'), cells)
        if each.get('size'): add_cell(3, i, int(each.get('price')) / int(each.get('size')), cells)
        add_cell(4, i, each.get('beds'), cells)
        add_cell(5, i, each.get('description'), cells)
        add_cell(6, i, each.get('ber'), cells)
        add_cell(7, i, each.get('address'), cells)
        add_cell(8, i, each.get('url'), cells)

        i += 1
    print 'done'

    # Update in batch
    wks.update_cells(cells)

def add_cell(c, r, val, cells):
    if val:
        cells[(r*8 + c)-1].value = val
        print 'next'


main()