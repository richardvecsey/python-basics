"""
Get platform data
-----------------
Input:      (None)

Output:     (string)    String contains specific data about platform.
                        It depends on the exact function.
"""
import platform



architecture = platform.architecture()
machine = platform.machine()
node = platform.node()
platform_platform = platform.platform(aliased=0, terse=0)
processor = platform.processor()
python_build = platform.python_build()
python_compiler = platform.python_compiler()
python_branch = platform.python_branch()
python_implementation = platform.python_implementation()
python_revision = platform.python_revision()
python_version = platform.python_version()
python_version_tuple = platform.python_version_tuple()
release = platform.release()
system = platform.system()
version = platform.version()
uname = platform.uname()

print('architecture: {}'.format(architecture))
print('machine: {}'.format(machine))
print('node: {}'.format(node))
print('platform: {}'.format(platform_platform))
print('processor: {}'.format(processor))
print('python_build: {}'.format(python_build))
print('python_compiler: {}'.format(python_compiler))
print('python_branch: {}'.format(python_branch))
print('python_implementation: {}'.format(python_implementation))
print('python_revision: {}'.format(python_revision))
print('python_version: {}'.format(python_version))
print('python_version_tuple: {}'.format(python_version_tuple))
print('release: {}'.format(release))
print('system: {}'.format(system))
print('version: {}'.format(version))
print('uname: {}'.format(uname))
