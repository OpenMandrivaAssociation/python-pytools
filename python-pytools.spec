%define module	pytools
%define name	python-%{module}
%define version 9
%define release %mkrel 1

Summary:	A collection of tools for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://mathema.tician.de/software/pytools
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools >= 0.6c8
%py_requires -d

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those. If you're curious nonetheless, here's what's on offer:

* A ton of small tool functions such as len_iterable, argmin, tuple
  generation, permutation generation, ASCII table pretty printing,
  Michele Simionato's decorator module, GvR's mokeypatch_xxx() hack,
  the elusive flatten, and much more.
* A time-series logging module, pytools.log.
* Batch job submission, pytools.batchjob.
* A lexer, pytools.lex.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README