from unittest import TestCase
import py_cppmodel
import clang

# TODO(jbcoe): Move this setup to a a proper test setup function.
clang.cindex.Config.set_library_path('/Library/Developer/CommandLineTools/usr/lib/')
tu = clang.cindex.TranslationUnit.from_source(
    'sample.cc',
    ['-x', 'c++', '-std=c++20', '-stdlib=libc++'])
model = py_cppmodel.Model(tu)

class TestCppModel(TestCase):
    
    def test_filename(self):
        self.assertEqual(model.filename, 'sample.cc')
        
    def test_functions(self):
        self.assertEqual(len(model.functions), 2)
        self.assertEqual(str(model.functions[0]), "<py_cppmodel.Function double bar(double)>")
        self.assertEqual(str(model.functions[1]), "<py_cppmodel.Function int main()>")
        
    def test_classes(self):
        self.assertEqual(len(model.classes), 1)
        self.assertEqual(str(model.classes[0]), "<py_cppmodel.Class A>")
        
        self.assertEqual(len(model.classes[0].members), 3)
        self.assertEqual(str(model.classes[0].members[0]), "<py_cppmodel.Member <py_cppmodel.Type int> a>")
        self.assertEqual(str(model.classes[0].members[1]), "<py_cppmodel.Member <py_cppmodel.Type double> b>")
        self.assertEqual(str(model.classes[0].members[2]), "<py_cppmodel.Member <py_cppmodel.Type char[8]> c>")
        
        self.assertEqual(len(model.classes[0].methods), 1)
        self.assertEqual(str(model.classes[0].methods[0]), "<py_cppmodel.Method int foo(int)>")

