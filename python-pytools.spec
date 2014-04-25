%define module	pytools

Summary:	A collection of tools for Python

Name:		python-%{module}
Version:	2014.1.2
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://mathema.tician.de/software/pytools
Source0:	http://pypi.python.org/packages/source/p/pytools/pytools-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-devel
Requires:	pkgconfig(python)

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

%prep
%setup -qn %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc README




