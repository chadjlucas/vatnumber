#This file is part of vatnumber.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Unit test for vatnumber
'''

import unittest
import vatnumber


class VatNumberTest(unittest.TestCase):
    '''
    Test Case for vatnumber
    '''

    def test_check_vat_at(self):
        '''
        Test check_vat_at
        '''
        self.assert_(vatnumber.check_vat_at('U12345675'))

    def test_check_vat_be(self):
        '''
        Test check_vat_be
        '''
        self.assert_(vatnumber.check_vat_be('1234567894'))

    def test_check_vat_bg(self):
        '''
        Test check_vat_bg
        '''
        self.assert_(vatnumber.check_vat_bg('1234567892'))

    def test_check_vat_cy(self):
        '''
        Test check_vat_cy
        '''
        self.assert_(vatnumber.check_vat_cy('12345678F'))

    def test_check_vat_cz(self):
        '''
        Test check_vat_cz
        '''
        for test in ('12345679', '612345670', '991231123', '6306150004'):
            self.assert_(vatnumber.check_vat_cz(test))

    def test_check_vat_de(self):
        '''
        Test check_vat_de
        '''
        self.assert_(vatnumber.check_vat_de('123456788'))

    def test_check_vat_dk(self):
        '''
        Test check_vat_dk
        '''
        self.assert_(vatnumber.check_vat_dk('12345674'))

    def test_check_vat_ee(self):
        '''
        Test check_vat_ee
        '''
        self.assert_(vatnumber.check_vat_ee('123456780'))

    def test_check_vat_es(self):
        '''
        Test check_vat_es
        '''
        for test in ('A12345674', 'P1234567D', '12345678Z', 'K1234567L'):
            self.assert_(vatnumber.check_vat_es(test))

    def test_check_vat_fi(self):
        '''
        Test check_vat_fi
        '''
        self.assert_(vatnumber.check_vat_fi('12345671'))

    def test_check_vat_fr(self):
        '''
        Test check_vat_fr
        '''
        for test in ('32123456789', '2H123456789'):
            self.assert_(vatnumber.check_vat_fr(test))

    def test_check_vat_gb(self):
        '''
        Test check_vat_gb
        '''
        for test in ('GD123', 'HA567', '123456782', '1234567823',
                '001123456782', '0011234567823'):
            self.assert_(vatnumber.check_vat_gb(test))

    def test_check_vat_gr(self):
        '''
        Test check_vat_gr
        '''
        for test in ('12345670', '123456783'):
            self.assert_(vatnumber.check_vat_gr(test))

    def test_check_vat_hu(self):
        '''
        Test check_vat_hu
        '''
        self.assert_(vatnumber.check_vat_hu('12345676'))

    def test_check_vat_ie(self):
        '''
        Test check_vat_ie
        '''
        for test in ('7A12345J', '1234567T'):
            self.assert_(vatnumber.check_vat_ie(test))

    def test_check_vat_it(self):
        '''
        Test check_vat_it
        '''
        self.assert_(vatnumber.check_vat_it('12345670017'))

    def test_check_vat_lt(self):
        '''
        Test check_vat_lt
        '''
        for test in ('123456715', '123456789011'):
            self.assert_(vatnumber.check_vat_lt(test))

    def test_check_vat_lu(self):
        '''
        Test check_vat_lu
        '''
        self.assert_(vatnumber.check_vat_lu('12345613'))

    def test_check_vat_lv(self):
        '''
        Test check_vat_lv
        '''
        for test in ('41234567891', '15066312345'):
            self.assert_(vatnumber.check_vat_lv(test))

    def test_check_vat_mt(self):
        '''
        Test check_vat_mt
        '''
        self.assert_(vatnumber.check_vat_mt('12345634'))

    def test_check_vat_nl(self):
        '''
        Test check_vat_nl
        '''
        self.assert_(vatnumber.check_vat_nl('123456782B90'))

    def test_check_vat_pl(self):
        '''
        Test check_vat_pl
        '''
        self.assert_(vatnumber.check_vat_pl('1234567883'))

    def test_check_vat_pt(self):
        '''
        Test check_vat_pt
        '''
        self.assert_(vatnumber.check_vat_pt('123456789'))

    def test_check_vat_ro(self):
        '''
        Test check_vat_ro
        '''
        for test in ('1234567897', '1630615123457'):
            self.assert_(vatnumber.check_vat_ro(test))

    def test_check_vat_se(self):
        '''
        Test check_vat_se
        '''
        self.assert_(vatnumber.check_vat_se('123456789701'))

    def test_check_vat_si(self):
        '''
        Test check_vat_si
        '''
        self.assert_(vatnumber.check_vat_si('12345679'))

    def test_check_vat_sk(self):
        '''
        Test check_vat_sk
        '''
        for test in ('0012345675', '0012345678', '531231123', '6306151234'):
            self.assert_(vatnumber.check_vat_sk(test))

if __name__ == '__main__':
    unittest.main()
