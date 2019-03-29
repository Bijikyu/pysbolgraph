
from pysbolgraph.SBOL2Graph import SBOL2Graph
from pysbolgraph.terms import Biopax, SBOL2
from glob import glob
import json
import requests


def load(f):
    file = open(f, 'r')
    s = file.read()
    file.close()
    return s


files = glob('SBOLTestSuite/SBOL2/*.xml')

for file in files:
    print('🐍🐍🐍 ' + file)
    g = SBOL2Graph()
    g.load(file)

    new_filename = "out/" + file

    f = open(new_filename, "wb+")
    f.write(g.serialize_xml())
    f.close()

    request = {
        'options': {
            'language': 'SBOL2',
            'test_equality': True,
            'check_uri_compliance': False,
            'check_completeness': False,
            'check_best_practices': False,
            'continue_after_first_error': True,
            'provide_detailed_stack_trace': False,
            'insert_type': False,
            'uri_prefix': 'http://foo/',
            'main_file_name': 'main file',
            'diff_file_name': 'comparison file',
        },
        'return_file': False,
        'main_file': load(file),
        'diff_file': load(new_filename)
    }

    resp = requests.post(
        "http://www.async.ece.utah.edu/validate/", json=request)

    r = resp.json()

    if r['valid']:
        print('✅ Valid')
    else:
        print('❌ NOT valid')

    for e in r['errors']:
        if "Namespace" in e:
            continue
        if len(e.strip()) > 0:
            print('⚠️  ' + e)