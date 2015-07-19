Summary:	A file format wizard for OpenOffice.org
Name:		drakoo
Version:	0.13.2
Release:	13
License:	GPLv2
Group:		Office
Url:		http://www.mandrivalinux.com/en/cvs.php3
# get the source from our SVN repository (see
# http://svn.mandriva.com/)
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	gettext 
BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools

%description
This wizard is run on first run of OpenOffice.org and enables to
select the default file format (either native OpenOffice.org one or
Microsoft(R) Office).

%prep
%setup -q

%build
sed -i -e 's/^use strict/#use strict/g' drakoo

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING
%{_bindir}/*

