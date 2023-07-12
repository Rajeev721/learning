import unittest as ut

import sys

# to use  python -m unittest -v the files names should start with test
# # adding Folder_2 to the system path
# sys.path.insert(0, 'C:\VersionControl\learning\python\Course\Python_Course_Andrei\projects\gussinggame')

import guessing

class testingguess(ut.TestCase):
    def testguess(self):
        result = guessing.guess(6,7)
        self.assertTrue(result)
    def testguessval(self):
        result = guessing.guess()
        self.assertIsInstance(ValueError)

if __name__ == '__main__':
    ut.main()