# Changed by Makefile of cvs.
# do not edit here, but in cvs/soft/drakoo

Summary:  A file format wizard for OpenOffice.org
Name:     drakoo
Version:  0.13.2
Release:  %mkrel 3
# get the source from our SVN repository (see
# http://svn.mandriva.com/)
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    Office
Url:      http://www.mandrivalinux.com/en/cvs.php3
BuildArch: noarch
BuildRequires: gettext 
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools > 10-56mdk
BuildRoot: %_tmppath/%name-%version-buildroot

%description
This wizard is run on first run of OpenOffice.org and enables to
select the default file format (either native OpenOffice.org one or
Microsoft(R) Office).

%prep
%setup -q

%build
perl -pi -e 's/^use strict/#use strict/g' drakoo

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%_bindir/*


