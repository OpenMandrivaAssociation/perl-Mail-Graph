%define	upstream_name	 Mail-Graph
%define	upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Draw graphical stats for mails/spams
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(GD)
BuildRequires:	perl(GD::Graph)
BuildRequires:	perl(MIME::Tools)
BuildRequires:	perl(Date::Calc)
BuildRequires:	perl(Compress::Zlib)
BuildArch:	noarch

%description
This module parses mailbox files in either compressed or uncompressed form and
then generates pretty statistics and graphs about them. Although at first
developed to do spam statistics, it works just fine for normal mail.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES CREDITS README TODO
%{perl_vendorlib}/Mail
%{_mandir}/man3*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 403841
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.14-8mdv2009.0
+ Revision: 241703
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-6mdv2008.0
+ Revision: 46978
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.14-5mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.14-4mdk
- Add BuildRequires

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-3mdk
- spec cleanup
- fix buildrequires
- rpmbuildupdate aware
- better URL, summary and description

* Mon Jul 04 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14-2mdk
- rebuild

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.14-1mdk
- 0.14
- drop PREFIX and use %%makeinstall_std
- fix standard-dir-owned-by-package
- cosmetics

* Sun Jul 27 2003 Michael Scherer <scherer.michael@free.fr> 0.10-2mdk
- BuildRequires

* Wed Jul 23 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.10-1mdk
- initial cooker contrib.

