import pyrte_rrtmgp
print(pyrte_rrtmgp.__file__)
import rte_rrtmgp
print(rte_rrtmgp.__file__)
import pyrte_rrtmgp.kernels.rte
import pyrte_rrtmgp.kernels.rrtmgp
# from rte_rrtmgp import rte_lw_solver_noscat

func_names=["rte_lw_solver_noscat","rte_sw_solver_noscat","rte_lw_solver_2stream","rte_increment_1scalar_by_1scalar",
            "rte_increment_1scalar_by_2stream","rte_increment_1scalar_by_nstream", "rte_increment_2stream_by_1scalar",
            "rte_increment_2stream_by_2stream"]

for func in func_names:
    if not hasattr(rte_rrtmgp, func):
        raise ImportError("Function ", func, " is not available in rte_rrtmgp.")
    else:
        print(func, " exists in rte_rrtmgp")

func_names=["lw_solver_noscat", "lw_solver_2stream","sw_solver_noscat","sw_solver_2stream"]

for func in func_names:
    if not hasattr(pyrte_rrtmgp.kernels.rte, func):
        raise ImportError("Function ", func, " is not available in pyrte_rrtmgp.")
    else:
        print(func, " exists in pyrte_rrtmgp")

func_names=["interpolation", "compute_planck_source","compute_tau_absorption","compute_tau_rayleigh"]

for func in func_names:
    if not hasattr(pyrte_rrtmgp.kernels.rrtmgp, func):
        raise ImportError("Function ", func, " is not available in pyrte_rrtmgp.")
    else:
        print(func, " exists in pyrte_rrtmgp")

from pyrte_rrtmgp.rte_solver import RTESolver

if not hasattr(pyrte_rrtmgp.rte_solver, "RTESolver"):
    raise ImportError("Function ", func, " is not available in pyrte_rrtmgp.")
else:
    print(" RTESolver exists in pyrte_rrtmgp")


# func_names=["compute_quadrature", "compute_lw_fluxes_absorption", "compute_sw_fluxes", "solve"]
#
# for func in func_names:
#     if not hasattr(pyrte_rrtmgp.rte_solver.RTESolver, func ):
#         raise ImportError("Function ", func, " is not available in pyrte_rrtmgp.")
#     else:
#         print(func, " exists in pyrte_rrtmgp")

import pyrte_rrtmgp.rrtmgp_data

if not hasattr(pyrte_rrtmgp.rrtmgp_data, "download_rrtmgp_data"):
    raise ImportError("Function ", func, " is not available in pyrte_rrtmgp.")
else:
    print(" download_rrtmgp_data exists in pyrte_rrtmgp")

