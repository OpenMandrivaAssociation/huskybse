%define name    huskybse
%define version 1.0.0
%define release %mkrel 7

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

