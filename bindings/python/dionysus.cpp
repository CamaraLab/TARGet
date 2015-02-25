#include <utilities/log.h>
#include <boost/python.hpp>
#include "utils.h"

namespace bp = boost::python;
namespace dp = dionysus::python;

void export_simplex();
void export_filtration();
void export_static_persistence();
void export_dynamic_persistence_chains();
void export_chain();
void export_birthid();
void export_point();
void export_persistence_diagram();

void export_rips();
void export_pairwise_distances();

BOOST_PYTHON_MODULE(_dionysus)
{
    bp::to_python_converter<std::pair<double, bool>, dp::PairToTupleConverter<double, bool> >();

    export_simplex();
    export_filtration();
    export_static_persistence();
    export_dynamic_persistence_chains();
    export_chain();
    export_point();
    export_persistence_diagram();

    export_birthid();

    export_rips();
    export_pairwise_distances();

};
