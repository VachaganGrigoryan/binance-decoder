#include <Python.h>

PyObject* binance_decoder(PyObject *self, PyObject *args);


int PyArgParseTuple(PyObject* args, const char** ptr, Py_ssize_t* size) {
    return PyArg_ParseTuple(args, "s", ptr, size);
}

static struct PyMethodDef methods[] = {
    {"binance_decoder", (PyCFunction)binance_decoder, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "binance_decoder",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_binance_decoder(void) {
    return PyModule_Create(&module);
}



