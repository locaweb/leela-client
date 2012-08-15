%define __python python2.6
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Leela client module
Name: {{ name }}
Version: {{ version }}
Release: 1
Group: Locaweb
License: APACHE2
URL: http://leela.rtfd.org/
BuildRoot: {{ build_dir }}
Source0: {{ source }}
BuildRequires: python2.6
BuildArch: noarch
Conflicts: python-leela
Requires: python2.6-setuptools, python2.6-psutil, python2.6-dns

# Packager Information
Packager: Bricklayer Builder <bricklayer@locaweb.com.br>

%description
{{ name }} Leela client module

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%{python_sitelib}/

%changelog

