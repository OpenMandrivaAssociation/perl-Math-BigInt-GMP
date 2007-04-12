%define realname Math-BigInt-GMP

Summary:	High speed arbitrary size integer math
Name:		perl-%{realname}
Version:	1.18
Release: %mkrel 2
License:	Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{realname}
Source0:        ftp.perl.org/pub/CPAN/modules/by-module/Math/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	gmp-devel
BuildRequires:	perl(YAML)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains a replacement (drop-in) module for
Math::BigInt's core, Math::BigInt::Calc.pm.

%prep

%setup -n %{realname}-%{version}

%build
export CFLAGS="%{optflags}"
export OPTIMIZE="%{optflags}"

perl Makefile.PL INSTALLDIRS="vendor"

%make

make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc build BUGS CHANGES CREDITS INSTALL LICENSE NEW README SIGNATURE TODO
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/BigInt/
%dir %{perl_vendorarch}/auto/Math/BigInt/
%{perl_vendorarch}/auto/Math/BigInt/GMP/
%doc %{_mandir}/man*/*

