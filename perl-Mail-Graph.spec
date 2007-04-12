%define	module	Mail-Graph
%define	name	perl-%{module}
%define	version	0.14
%define	release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	draw graphical stats for mails/spams
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(GD)
BuildRequires:	perl-GDGraph
BuildRequires:	perl-MIME-tools
BuildRequires:	perl(Date::Calc)
BuildRequires:  perl(Compress::Zlib)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module parses mailbox files in either compressed or uncompressed form and
then generates pretty statistics and graphs about them. Although at first
developed to do spam statistics, it works just fine for normal mail.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README TODO
%{perl_vendorlib}/Mail
%{_mandir}/man3*/*

