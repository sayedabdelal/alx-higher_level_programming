#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  Print information about a Python list.
 *
 * Parameters:
 * @p: PyObject* - Python list object
 * retun - void
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t listSize = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", listSize);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < listSize; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, typeName);
	}
}
