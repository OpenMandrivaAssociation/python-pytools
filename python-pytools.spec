%define module	pytools

Summary:	A collection of tools for Python
Name:		python-%{module}
Version:	2011.5
Release:	2
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		no-distribute.patch
License:	MIT
Group:		Development/Python
Url:		http://mathema.tician.de/software/pytools
BuildArch:	noarch
Requires:	python-decorator >= 3.2.0
BuildRequires:	python-setuptools >= 0.6c8
%py_requires -d

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
%patch0 -p0

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc README


%changelog
* Fri Nov 18 2011 Lev Givon <lev@mandriva.org> 2011.5-1
+ Revision: 731619
- Update to 2011.5.

* Mon Aug 29 2011 Lev Givon <lev@mandriva.org> 2011.4-1
+ Revision: 697393
- Update to 2011.4.

* Thu Apr 21 2011 Lev Givon <lev@mandriva.org> 2011.3-1
+ Revision: 656499
- Update to 2011.3.

* Wed Mar 23 2011 Lev Givon <lev@mandriva.org> 2011.2-1
+ Revision: 648141
- Update to 2011.2.

* Tue Feb 15 2011 Lev Givon <lev@mandriva.org> 2011.1-1
+ Revision: 637852
- Update to 2011.1.

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 11-2mdv2011.0
+ Revision: 593998
- rebuild for py2.7

  + Lev Givon <lev@mandriva.org>
    - Update to 11.

* Mon Mar 01 2010 Lev Givon <lev@mandriva.org> 10-1mdv2010.1
+ Revision: 512980
- Update to 10.

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 9-1mdv2010.0
+ Revision: 384254
- update to new version 9

* Mon Feb 02 2009 Lev Givon <lev@mandriva.org> 7-1mdv2009.1
+ Revision: 336704
- import python-pytools


