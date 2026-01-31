def romanizer(numbers):
   roman_values = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }
   
   roman_numbers = []

   def int_to_roman(n):
      letter = ''
      for value, symbol in reversed(roman_values.items()):
         print('n= ', n)
         while value <= n:
            letter += symbol
            n -= value

      return letter
            

   for n in numbers:
      roman_numbers.append(int_to_roman(n))
   
   print(roman_numbers)

romanizer([1, 49, 23])