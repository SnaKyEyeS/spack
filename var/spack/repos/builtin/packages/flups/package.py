# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Flups(MakefilePackage):
    """FLUPS - A Fourier-based Library of Unbounded Poisson Solvers"""

    # GitHub repository
    git="ssh://git@git.immc.ucl.ac.be:examples/flups.git"

    # Versions
    version("develop", branch="develop") 

    # Dependencies
    depends_on("mpi")
    depends_on("hdf5")
    depends_on("fftw")
    depends_on("h3lpr")

    def edit(self, spec, prefix):
        # Use MPI's compiler
        env["CC"] = spec["mpi"].mpicc
        env["CXX"] = spec["mpi"].mpicxx
        env["F77"] = spec["mpi"].mpif77
        env["FC"] = spec["mpi"].mpifc
        # Set the install prefix
        env["PREFIX"] = prefix
        # Set the arch file
        env["ARCH_FILE"] = "make_arch/make.spack"
        # Write out said arch file
        arch_file = {
            "CC": spec["mpi"].mpicc,
            "CXX": spec["mpi"].mpicxx,
            "CCFLAGS": "-03 -fopenmp -std=c++17 -DNDEBUG -DNO_PROF",
            "CXXFLAGS": "-03 -fopenmp -std=c99 -DNDEBUG -DNO_PROF",
            "LDFLAGS": "-fopenmp",
            # FFTW
            "FFTW_DIR": prefix,
            "FFTW_LIB": prefix.lib,
            "FFTW_DIR": prefix.dir,
            # HDF5
            "HDF5_DIR": prefix,
            "HDF5_LIB": prefix.lib,
            "HDF5_DIR": prefix.dir,
            # H3LPR
            "H3LPR_DIR": prefix,
            "H3LPR_LIB": prefix.lib,
            "H3LPR_DIR": prefix.dir,
            # Set no libname for Accfft, to override the dep
            "ACCFFT_LIBNAME": "",
        }
        with open(env["ARCH_FILE"]) as f:
            for key in arch_file:
                f.write(f"{key}:={arch_file[key]}")

