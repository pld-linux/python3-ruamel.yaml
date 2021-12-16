#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		ruamel.yaml
Summary:	YAML 1.2 loader/dumper for Python 2
Summary(pl.UTF-8):	Biblioteka do wczytywania/zrzucania YAML-a 1.2 dla Pythona 2
Name:		python-%{module}
Version:	0.16.10
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.yaml/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml/%{module}-%{version}.tar.gz
# Source0-md5:	02774e7ed3273b3d8eee6c08326b91c4
URL:		https://pypi.org/project/ruamel.yaml/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:28.7.0
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:28.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML parser/emitter that supports roundtrip preservation of comments,
seq/map flow style and map key order.

%description -l pl.UTF-8
Biblioteka do analizy/tworzenia YAML-a zachowująca komentarze i
kolejność kluczy w mapach.

%package -n python3-%{module}
Summary:	YAML 1.2 loader/dumper for Python 3
Summary(pl.UTF-8):	Biblioteka do wczytywania/zrzucania YAML-a 1.2 dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
YAML parser/emitter that supports roundtrip preservation of comments,
seq/map flow style and map key order.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka do analizy/tworzenia YAML-a zachowująca komentarze i
kolejność kluczy w mapach.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/ruamel/yaml
%{py_sitescriptdir}/ruamel.yaml-%{version}-py*.egg-info
%{py_sitescriptdir}/ruamel.yaml-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/ruamel/yaml
%{py3_sitescriptdir}/ruamel.yaml-%{version}-py*.egg-info
%{py3_sitescriptdir}/ruamel.yaml-%{version}-py*-nspkg.pth
%endif
