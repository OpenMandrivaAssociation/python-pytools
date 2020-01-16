%define module	pytools

%define debug_package          %{nil}

Summary:	A collection of tools for Python
Name:		python-%{module}
Version:	2020.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/66/c7/88a4f8b6f0f78d0115ec3320861a0cc1f6daa3b67e97c3c2842c33f9c089/pytools-2020.1.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/%{module}
BuildArch:      noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	python-six
BuildRequires:	python2-six
BuildRequires:	pkgconfig(python2)


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


%package -n python2-%{module} 
Summary:	A collection of tools for Python 3
Group:		Development/Python
BuildArch:	noarch
Obsoletes:      python-pytools < 2018.5.2
Provides:       python-pytools = %{version}-%{release}
#(eatdirt) packages needed this should be updated and fixed (TODO)
Obsoletes:      python-tools < 2018.5.2
Provides:       python-tools = %{version}-%{release}


%description -n python2-%{module} 
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
cp -a . %{py3dir}

%build
%py2_build
pushd %{py3dir}
%py3_build
popd

%install
%py2_install
pushd %{py3dir}
%py3_install
popd

%files -n python-%{module} 
%doc README.rst PKG-INFO LICENSE
%{python3_sitelib}/*

%files -n python2-%{module}
%doc README.rst PKG-INFO LICENSE
%{python2_sitelib}/*

