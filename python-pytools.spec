%define module	pytools

%define debug_package          %{nil}

Summary:	A collection of tools for Python
Name:		python-%{module}
Version:	2022.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/5b/0b/260d69e3e7c16af4af91198c5279004c9e8786ff33fae3760f3f4fc697b4/pytools-2022.1.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/%{module}
BuildArch:      noarch
BuildRequires:	python-setuptools
BuildRequires:	python-six


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
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{module} 
%doc README.rst PKG-INFO LICENSE
%{python3_sitelib}/*
