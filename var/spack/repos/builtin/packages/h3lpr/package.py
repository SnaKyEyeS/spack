# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class H3lpr(MakefilePackage):
    """Helper library for profiling, logging, and parsing."""

    # Versions
    version("develop", 
            branch="develop", 
            git="ssh://git@github.com/van-Rees-Lab/h3lpr.git")

    # Dependencies
    depends_on("mpi")

    def edit(self, spec, prefix):
        # Use MPI's compiler
        env['CC'] = spec['mpi'].mpicc
        env['CXX'] = spec['mpi'].mpicxx
        env['F77'] = spec['mpi'].mpif77
        env['FC'] = spec['mpi'].mpifc
        # Set the install prefix
        env["PREFIX"] = prefix
        # Other arguments ?
