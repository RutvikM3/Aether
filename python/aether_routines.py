#!/usr/bin/env python

from netCDF4 import Dataset
import datetime as dt
import numpy as np

def read_aether_header(filelist):
    """ Obtain ancillary information from the netCDF file

    Get some ancillary information from the netcdf file.  This simply
    mirrors the gitm header info.

    Parameters
    ----------
    filelist : list
        A list of netcdf file names.  The number of files is recorded, but only the last
        file is used.

    Returns
    -------
    header : dict
        A dictionary containing header information from the netCDF files, including:
        nFilles - number of files in list
        nLons - number of longitude grids
        nLats - number of latitude grids
        nAlts - number of altitude grids
        nVars - number of data variable names
        time - list of datetimes with data
    """

    header = {"nFiles": len(filelist),
              "version": 0.1, \
              "nLons": 0, \
              "nLats": 0, \
              "nAlts": 0, \
              "nVars": 0, \
              "vars": [], \
              "time": [], \
              "filename": [filelist[-1]] }
    
    with Dataset(filelist[-1], 'r') as ncfile:
        header["nVars"] = 0
        for var in ncfile.variables.values():
            if (len(var.shape) == 3):
                header["nLons"] = var.shape[0]
                header["nLats"] = var.shape[1]
                header["nAlts"] = var.shape[2]
                header["vars"].append(var.name)
                header["nVars"] += 1

        base = dt.datetime(1965, 1, 1, 0, 0, 0)
        time = np.array(ncfile.variables['Time'])
        current = base + dt.timedelta(seconds=time[0])
        header["time"].append(current)

    return header
    

def read_aether_one_file(file, vars):
    """ Read in list of variables from a single netCDF file

    Parameters
    ----------
    file : str
        Name of netCDF file to read
    vars : list
        List of desired variable names to read

    Returns
    -------
    data : dict
        Dict with keys 'time', which contains a datetime object specifying the time of
        the file and indices ranging from 0 to `len(vars) - 1`, corresponding to the
        variable names in `vars` that holds arrays of the specified dat
    
    """

    with Dataset(file, 'r') as ncfile:
        # Save the data as numpy arrays, using variable index as a key
        data = {i_var: np.array(ncfile.variables[var]) for i_var, var in enumerate(vars)}
        
        # Calculate the date and time for this data
        base = dt.datetime(1965, 1, 1)
        time = np.array(ncfile.variables['Time'])
        data['time'] = base + dt.timedelta(seconds=time[0])

    return data
    