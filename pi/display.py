import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

lcd.clear()

rows = [''] * 2


def print_first_line(text):
    if len(text) < len(rows[0]):
        lcd.clear()
        print_second_line(rows[1])

    rows[0] = text[0:16]
    lcd.cursor_position(0, 0)
    lcd.message = rows[0]


def print_second_line(text):
    if len(text) < len(rows[1]):
        lcd.clear()
        print_first_line(rows[0])

    rows[1] = text[0:16]
    lcd.cursor_position(0, 1)
    lcd.message = rows[1]
