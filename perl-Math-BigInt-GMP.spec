%define module  Math-BigInt-GMP
%define name	perl-%{module}
%define version 1.24
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	High speed arbitrary size integer math
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	gmp-devel
BuildRequires:	perl(YAML)
# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87

%description
This package contains a replacement (drop-in) module for
Math::BigInt's core, Math::BigInt::Calc.pm.

%prep
%setup -q -n %{module}-%{version}

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

