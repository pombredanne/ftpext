#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ftpext
----------------------------------

Tests for `ftpext` module.
"""

import unittest
import os
from ftpext import FTPExt


def load_secure_ftp():
    ftps = FTPExt('ftp.intel.com', '21', 'anonymous',
                  'anonymous@', True, True, 0)
    ftps.set_pasv(True)
    return ftps


def load_ftp():
    ftp = FTPExt('mirrors.se.kernel.org', '21', 'anonymous',
                 'anonymous@', False, True, 0)
    ftp.set_pasv(True)
    return ftp

ftp = load_ftp()
ftps = load_secure_ftp()


class TestFtpext(unittest.TestCase):

    def test_basic_functionality(self):
        ftp.cwd('/')
        ftps.cwd('/')
        dev_null_byte = open(os.devnull, "wb")
        dev_null_string = open(os.devnull, "w")
        ftp.retrlines('RETR welcome.msg', dev_null_string.write)
        ftp.retrbinary('RETR welcome.msg', dev_null_byte.write)
        ftps.prot_p()
        ftps.retrlines('RETR readme.txt', dev_null_string.write)
        ftps.retrbinary('RETR readme.txt', dev_null_byte.write)
        ftps.prot_c()
        ftps.retrlines('RETR readme.txt', dev_null_string.write)
        ftps.retrbinary('RETR readme.txt', dev_null_byte.write)
        dev_null_byte.close()
        dev_null_string.close()

    def test_ls(self):
        ftp.cwd('debian-cd')
        dir_list = ftp.ls()
        self.assertEqual(len(dir_list), 6)
        self.assertIn('project', dir_list)
        self.assertIn('current', dir_list)
        self.assertIn('ls-lR.gz', dir_list)
        self.assertTrue(dir_list['project']['dir'])
        self.assertFalse(dir_list['project']['symlink'])
        self.assertFalse(dir_list['project']['device'])
        self.assertFalse(dir_list['project']['file'])
        self.assertTrue(dir_list['current']['symlink'])
        self.assertFalse(dir_list['current']['dir'])
        self.assertFalse(dir_list['current']['device'])
        self.assertFalse(dir_list['current']['file'])
        self.assertTrue(dir_list['ls-lR.gz']['file'])
        self.assertFalse(dir_list['ls-lR.gz']['dir'])
        self.assertFalse(dir_list['ls-lR.gz']['device'])
        self.assertFalse(dir_list['ls-lR.gz']['symlink'])
        self.assertEqual(dir_list['ls-lR.gz']['filesize'],
                         ftp.size('ls-lR.gz'))

    def test_last_com_log(self):
        ftp.pwd()
        self.assertEqual(ftp.last_command, 'PWD')
        self.assertEqual(ftp.last_response_code, '257')
        self.assertIn('257 "/"', ftp.last_response)
        self.assertIn('257 "/"', ftp.log.split('\n')[-1])

    def tearDownModule(self):
        ftp.quit()
        ftps.quit()

if __name__ == '__main__':
    unittest.main()
