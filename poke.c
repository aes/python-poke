#include <Python.h>

PyMethodDef methods[] = {
  {NULL, NULL},
};

void initpoke(void)
{
  (void)Py_InitModule("poke", methods);
}
