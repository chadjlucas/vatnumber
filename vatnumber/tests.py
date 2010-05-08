#This file is part of vatnumber.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Unit test for vatnumber
'''

import unittest
import vatnumber

VAT_NUMBERS = [
    ('AT', 'U12345675'),
    ('AL', 'K99999999L'),
    ('BE', '0123456749'),
    ('BG', '1234567892'),
    ('BG', '175074752'),
    ('BG', '131202360'),
    ('BG', '040683212'),
    ('CL', '334441113'),
    ('CO', '9001279338'),
    ('CY', '12345678F'),
    ('CZ', '12345679'),
    ('CZ', '612345670'),
    ('CZ', '991231123'),
    ('CZ', '6306150004'),
    ('DE', '123456788'),
    ('DK', '12345674'),
    ('EE', '123456780'),
    ('ES', 'A12345674'),
    ('ES', 'P1234567D'),
    ('ES', 'K1234567L'),
    ('ES', 'R9600075G'),
    ('ES', 'W4003922D'),
    ('ES', 'V99218067'),
    ('ES', 'U99216632'),
    ('ES', 'J99216582'),
    ('ES', 'U99216426'),
    ('ES', '12345678Z'),
    ('ES', 'X5277343Q'),
    ('ES', 'Y5277343F'),
    ('ES', 'Z5277343K'),
    ('FI', '12345671'),
    ('FR', '32123456789'),
    ('FR', '2H123456789'),
    ('GB', 'GD123'),
    ('GB', 'GD888812326'),
    ('GB', 'HA567'),
    ('GB', 'HA888856782'),
    ('GB', '123456782'),
    ('GB', '1234567823'),
    ('GB', '001123456782'),
    ('GB', '0011234567823'),
    ('GB', '242338087388'),
    ('GR', '12345670'),
    ('GR', '123456783'),
    ('HU', '12345676'),
    ('IE', '7A12345J'),
    ('IE', '1234567T'),
    ('IT', '12345670017'),
    ('LT', '123456715'),
    ('LT', '123456789011'),
    ('LU', '12345613'),
    ('LV', '41234567891'),
    ('LV', '15066312345'),
    ('MT', '12345634'),
    ('NL', '123456782B90'),
    ('PL', '1234567883'),
    ('PT', '123456789'),
    ('RO', '24736200'),
    ('RO', '1234567897'),
    ('RO', '1630615123457'),
    ('RU', '5505035011'),
    ('RU', '550501929014'),
    ('SE', '123456789701'),
    ('SI', '12345679'),
    ('SK', '0012345675'),
    ('SK', '0012345678'),
    ('SK', '531231123'),
    ('SK', '6306151234'),
    ('SM', '12345'),
    ('UA', '12345678'),
]

VIES_NUMBERS = [
    'BE0897290877',
]


class VatNumberTest(unittest.TestCase):
    '''
    Test Case for vatnumber
    '''

    def test_vat_numbers(self):
        '''
        Test VAT numbers
        '''
        for code, number in VAT_NUMBERS:
            self.assert_(getattr(vatnumber,
                'check_vat_' + code.lower())(number), code + ' ' + number)

    def test_vies(self):
        '''
        Test vies
        '''
        for vat in VIES_NUMBERS:
            self.assert_(vatnumber.check_vies(vat))

if __name__ == '__main__':
    unittest.main()
