%define module pytools

Name:		python-pytools
Summary:	A collection of tools for Python
Version:	2026.1.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://documen.tician.de/pytools
Source0:	https://github.com/inducer/pytools/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:  noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those. If you're curious nonetheless, here's what's on offer:

* A ton of small tool functions such as len_iterable, argmin, tuple
  generation, permutation generation, ASCII table pretty printing,
  GvR's mokeypatch_xxx() hack, the elusive flatten, and much more.
* Michele Simionato's decorator module.
* A time-series logging module, pytools.log.
* Batch job submission, pytools.batchjob.
* A lexer, pytools.lex.

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
