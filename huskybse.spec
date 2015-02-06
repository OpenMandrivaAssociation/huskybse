%define name    huskybse
%define version 1.0.0
%define release 9

Summary:	Common files for all packages of the Husky-project
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		File tools
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://sourceforge.net/projects/husky/
Buildarch:	noarch

%description
This package contains some files common to all packages of the Husky-software.
Only needed if you want to compile the Husky-software yourself.

%prep
%setup -q -n %name

%build

perl -pi -e 's!^PREFIX=.*!PREFIX=%_prefix!' huskymak.cfg
perl -pi -e 's!^MANDIR=.*!MANDIR=%_mandir!' huskymak.cfg
perl -pi -e 's!^CFGDIR=.*!CFGDIR=%_sysconfdir/%name!' huskymak.cfg
perl -pi -e 's!^OPTCFLAGS=.*!OPTCFLAGS=-c -s %optflags!' huskymak.cfg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/husky
install -m 644 huskymak.cfg $RPM_BUILD_ROOT%{_datadir}/husky

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc bugreport.rus bugreport.txt ChangeLog DEPENDENCIES huskymak.cfg huskymak.cfg.bsd huskymak.cfg.debian huskymak.cfg.sun INSTALL README README.Makefiles develop-docs new
%dir %{_datadir}/husky/
%{_datadir}/husky/huskymak.cfg



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2011.0
+ Revision: 619492
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2010.0
+ Revision: 429481
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 247117
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-4mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import huskybse


* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.0.0-4mdk
- rebuild

* Tue Dec 23 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.0-3mdk
- fix %%optflags (grrr)
 
* Tue Dec 23 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.0-2mdk
- fix %%optflags in config
- it is not noarch (include %%optflags)

* Mon Dec 22 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.0-1mdk 
- cleanup
- From Iouri Goussev <elendal@polygonized.com>
  - First MDK version
  - original SPEC by Sergey Zhemchugov <Sergey_Zhemchugov@p8.f822.n463.z2.fidonet.org>
