#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lookup3.h"

static PyObject *
lookup3_hashlittle(PyObject *self, PyObject *args)
{
	const char *string;
	uint32_t hash;
	char ret[9];

	if (!PyArg_ParseTuple(args, "s", &string))
		return NULL;
	hash = hashlittle(string, strlen(string), 0);
	snprintf(ret, sizeof(ret), "%.8lx", hash);
	return Py_BuildValue("s", ret);
}

static PyMethodDef lookup3_methods[] = {
		/* The cast of the function is necessary since PyCFunction values
		 * only take two PyObject* parameters, and keywdarg_parrot() takes
		 * three.
		 */
		{"hashlittle", (PyCFunction)lookup3_hashlittle,
		 METH_VARARGS | METH_KEYWORDS,
		 "Returns a hash based on lookup3 little hash"},
		{NULL, NULL, 0, NULL}	 /* sentinel */
};

void
initlookup3(void)
{
	Py_InitModule("lookup3", lookup3_methods);
}
