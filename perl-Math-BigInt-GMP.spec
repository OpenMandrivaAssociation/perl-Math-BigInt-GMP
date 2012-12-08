%define upstream_name    Math-BigInt-GMP
%define upstream_version 1.36

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	High speed arbitrary size integer math
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	gmp-devel
BuildRequires:	perl(YAML)
# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This package contains a replacement (drop-in) module for
Math::BigInt's core, Math::BigInt::Calc.pm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL INSTALLDIRS="vendor"
%make  CFLAGS="%{optflags}"

%check
export PERL5LIB=%{perl_vendorlib}
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc build BUGS CHANGES CREDITS INSTALL LICENSE README SIGNATURE TODO
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-4mdv2012.0
+ Revision: 765475
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-3
+ Revision: 763969
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-2
+ Revision: 676631
- rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.360.0-1
+ Revision: 643402
- update to new version 1.36

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.350.0-1
+ Revision: 637371
- update to new version 1.35

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.340.0-1
+ Revision: 636732
- new version

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 403853
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.24-5mdv2009.0
+ Revision: 257780
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.24-4mdv2009.0
+ Revision: 245827
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.24-2mdv2008.1
+ Revision: 152125
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2008.1
+ Revision: 78162
- new version


* Thu May 04 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.18-2mdk
- Fix According to perl Policy
	-Source URL
	- URL
- use mkrel

* Thu Oct 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.18-1mdk
- initial  Mandriva package

