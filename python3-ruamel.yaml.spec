%define		module		ruamel.yaml
Summary:	YAML 1.2 loader/dumper for Python 3
Summary(pl.UTF-8):	Biblioteka do wczytywania/zrzucania YAML-a 1.2 dla Pythona 3
Name:		python3-%{module}
Version:	0.18.14
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel-yaml/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml/%{module}-%{version}.tar.gz
# Source0-md5:	367c7a1c5cad44704ee06ee625e5a06e
URL:		https://pypi.org/project/ruamel.yaml/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:28.7.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML parser/emitter that supports roundtrip preservation of comments,
seq/map flow style and map key order.

%description -l pl.UTF-8
Biblioteka do analizy/tworzenia YAML-a zachowująca komentarze i
kolejność kluczy w mapach.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.md
%{py3_sitescriptdir}/ruamel/yaml
%{py3_sitescriptdir}/ruamel.yaml-%{version}-py*.egg-info
