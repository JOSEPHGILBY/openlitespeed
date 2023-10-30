import os
import sys
import glob
import gdb.printing

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

# Get a list of all .py files in the pretty_printers directory
printer_files = glob.glob('/workspaces/openlitespeed/pretty_printers/*.py')

# Create an instance of the pretty printer
pp = gdb.printing.RegexpCollectionPrettyPrinter("my_library")

for file in printer_files:
    # Skip the load_all.py script
    if os.path.basename(file) != 'load_all.py':
        # Import the module
        module_name = os.path.splitext(os.path.basename(file))[0]
        module = __import__(module_name)

        pascal_case_module_name = ''.join(word.title() for word in module_name.split('_'))
        
        # Add the printer from this module to "my_library"
        pp.add_printer(module_name, '^' + pascal_case_module_name + '(<.*>)?$', module.build_pretty_printer())

# Register "my_library" with gdb
gdb.printing.register_pretty_printer(gdb.current_objfile(), pp)