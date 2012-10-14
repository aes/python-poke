#include <Python.h>

PyObject *peek(PyObject *self, PyObject *args)
{
  unsigned long long q, l;

  if (!PyArg_ParseTuple(args, "KK", &q, &l))
    return NULL; /* exception raised by PyArg_ParseTuple, NULL is returned. */

  return PyString_FromStringAndSize((void *) q, l);
}


PyObject *poke(PyObject *self, PyObject *args)
{
  unsigned long long q, l;
  const char *s;

  if (!PyArg_ParseTuple(args, "Ks#", &q, &s, &l))
    return NULL; /* exception raised by PyArg_ParseTuple, NULL is returned. */

  memcpy((void *) q, s, l);

  Py_INCREF(Py_None);
  return Py_None;
}


PyMethodDef methods[] = {
  {"peek", peek},
  {"poke", poke},
  {NULL, NULL},
};

void initpoke(void)
{
  (void)Py_InitModule("poke", methods);
}
