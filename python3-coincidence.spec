#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Helper functions for pytest
Summary(pl.UTF-8):	Funkcje pomocnicze dla pytesta
Name:		python3-coincidence
Version:	0.6.5
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/coincidence/
Source0:	https://files.pythonhosted.org/packages/source/c/coincidence/coincidence-%{version}.tar.gz
# Source0-md5:	0d1d08cdbef6030dd91c44219ec77892
Patch0:		coincidence-deps.patch
URL:		https://pypi.org/project/coincidence/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-domdf-python-tools >= 2.8.0
BuildRequires:	python3-pytest >= 6.2.0
BuildRequires:	python3-pytest-regressions >= 2.0.2
%if "%{_ver_lt '%{py3_ver}' '3.8'}" == "1"
BuildRequires:	python3-typing-extensions >= 3.7.4.3
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.749
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helper functions for pytest.

%description -l pl.UTF-8
Funkcje pomocnicze dla pytesta.

%prep
%setup -q -n coincidence-%{version}
%patch0 -p1

cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/coincidence
%{py3_sitescriptdir}/coincidence-%{version}-py*.egg-info
