// pywrap.cpp
#include <pybind11/pybind11.h>
#include "cpp_lib.h"

namespace py = pybind11;

PYBIND11_MODULE(CPPLib, m) {
    m.doc() = "optional module docstring";

    m.def("fact", &fact);
    m.def("isPrime", &isPrime);
    m.def("nThPrime", &nThPrime);
}