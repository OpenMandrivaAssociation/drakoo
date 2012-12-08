# Changed by Makefile of cvs.
# do not edit here, but in cvs/soft/drakoo

Summary:  A file format wizard for OpenOffice.org
Name:     drakoo
Version:  0.13.2
Release:  %mkrel 5
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




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-5mdv2011.0
+ Revision: 663859
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-4mdv2011.0
+ Revision: 604823
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-3mdv2010.1
+ Revision: 522510
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-2mdv2010.0
+ Revision: 413390
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.13.2-1mdv2009.1
+ Revision: 367392
- updated translation

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.13.1-1mdv2009.1
+ Revision: 362323
- updated translation

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.13-2mdv2009.1
+ Revision: 350857
- rebuild

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2009.0
+ Revision: 286967
- updated translation

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12-2mdv2009.0
+ Revision: 220702
- rebuild

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.12-1mdv2008.1
+ Revision: 192107
- updated translation

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2008.1
+ Revision: 149263
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix URL

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.11-1mdv2008.0
+ Revision: 94247
- updated translation

* Sat Sep 15 2007 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2008.0
+ Revision: 86825
- translation snapshot


* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9-1mdv2007.1
+ Revision: 141957
- Import drakoo

* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9-1mdv2007.1
- fix finding icons with oofice-2.1
- translation snapshot

* Fri Sep 01 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.8-1mdv2007.0
- translation snapshot

* Mon Jan 02 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.7-1mdk
- fix crash due to API change in drakxtools (#20361)

* Mon Sep 26 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.6-2mdk
- translation snapshot

* Mon Feb 21 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-1mdk
- translation snapshot

* Wed Jan 05 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5-1mdk
- add Greek, Indonesian, Kirghiz, Kurdish, Turkish, Tajik, Urdu and
  Welsh translations
- update Portuguese Brazil translation

* Thu Nov 25 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-1mdk
- more translations

* Sat Oct 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-3mdk
- more translations

* Fri Oct 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-2mdk
- translation snapshot

* Thu Sep 23 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-1mdk
- prevent user from resizing the dialog
- add ar, da, et, eu, ja, nn, pt, sk and zh_CN translations

* Wed Sep 22 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-1mdk
- add Ukrainian and Walloon translations

* Tue Sep 21 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-1mdk
- initial release

