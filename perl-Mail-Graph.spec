%define	upstream_name	 Mail-Graph
%define	upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	draw graphical stats for mails/spams
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(GD)
BuildRequires:	perl-GDGraph
BuildRequires:	perl-MIME-tools
BuildRequires:	perl(Date::Calc)
BuildRequires:  perl(Compress::Zlib)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module parses mailbox files in either compressed or uncompressed form and
then generates pretty statistics and graphs about them. Although at first
developed to do spam statistics, it works just fine for normal mail.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
