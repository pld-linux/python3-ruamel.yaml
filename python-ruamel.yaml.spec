# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		ruamel.yaml
Summary:	YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style and map key order
Name:		python-%{module}
Version:	0.16.6
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.yaml/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml/%{module}-%{version}.tar.gz
# Source0-md5:	6a0b7fe48578cf8e4a77d788ac4fe58b
URL:		https://pypi.org/project/ruamel.yaml/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML parser/emitter that supports roundtrip preservation of comments,
seq/map flow style and map key order.

%package -n python3-%{module}
Summary:	YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style and map key order
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
YAML parser/emitter that supports roundtrip preservation of comments,
seq/map flow style and map key order.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitedir}/ruamel/yaml

%py_install

%py_postclean
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitedir}/ruamel/yaml

%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{py_sitescriptdir}/ruamel/yaml
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/%{module}-%{version}-py*-nspkg.pth
%dir %{py_sitedir}/ruamel/yaml
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{py3_sitescriptdir}/ruamel/yaml
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py3_sitescriptdir}/%{module}-%{version}-py*-nspkg.pth
%dir %{py3_sitedir}/ruamel/yaml
%endif
